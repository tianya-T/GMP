# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# Author: LiYangYang             
# Date: 2020 年
# Description:
#
# -----------------------------------------------------------------------------------

from base_page.base_page import get_driver
from gmp_dms.dms_base_page.dms_base_page import DmsBasePage


class DPBasePage(DmsBasePage):

    def open_document_change_request(self):
        """
        打开文件变更申请
        :return:
        """
        self._switch_to_frame()
        self.driver.sleep(0.5)
        self.driver.click(self.element['新增修订']['文件变更申请']['文件变更申请按钮'])  # 点击文件变更申请，打开页面

    def open_document_addition(self):
        """
        打开文件新增
        :return:
        """
        self._switch_to_frame()
        self.driver.sleep(0.5)
        self.driver.click(self.element['新增修订']['文件新增']['文件新增按钮'])  # 点击文件变更申请，打开页面

    def open_document_revision(self):
        """
        打开文件修订
        :return:
        """

        self._switch_to_frame()
        self.driver.sleep(0.5)
        self.driver.click(self.element['新增修订']['文件修订']['文件修订按钮'])


if __name__ == '__main__':
    b = DPBasePage(get_driver())
    b.login()
    b.select_dms_page()
    b.select_document_preparation()
    b.open_document_change_request()
    b.driver.sleep(2)
    b.open_document_addition()
    b.driver.sleep(2)
    b.open_document_revision()
    b.driver.sleep(5)
    b.driver.quit()
