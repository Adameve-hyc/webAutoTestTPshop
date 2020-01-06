from selenium.webdriver.common.by import By

# 首页页面
login_link = By.LINK_TEXT, '登录'  # 登录按钮
search_bar = By.ID, 'q'  # 商品搜索框
search_button = By.CLASS_NAME, 'ecsc-search-button'  # 搜索按钮
my_order_link = By.LINK_TEXT, '我的订单'  # 我的订单
my_cart = By.CLASS_NAME, 'share-shopcar-index'  # 我的购物车

# 登录页面
user_mobile = By.ID, 'username'  # 手机号
psw = By.ID, 'password'  # 密码
code = By.ID, 'verify_code'  # 验证码
login = By.CLASS_NAME, 'J-login-submit'  # 登录按钮
