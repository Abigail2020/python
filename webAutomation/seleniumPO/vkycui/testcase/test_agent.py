"""
@Time:  2021/3/3
@Author:chenzhe

"""
from webAutomation.seleniumPO.vkycui.page.pageobject.agent_login import AgentLogin
from webAutomation.seleniumPO.vkycui.page.pageobject.inbound_waiting_room_page import InboundWaitingRoomPage


class TestAgentLogin:
    def setup(self):
        self.login = AgentLogin()

    def teardown(self):
        self.login.quit_driver()

    def test_chatting_room_function(self):
        # 在agent登陆窗口，输入用户名密码等信息
        input_login: InboundWaitingRoomPage = \
            self.login.goto_inbound_waiting_room("vkyc", "***", "1111")
        # 进入waiting-room页面，点击resume成为available状态
        switch_to_available = input_login.goto_preparing_room()
        # 打开新tab，输入client demo url，开始排队
        start_client_page = switch_to_available.goto_agent_preparing_room()
        # 切换tab到agent，直到进入到chatting-room
        preparing_room = start_client_page.goto_chatting_room()
        # 在chatting-room检查checklist文案
        checklist_text = preparing_room.get_checklist_text()
        print(checklist_text)
        assert checklist_text[0] == "Client's face in video call is consistent with the photo submitted"
        assert checklist_text[1] == "Full Name is consistent"
        assert checklist_text[2] == "ID number is consistent"
        assert checklist_text[3] == "Birthday is consistent"
        assert checklist_text[4] == "Place of birth is consistent"
        assert checklist_text[5] == "Mother maiden name is consistent"
        # 在chatting-room点击拍照按钮，检查take photo按钮是否可用
        # 在chatting-room点击submit，检查submit按钮是否可用
