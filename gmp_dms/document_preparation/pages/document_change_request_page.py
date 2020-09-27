# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# Author: LiYangYang             
# Date: 2020 年
# Description:
#
# -----------------------------------------------------------------------------------
from base_page.base_page import get_driver
from gmp_dms.document_preparation.pages.document_preparation_base_page import DPBasePage


# TODO ： 封装页面元素
class DocumentChangeRequestPage(DPBasePage):
    """
    文件变更申请页面
    """

    def open_information_popup_window(self):
        """
        打开记录文件信息弹窗，并进入frame框架
        :return:
        """
        self.driver.click('l,新增')
        self.driver.sleep(0.5)
        self.driver.switch_to_parent()
        self.driver.switch_to_frame('xpath,/html/body/div[3]/div[2]/iframe')

    def get_information_popup_window_title(self):
        """
        获取输入框的lable
        :return:
        """

        return self.driver.get_text('xpath,/html/body/div[2]/div[1]/div/li[1]/span/span[1]')

    def document_change_request_input(self, file_name):
        """
        向记录文件信息输入框输入file_name
        :param file_name:
        :return:
        """
        self.driver.send_keys('xpath,/html/body/div[2]/div[1]/div/li[1]/span/span[2]/input[1]', file_name)

    def text(self):
        text = self.driver.get_text('xpath,/html/body/div[2]/div[1]/div/li[1]/div/span')
        return text


if __name__ == '__main__':
    b = DocumentChangeRequestPage(get_driver())
    b.login()

    b.select_dms_page()
    b.select_document_preparation()
    b.open_document_change_request()
    b.driver.sleep(1)
    b.open_information_popup_window()
    b.driver.sleep(1)
    print(b.get_information_popup_window_title())
    b.document_change_request_input("tetst")
    b.driver.sleep(3)
    b.driver.quit()
