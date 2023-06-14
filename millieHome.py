from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

chrome_options = Options()
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_experimental_option('detach', True)
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

service_obj = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service_obj, options=chrome_options)

driver.implicitly_wait(5)

driver.get('https://hyelight.github.io/millie/')

driver.maximize_window()

# ------------- PC 환경 테스트 -------------

# step-1 : Millie 로고 클릭 시 상단 이동
driver.execute_script('window.scrollBy(0, document.body.scrollHeight)')
time.sleep(2)
driver.find_element(By.XPATH, "//img[@src='img/millie-logo.png']").click()

time.sleep(1)

# step-2 : 광고 1
adSection = driver.find_element(By.CSS_SELECTOR, 'section.ad')
driver.execute_script('arguments[0].scrollIntoView()', adSection)

playBtnFirst = driver.find_element(By.CSS_SELECTOR, '.play-button-1')
playBtnFirst.click()
time.sleep(5)

driver.refresh()

time.sleep(1)

# step-3 : 관심 분야 분야별
favBookSection = driver.find_element(By.CSS_SELECTOR, 'section.fav-books')
driver.execute_script('arguments[0].scrollIntoView()', favBookSection)

time.sleep(2)

typeBtns = driver.find_elements(By.XPATH, "//section[@class='fav-books']/div[@class='tab-content']/label")
typeCount = len(typeBtns)
assert typeCount == 5

for typeBtn in typeBtns:
    typeBtn.click()
    time.sleep(1.5)

time.sleep(1)

# step-4 : 오디오북과 밀리뷰어
exampleSection = driver.find_element(By.CSS_SELECTOR, 'section.example')
driver.execute_script('arguments[0].scrollIntoView()', exampleSection)

exampleNumBtns = driver.find_elements(By.CSS_SELECTOR, '#tab-1 ul.click-num li')
exampleNumCount = len(exampleNumBtns)
assert exampleNumCount == 4

for exampleNumBtn in exampleNumBtns:
    exampleNumBtn.click()
    time.sleep(2)

# header가 가려서 자꾸 header가 클릭되는 문제 해결
scroll_y = driver.execute_script('return window.scrollY')
driver.execute_script(f'window.scrollTo(0, {scroll_y - 50})')

millieViewer = driver.find_elements(By.CSS_SELECTOR, '.example-tab .tabs-ul .tab-item')[1]
millieViewer.click()

viewerNumBtns = driver.find_elements(By.CSS_SELECTOR, '#tab-2 ul.click-num li')
viewerNumCount = len(exampleNumBtns)
assert viewerNumCount == 4

for viewerNumBtn in viewerNumBtns:
    viewerNumBtn.click()
    time.sleep(2)

# step-5 : 광고 2 (구독 이야기)
storySection = driver.find_element(By.CSS_SELECTOR, 'section.story')
driver.execute_script('arguments[0].scrollIntoView()', storySection)

playBtnFirst = driver.find_element(By.CSS_SELECTOR, '.play-button-2')
playBtnFirst.click()
time.sleep(5)

driver.refresh()

time.sleep(1)

# step-6 : 자주 묻는 질문
qaSection = driver.find_element(By.CSS_SELECTOR, 'section.qa')
driver.execute_script('arguments[0].scrollIntoView()', qaSection)

qaAccordionItems = driver.find_elements(By.CSS_SELECTOR, 'ul.accordion li.accordion-item')

expected_titTxts = ['안쓰면 정말 환불해 주나요?', '구독 중 해지 할 수 있나요? 수수료는 없나요?', '무료 혜택은 누구나 받을 수 있나요?', '어떤 기기에서 사용할 수 있나요?']

for i in range(4):
    assert qaAccordionItems[i].text == expected_titTxts[i]
    print(qaAccordionItems[i].text)

expected_contents = ['환불해 드리고 있어요.', '수수료 없이', '첫 달 무료 또는 첫 주 무료', '아래 기기와 버전']

for i, qaAccordionItem in enumerate(qaAccordionItems):
    qaAccordionItem.click()
    accordionContent = qaAccordionItem.find_element(By.CSS_SELECTOR, '.accordion-content')

    time.sleep(1)

    assert expected_contents[i] in accordionContent.text

# step-7 : Footer
footer = driver.find_element(By.CSS_SELECTOR, 'footer')
driver.execute_script('arguments[0].scrollIntoView()', footer)

businessInfoTlt = driver.find_element(By.CSS_SELECTOR, '.business-info-title')
businessInfoTlt.click()

assert businessInfoTlt.text == '사업자 정보 닫기'

businessInfoContent = driver.find_element(By.CSS_SELECTOR, '.business-info address.business-info-content').text

assert '호스팅 제공자 : (주) 밀리의 서재' in businessInfoContent

time.sleep(1)

businessInfoTlt.click()

assert businessInfoTlt.text == '사업자 정보 펼쳐보기'