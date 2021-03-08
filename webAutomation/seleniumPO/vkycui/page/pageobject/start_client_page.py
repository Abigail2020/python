"""
@Time:  2021/3/5
@Author:chenzhe

"""
from webAutomation.seleniumPO.vkycui.page.pageobject.base_page import BasePage
from webAutomation.seleniumPO.vkycui.page.pageobject.inbound_preparing_room_page import InboundPreparingRoomPage


class StartClientPage(BasePage):

    def goto_agent_preparing_room(self):
        # 打开新tab
        js = 'window.open("https://vkyc-staging-id.advai.net/client/demo/transactionID");'
        self.driver.execute_script(js)
        # 获取窗口句柄信息
        print(self.driver.current_window_handle)
        print(self.driver.window_handles)
        handlers = self.driver.window_handles
        # 切换到当前窗口句柄
        self.driver.switch_to.window(handlers[1])
        # 点击开始，client端开始请求
        self.steps("../page/steps/start_client", "start")
        return InboundPreparingRoomPage(driver=self.driver)
