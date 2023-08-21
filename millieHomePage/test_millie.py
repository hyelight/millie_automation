import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from millieHomePage.logging import LoggingClass
from millieHomePage.test_step import TestSteps

class TestMilliePC(LoggingClass):

    pc_message_displayed = False

    # PC
    def setup_method(self):
        self.log = self.getLogger()
        self.test_steps = TestSteps(self.driver)

        if not TestMilliePC.pc_message_displayed:
            self.log.info('PC 환경 테스트를 시작합니다.')
            TestMilliePC.pc_message_displayed = True

    def test_step_1(self):
        # step-1 : Millie 로고 클릭 시 상단 이동
        self.test_steps.test_step_1()

    def test_step_2(self):
        # step-2 : 광고 1
        self.test_steps.test_step_2()

    def test_step_3(self):
        # step-3 : 관심 분야별
        self.test_steps.test_step_3()

    def test_step_4(self):
        # step-4 : 오디오북과 밀리뷰어
        self.test_steps.test_step_4()

    def test_step_5(self):
        # step-5 : 광고 2 (구독 이야기)
        self.test_steps.test_step_5()

    def test_step_6(self):
        # step-6 : 자주 묻는 질문
        self.test_steps.test_step_6()

    def test_step_7(self):
        # step-7 : Footer
        self.test_steps.test_step_7()

class TestMillieMobile(LoggingClass):

    mobile_message_displayed = False
    test_method_counter = 0
    TOTAL_TESTS = 2

    # MOBILE
    def setup_method(self):
        self.log = self.getLogger()
        self.driver.set_window_size(390, 844)
        self.test_steps = TestSteps(self.driver)

        if not TestMillieMobile.mobile_message_displayed:
            self.log.info('아이폰 12 Pro 기준 Mobile 환경 테스트를 시작합니다.')
            TestMillieMobile.mobile_message_displayed = True

    def test_step_8(self):           
        # step-8 : 햄버거 버튼
        self.test_steps.test_step_8()

    def test_step_9(self):
        # step-9 : 책 드래그 기능
        self.test_steps.test_step_9()

    def teardown_method(self):
        TestMillieMobile.test_method_counter += 1
        if TestMillieMobile.test_method_counter == TestMillieMobile.TOTAL_TESTS:
            self.log.info('모든 자동화 테스트가 끝났습니다.')
