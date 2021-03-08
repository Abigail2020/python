"""
@Time:  2021/3/4
@Author:chenzhe

"""
from time import sleep

from webAutomation.seleniumPO.vkycui.page.pageobject.base_page import BasePage
from webAutomation.seleniumPO.vkycui.page.pageobject.start_client_page import StartClientPage


class InboundWaitingRoomPage(BasePage):
    # 点击"RESUME"按钮
    def goto_preparing_room(self):
        sleep(3)
        # 点击resume
        self.steps("../page/steps/inbound_waiting_room", "resume")
        return StartClientPage(driver=self.driver)
