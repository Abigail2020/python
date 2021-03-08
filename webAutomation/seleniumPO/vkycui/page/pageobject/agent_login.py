"""
@Time:  2021/3/3
@Author:chenzhe

"""
from webAutomation.seleniumPO.vkycui.page.pageobject.base_page import BasePage
from webAutomation.seleniumPO.vkycui.page.pageobject.inbound_waiting_room_page import InboundWaitingRoomPage


class AgentLogin(BasePage):

    def __init__(self):
        super().__init__(browser="chrome")
        self.driver.get("https://****/agent/***")

    def goto_inbound_waiting_room(self, username, password, captcha):
        # 点击role并选择
        self.steps("../page/steps/agent_login.yaml", "role")
        self.steps("../page/steps/agent_login.yaml", "select")
        # 输入username
        self._params['value'] = username
        self.steps("../page/steps/agent_login.yaml", "username")
        # 输入password
        self._params['value'] = password
        self.steps("../page/steps/agent_login.yaml", "password")
        # 输入captcha
        self._params['value'] = captcha
        self.steps("../page/steps/agent_login.yaml", "captcha")

        return InboundWaitingRoomPage(driver=self.driver)
