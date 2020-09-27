# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# Author: LiYangYang             
# Date: 2020 年
# Description:
#
# -----------------------------------------------------------------------------------

from base_page.base_page import get_driver
from gmp_dms.dms_base_page.dms_base_page import DmsBasePage


class DSBasePage(DmsBasePage):
    """
    文件签收
    """

    def open_to_be_received_documents(self):
        """
        待签收文件
        :return:
        """

        self._switch_to_frame()
        self.driver.sleep(0.5)
        self.driver.click(self.element['文件签收']['待签收文件']['待签收文件按钮'])

    def open_received_document(self):
        """
        已签收文件
        :return:
        """

        self._switch_to_frame()
        self.driver.sleep(0.5)
        self.driver.click(self.element['文件签收']['已签收文件']['已签收文件按钮'])


if __name__ == '__main__':
    b = DSBasePage(get_driver())
    b.login()
    b.select_dms_page()
    b.select_document_signature()
    b.open_to_be_received_documents()
    b.driver.sleep(3)
    b.open_received_document()
    b.driver.sleep(3)
    b.driver.quit()
