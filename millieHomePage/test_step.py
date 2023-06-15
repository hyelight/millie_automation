import time
from selenium.webdriver.common.by import By
from millieHomePage.logging import LoggingClass
from selenium.webdriver import ActionChains

class TestSteps(LoggingClass):

    def test_step_1(self):
        log = self.getLogger()
        log.info('step-1 : Millie 로고 클릭 시 상단 이동 테스트를 시작합니다.')
        self.driver.execute_script('window.scrollBy(0, document.body.scrollHeight)')
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//img[@src='img/millie-logo.png']").click()
        log.info('MILLIE 로고를 클릭하여 페이지 최상단으로 이동하였습니다.')

        time.sleep(1)

    def test_step_2(self):
        log = self.getLogger()
        log.info('step-2 : 광고 1 테스트를 시작합니다.')
        adSection = self.driver.find_element(By.CSS_SELECTOR, 'section.ad')
        self.driver.execute_script('arguments[0].scrollIntoView()', adSection)

        playBtnFirst = self.driver.find_element(By.CSS_SELECTOR, '.play-button-1')
        playBtnFirst.click()
        log.info('광고 1 영상 재생이 시작되었습니다.')
        time.sleep(5)

        self.driver.refresh()
        log.info('페이지가 새로고침 되었습니다.')

        time.sleep(1)

    def test_step_3(self):
        log = self.getLogger()
        log.info('step-3 : 관심 분야별 테스트를 시작합니다.')
        favBookSection = self.driver.find_element(By.CSS_SELECTOR, 'section.fav-books')
        self.driver.execute_script('arguments[0].scrollIntoView()', favBookSection)
        log.info('관심 분야별 책 섹션으로 이동하였습니다.')

        time.sleep(2)

        typeBtns = self.driver.find_elements(By.XPATH, "//section[@class='fav-books']/div[@class='tab-content']/label")
        typeCount = len(typeBtns)
        assert typeCount == 5, 'typeBtns의 개수가 기존에 예상했던 5개에 맞지 않습니다.'

        for typeBtn in typeBtns:
            typeBtn.click()
            log.info('각각의 typeBtn이 클릭되었습니다.')
            time.sleep(1.5)

        time.sleep(1)

    def test_step_4(self):
        log = self.getLogger()
        log.info('step-4 : 오디오북과 밀리뷰어')
        exampleSection = self.driver.find_element(By.CSS_SELECTOR, 'section.example')
        self.driver.execute_script('arguments[0].scrollIntoView()', exampleSection)
        log.info('오디오북과 밀리뷰어 섹션으로 이동하였습니다.')

        exampleNumBtns = self.driver.find_elements(By.CSS_SELECTOR, '#tab-1 ul.click-num li')
        exampleNumCount = len(exampleNumBtns)
        assert exampleNumCount == 4, '오디오북에서 exampleNumBtns의 개수가 기존에 예상했던 4개에 맞지 않습니다.'

        for exampleNumBtn in exampleNumBtns:
            exampleNumBtn.click()
            log.info('exampleNumBtn이 클릭되었습니다.')
            time.sleep(2)

        # header가 가려서 자꾸 header가 클릭되는 문제 해결
        scroll_y = self.driver.execute_script('return window.scrollY')
        self.driver.execute_script(f'window.scrollTo(0, {scroll_y - 50})')
        log.info('현재 기준 scroll_y를 50 만큼 상단으로 이동하였습니다.')

        millieViewer = self.driver.find_elements(By.CSS_SELECTOR, '.example-tab .tabs-ul .tab-item')[1]
        millieViewer.click()

        viewerNumBtns = self.driver.find_elements(By.CSS_SELECTOR, '#tab-2 ul.click-num li')
        viewerNumCount = len(exampleNumBtns)
        assert viewerNumCount == 4, '밀리뷰어에서 exampleNumBtns의 개수가 기존에 예상했던 4개에 맞지 않습니다.'

        for viewerNumBtn in viewerNumBtns:
            viewerNumBtn.click()
            log.info('viewerNumBtn이 클릭되었습니다.')
            time.sleep(2)

    def test_step_5(self):
        log = self.getLogger()
        log.info('step-5 : 광고 2 (구독 이야기) 테스트를 시작합니다.')
        storySection = self.driver.find_element(By.CSS_SELECTOR, 'section.story')
        self.driver.execute_script('arguments[0].scrollIntoView()', storySection)
        log.info('광고 2 (구독 이야기) 섹션으로 이동하였습니다.')

        playBtnFirst = self.driver.find_element(By.CSS_SELECTOR, '.play-button-2')
        playBtnFirst.click()
        log.info('광고 2 영상 재생이 시작되었습니다.')
        time.sleep(5)

        self.driver.refresh()
        log.info('페이지가 새로고침 되었습니다.')

        time.sleep(1)

    def test_step_6(self):
        log = self.getLogger()
        log.info('step-6 : 자주 묻는 질문 테스트를 시작합니다.')
        qaSection = self.driver.find_element(By.CSS_SELECTOR, 'section.qa')
        self.driver.execute_script('arguments[0].scrollIntoView()', qaSection)
        log.info('자주 묻는 질문 섹션으로 이동하였습니다.')

        qaAccordionItems = self.driver.find_elements(By.CSS_SELECTOR, 'ul.accordion li.accordion-item')

        expected_titTxts = ['안쓰면 정말 환불해 주나요?', '구독 중 해지 할 수 있나요? 수수료는 없나요?', '무료 혜택은 누구나 받을 수 있나요?', '어떤 기기에서 사용할 수 있나요?']

        for i in range(4):
            assert qaAccordionItems[i].text == expected_titTxts[i], 'qaAccordionItems.text와 expected_titTxts가 일치하지 않습니다.'

        expected_contents = ['환불해 드리고 있어요.', '수수료 없이', '첫 달 무료 또는 첫 주 무료', '아래 기기와 버전']

        for i, qaAccordionItem in enumerate(qaAccordionItems):
            qaAccordionItem.click()
            log.info('qaAccordionItem을 클릭하였습니다.')
            accordionContent = qaAccordionItem.find_element(By.CSS_SELECTOR, '.accordion-content')

            time.sleep(1)

            assert expected_contents[i] in accordionContent.text, 'expected_contents와 accordionContent.text가 일치하지 않습니다.'

    def test_step_7(self):
        log = self.getLogger()
        log.info('step-7 : Footer 테스트를 시작합니다.')
        footer = self.driver.find_element(By.CSS_SELECTOR, 'footer')
        self.driver.execute_script('arguments[0].scrollIntoView()', footer)
        log.info('Footer 섹션으로 이동하였습니다.')

        businessInfoTit = self.driver.find_element(By.CSS_SELECTOR, '.business-info-title')
        businessInfoTit.click()
        log.info('Footer의 businessInfoTit을 클릭하였습니다.')

        assert businessInfoTit.text == '사업자 정보 닫기', 'businessInfoTit 텍스트가 사업자 정보 닫기가 아닙니다.'

        businessInfoContent = self.driver.find_element(By.CSS_SELECTOR, '.business-info address.business-info-content').text

        assert '호스팅 제공자 : (주) 밀리의 서재' in businessInfoContent, 'businessInfoContent에 들어있는 내용이 아닙니다.'

        time.sleep(1)

        businessInfoTit.click()
        log.info('Footer의 businessInfoTit을 클릭하였습니다.')

        assert businessInfoTit.text == '사업자 정보 펼쳐보기', 'businessInfoTit 텍스트가 사업자 정보 펼쳐보기가 아닙니다.'


    def test_step_8(self):
        log = self.getLogger()
        log.info('step-8 : 햄버거 버튼 테스트를 시작합니다.')
        hamburgerBtn = self.driver.find_element(By.CSS_SELECTOR, '.hamburger-menu')
        hamburgerBtn.click()
        log.info('햄버거 버튼 메뉴를 클릭하였습니다.')

        time.sleep(1.5)

        navLists = self.driver.find_elements(By.CSS_SELECTOR, 'nav ul li')

        expectedMenuLists = ['기업문의', '회사소개', '계정관리', '고객센터']

        for i in range(len(expectedMenuLists)):
            assert navLists[i].text == expectedMenuLists[i], 'navLists.text가 expectedMenuLists와 일치하지 않습니다.'

        hamburgerBtn.click()
        log.info('햄버거 버튼을 클릭하였습니다.')

        time.sleep(1)

    def test_step_9(self):
        log = self.getLogger()
        log.info('step-9 : 책 드래그 기능 테스트를 시작합니다.')
        favBookSection = self.driver.find_element(By.CSS_SELECTOR, 'section.fav-books')
        self.driver.execute_script('arguments[0].scrollIntoView()', favBookSection)
        log.info('책 드래그 기능 섹션으로 이동하였습니다.')

        action = ActionChains(self.driver)

        typeBtns = self.driver.find_elements(By.XPATH, "//section[@class='fav-books']/div[@class='tab-content']/label")

        startElements = self.driver.find_elements(By.CSS_SELECTOR, '.fav-books .book-list-wrapper')

        for i in range(len(typeBtns)):
            typeBtns[i].click()
            log.info('typeBtn이 클릭되었습니다.')
            action.move_to_element(startElements[i]).click_and_hold().move_by_offset(-200, 0).release().perform()
            time.sleep(1)
