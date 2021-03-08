"""
@Time:  2021/3/5
@Author:chenzhe

"""
from webAutomation.seleniumPO.vkycui.page.pageobject.base_page import BasePage


class InboundChattingRoomPage(BasePage):
    step_path = "../page/steps/inbound_chatting_room"

    # 获取checklist
    def get_checklist_text(self):
        # 第一条内容
        self.steps(self.step_path, "first")
        first_content = self.element_content
        # 第二条内容
        self.steps(self.step_path, "second")
        second_content = self.element_content
        # 第三条内容
        self.steps(self.step_path, "third")
        third_content = self.element_content
        # 第四条内容
        self.steps(self.step_path, "fourth")
        fourth_content = self.element_content
        # 第五条内容
        self.steps(self.step_path, "fifth")
        fifth_content = self.element_content
        # 第六条内容
        self.steps(self.step_path, "sixth")
        sixth_content = self.element_content
        return first_content, second_content, third_content, fourth_content, fifth_content, sixth_content

    # 获取submitInfo
    def get_submit_info_text(self):
        pass

    # 点击拍照按钮
    def click_take_photo_button(self):
        pass

    # 点击submit
    def click_submit(self):
        pass

    # 点击cancel
    def click_cancel(self):
        pass
