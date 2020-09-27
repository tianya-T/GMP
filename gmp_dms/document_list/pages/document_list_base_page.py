# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# Author: LiYangYang             
# Date: 2020 年
# Description:
#
# -----------------------------------------------------------------------------------

from base_page.base_page import get_driver
from gmp_dms.dms_base_page.dms_base_page import DmsBasePage


class DLBasePage(DmsBasePage):

    def open_document_to_be_effective(self):
        """
        打开借阅申请页面
        :return:
        """

        self._switch_to_frame()
        self.driver.sleep(0.5)
        self.driver.click(self.element['文件清单']['待生效文件']['待生效文件按钮'])

    def open_effective_document(self):
        """
        打开已生效文件
        :return:
        """

        self._switch_to_frame()
        self.driver.sleep(0.5)
        self.driver.click(self.element['文件清单']['已生效文件']['已生效文件按钮'])

    def open_document_to_be_revised(self):
        """
        打开待修改文件
        :return:
        """

        self._switch_to_frame()
        self.driver.sleep(0.5)
        self.driver.click(self.element['文件清单']['待修改文件']['待修改文件按钮'])

    def open_records_documents(self):
        """
        打开生效记录文件
        :return:
        """

        self._switch_to_frame()
        self.driver.sleep(0.5)
        self.driver.click(self.element['文件清单']['生效记录文件']['生效记录文件按钮'])

    def open_obsoleted_documents(self):
        """
        打开已作废文件
        :return:
        """

        self._switch_to_frame()
        self.driver.sleep(0.5)
        self.driver.click(self.element['文件清单']['已作废文件']['已作废文件按钮'])

    def open_document_in_process(self):
        """
        打开过程中文件
        :return:
        """

        self._switch_to_frame()
        self.driver.sleep(0.5)
        self.driver.click(self.element['文件清单']['过程中文件']['过程中文件按钮'])

    def open_the_old_files(self):
        """
        打开旧版文件
        :return:
        """

        self._switch_to_frame()
        self.driver.sleep(0.5)
        self.driver.click(self.element['文件清单']['旧版文件']['旧版文件按钮'])

    def open_documenets_to_be_invalidated(self):
        """
        打开借阅申请页面
        :return:
        """

        self._switch_to_frame()
        self.driver.sleep(0.5)
        self.driver.click(self.element['文件清单']['待作废文件']['待作废文件按钮'])


if __name__ == '__main__':
    b = DLBasePage(get_driver())
    b.login()
    b.select_dms_page()
    b.select_document_list()
    b.open_document_to_be_effective()
    b.driver.sleep(3)
    b.open_effective_document()
    b.driver.sleep(3)
    b.open_document_to_be_revised()
    b.driver.sleep(3)
    b.open_records_documents()
    b.driver.sleep(3)
    b.open_obsoleted_documents()
    b.driver.sleep(3)
    b.open_document_in_process()
    b.driver.sleep(3)
    b.open_the_old_files()
    b.driver.sleep(3)
    b.open_documenets_to_be_invalidated()
    b.driver.sleep(3)
    b.driver.quit()
