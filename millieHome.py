from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
