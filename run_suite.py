import unittest
import time
from base import  *
from script.tpshop_cart import TestTPShopCart
from script.tpshop_login import TestTPShopLogin
from script.tpshop_palce_order import TestTPShopPlaceOrder
from tools.HTMLTestRunnerCN import HTMLTestReportCN

from utils import DriverUtil

suite = unittest.TestSuite()

suite.addTest(unittest.makeSuite(TestTPShopLogin))
# suite.addTest(TestTPShopLogin('test_login'))  # 参数化不能单个调用方法名
suite.addTest(unittest.makeSuite(TestTPShopCart))
suite.addTest(unittest.makeSuite(TestTPShopPlaceOrder))

DriverUtil.change_quit_status(False)

# unittest.TextTestRunner().run(suite)
report_name = BASE_DIR + '/report/test_report{}.html'.format(time.strftime('%Y%m%d_%H%M%S'))
with open(report_name,'wb') as f:
    runner = HTMLTestReportCN(stream=f,
                              verbosity=2,
                              title='web自动化测试',
                              description='python,火狐浏览器，window',
                              tester='QAhyc')
    runner.run(suite)

DriverUtil().change_quit_status(True)
