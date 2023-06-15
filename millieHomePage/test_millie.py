import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from millieHomePage.logging import LoggingClass
from millieHomePage.test_step import TestSteps

class TestMillie(LoggingClass):

    def test_millie(self):

        log = self.getLogger()

        # ------------- PC 환경 테스트 -------------

        log.info('PC 환경 테스트를 시작합니다.')

        test_steps = TestSteps(self.driver)

        # step-1 : Millie 로고 클릭 시 상단 이동
        test_steps.test_step_1()

        # step-2 : 광고 1
        test_steps.test_step_2()

        # step-3 : 관심 분야별
        test_steps.test_step_3()

        # step-4 : 오디오북과 밀리뷰어
        test_steps.test_step_4()

        # step-5 : 광고 2 (구독 이야기)
        test_steps.test_step_5()

        # step-6 : 자주 묻는 질문
        test_steps.test_step_6()

        # step-7 : Footer
        test_steps.test_step_7()

        # ------------- Mobile 환경 테스트 -------------

        self.driver.set_window_size(390, 844)
        log.info('아이폰 12 Pro 기준 Mobile 환경 테스트를 시작합니다.')

        # step-8 : 햄버거 버튼
        test_steps.test_step_8()

        # step-9 : 책 드래그 기능
        test_steps.test_step_9()
        
        log.info('모든 자동화 테스트가 끝났습니다.')