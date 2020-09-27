# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# Author: LiYangYang             
# Date: 2020 年
# Description:
#
# -----------------------------------------------------------------------------------

from base_page.base_page import get_driver
from gmp_dms.dms_base_page.dms_base_page import DmsBasePage


class DWBasePage(DmsBasePage):
    """
    文件回收
    """

    def open_withdrawing_docs(self):
        """
        待回收文件
        :return:
        """

        self._switch_to_frame()
        self.driver.sleep(0.5)
        self.driver.click(self.element['文件回收']['待回收文件']['待回收文件按钮'])

    def open_recovered_docs(self):
        """
        已回收文件
        :return:
        """

        self._switch_to_frame()
        self.driver.sleep(0.5)
        self.driver.click(self.element['文件回收']['已回收文件']['已回收文件按钮'])


if __name__ == '__main__':
    b = DWBasePage(get_driver())
    b.login()
    b.select_dms_page()
    b.select_document_withdrawal()
    b.open_withdrawing_docs()
    b.driver.sleep(3)
    b.open_recovered_docs()
    b.driver.sleep(3)
    b.driver.quit()
