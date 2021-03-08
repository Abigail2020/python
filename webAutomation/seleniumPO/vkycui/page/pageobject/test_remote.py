"""
@Time:  2021/3/4
@Author:chenzhe

"""

from selenium import webdriver
from selenium.webdriver.common.by import By

from webAutomation.seleniumPO.vkycui.config.config import driver_path


class TestRemote():
    def setup(self):
        # 创建一个选项options
        opt = webdriver.ChromeOptions()
        # 创建一个远程ip端口9222
        opt.debugger_address = "127.0.0.1:9222"
        # 把选项应用到Chrome浏览器中
        self.driver = webdriver.Chrome(options=opt, executable_path=driver_path)

    def teardown(self):
        self.driver.quit()

    def test_baidu(self):
        # 打开百度首页，选择搜索框，输入111
        self.driver.find_element(By.CSS_SELECTOR, '.switch').click()
