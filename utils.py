'''
公共方法类
'''
from selenium import webdriver


def driver_to_new_handle_func():
    '''driver切换到新开的页面'''
    driver = DriverUtil.get_driver()

    handles = driver.window_handles
    driver.switch_to.window(handles[-1])


def get_text_element_func(text):
    '''根据文本内容获取文本信息'''
    xpath = "// *[contains(text(), '{}')]".format(text)
    try:
        element = DriverUtil.get_driver().find_element_by_xpath(xpath)
        return element
    except:
        return False


def get_tip_message():
    """获取弹窗信息方法"""
    msg = DriverUtil.get_driver().find_element_by_class_name('layui-layer-content').text
    print('msg:', msg)
    return msg


class DriverUtil(object):
    """浏览器驱动对象工具类"""

    driver = None  # 驱动对象初始化状态、
    status = True  # 浏览器对象退出方法附加条件

    @classmethod
    def get_driver(cls):
        """获取驱动对象方法"""
        # 判断浏览器对象不存在时再进行创建操作
        if cls.driver is None:
            cls.driver = webdriver.Chrome()
            # 由于判断条件下的代码只会执行一次, 因此将打开和最大化和隐式等待的设置暂时放置到这里
            cls.driver.get('http://127.0.0.1')
            cls.driver.maximize_window()
            cls.driver.implicitly_wait(10)
        return cls.driver

    @classmethod
    def quit_driver(cls):
        """
        退出驱动对象方法,
        :return:
        """
        if cls.driver and cls.status:
            cls.driver.quit()
            cls.driver = None

    @classmethod
    def change_quit_status(cls, type):
        '''
        改变status属性，设置关闭浏览器的开关
        :param type: True执行退出 Flose不执行退出
        :return:
        '''
        cls.status = type


if __name__ == '__main__':
    DriverUtil.get_driver()
    DriverUtil.quit_driver()
