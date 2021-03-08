"""
@Time:  2021/3/5
@Author:chenzhe

"""
from time import sleep

from webAutomation.seleniumPO.vkycui.page.pageobject.base_page import BasePage
from webAutomation.seleniumPO.vkycui.page.pageobject.inbound_chatting_room_page import InboundChattingRoomPage


class InboundPreparingRoomPage(BasePage):

    def goto_chatting_room(self):
        all_handlers = self.driver.window_handles
        self.driver.switch_to.window(all_handlers[0])
        sleep(20)
        # self.steps("../page/steps/preparing_room", "skip")
        # sleep(3)

        return InboundChattingRoomPage(driver=self.driver)
