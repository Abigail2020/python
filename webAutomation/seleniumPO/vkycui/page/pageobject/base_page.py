"""
@Time:  2021/3/2
@Author:chenzhe

"""
from datetime import datetime
from time import sleep

import yaml
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver

from webAutomation.seleniumPO.vkycui.common.log import Log
from webAutomation.seleniumPO.vkycui.config.config import driver_path

logger = Log()


def my_print(msg):
    logger.info(msg)


class BasePage:
    _element_content = ""
    _error_count = 0
    _error_max = 10
    _params = {}

    def __init__(self, browser='ff', remote_address=None, driver: WebDriver = None):
        t1 = datetime.now()
        dc = {'platform': 'ANY', 'browserName': 'chrome', 'version': '', 'javascriptEnabled': True}
        if driver == None:
            if remote_address is None:
                if browser == "firefox" or browser == "ff":
                    self.driver = webdriver.Firefox()
                elif browser == "headless chrome" or browser == "headless Chrome" or browser == "headless_chrome" or browser == "headless_Chrome":
                    options = Options()
                    options.add_argument('--headless')
                    options.add_argument('--disable-gpu')
                    self.driver = webdriver.Chrome(executable_path=driver_path, options=options)
                elif browser == "chrome" or browser == "Chrome":
                    options = Options()
                    # 用于浏览器复用
                    # options.debugger_address = "127.0.0.1:9999"
                    options.add_argument("--disable-infobars")
                    options.add_argument("start-maximized")
                    options.add_argument("--disable-extensions")
                    # 1-allow;2-disable 强制打开Chrome浏览器的mic和camera权限，不需要单独点击允许或拒绝
                    options.add_experimental_option("prefs", {
                        "profile.default_content_setting_values.media_stream_mic": 1,
                        "profile.default_content_setting_values.media_stream_camera": 1,
                        "profile.default_content_setting_values.geolocation": 1,
                        "profile.default_content_setting_values.notifications": 1
                    })

                    self.driver = webdriver.Chrome(executable_path=driver_path, options=options)
                elif browser == "internet explorer" or browser == "ie":
                    self.driver = webdriver.Ie()
                elif browser == "opera":
                    self.driver = webdriver.Opera()
                elif browser == "phantomjs":
                    self.driver = webdriver.PhantomJS()
                elif browser == "edge":
                    self.driver = webdriver.Edge()

            else:
                if browser == "RChrome":
                    self.driver = webdriver.Remote(command_executor='http://' + remote_address + '/wd/hub',
                                                   desired_capabilities=dc)
                elif browser == "RIE":
                    dc['browserName'] = 'internet explorer'
                    self.driver = webdriver.Remote(command_executor='http://' + remote_address + '/wd/hub',
                                                   desired_capabilities=dc)
                elif browser == "RFirefox":
                    dc['browserName'] = 'firefox'
                    dc['marionette'] = False
                    self.driver = webdriver.Remote(command_executor='http://' + remote_address + '/wd/hub',
                                                   desired_capabilities=dc)
            try:
                self.driver.implicitly_wait(5)
                my_print(
                    "Success Start a new browser:{0} , Spend {1} seconds".format(browser,
                                                                                 (datetime.now() - t1).seconds))
            except Exception:
                raise NameError("Not found {0} browser,You can enter 'ie','ff',"
                                "'chrome','RChrome','RIe' or 'RFirefox'.".format(browser))

        else:
            self.driver = driver

    def quit_driver(self):
        self.driver.quit()

    def find(self, by, locator=None):
        # 查找并返回这个元素，10次还找不到就抛异常
        try:
            element = self.driver.find_elements(*by) if isinstance(by, tuple) else self.driver.find_element(by, locator)
            self._error_count = 0
            return element

        except Exception as e:
            self._error_count += 1
            if self._error_count >= self._error_max:
                raise e

    def steps(self, path, keyname):
        global element
        with open(path, encoding="utf-8") as file:
            steps: list[dict] = yaml.safe_load(file)
            # print(steps)
            for step in steps:
                try:
                    if step['elementname'] != keyname:
                        continue
                    else:
                        if "by" in step.keys():
                            element = self.find(step['by'], step['locator'])
                            sleep(1)
                        if "action" in step.keys():
                            if "click" == step["action"]:
                                element.click()
                            if "send" == step["action"]:
                                content: str = step["value"]
                                print(step['value'])
                                for param in self._params:
                                    content = content.replace("{%s}" % param, self._params[param])
                                    print(content)
                                element.send_keys(content)
                                sleep(1)
                            if "textContent" == step["action"]:
                                self.element_content = element.text
                                return self.element_content

                except Exception as e:
                    my_print("Can not find this element")
