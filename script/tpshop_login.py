'''
登录测试
'''
import unittest
import time
import json

from config import BASE_DIR
from page.index_page import IndexProxy
from page.login_page import LoginProxy
from read_data.read_json import build_login_data
from utils import DriverUtil
from parameterized import parameterized


class TestTPShopLogin(unittest.TestCase):
    '''登录测试'''

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = DriverUtil.get_driver()
        cls.index_proxy = IndexProxy()  # 首页
        cls.login_proxy = LoginProxy()  # 登录页面

    @classmethod
    def tearDownClass(cls) -> None:
        DriverUtil.quit_driver()

    def setUp(self) -> None:
        time.sleep(2)
        self.driver.get('http://127.0.0.1')
        self.index_proxy.go_to_login()

    @parameterized.expand(build_login_data)
    def test_login(self, mobile, psw, code, expect, is_success):
        '''登录测试'''
        self.login_proxy.user_login(mobile, psw, code)
        if is_success:
            time.sleep(6)
            title = self.driver.title
            try:
                self.assertIn(expect, title)
            except AssertionError as e:
                self.driver.get_screenshot_as_file(
                    BASE_DIR + '/screenshot/{}.png'.format(time.strftime('%Y%m%d_%H%M%S')))
                raise e


if __name__ == '__main__':
    unittest.main()
