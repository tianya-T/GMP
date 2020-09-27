# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# Author: LiYangYang             
# Date: 2020 年
# Description:
#
# -----------------------------------------------------------------------------------

from base_page.base_page import get_driver
from gmp_dms.dms_base_page.dms_base_page import DmsBasePage


class DRBasePage(DmsBasePage):
    """
    文件复审
    """

    def open_document_to_be_routine_reviewed(self):
        """
        待复审文件
        :return:
        """

        self._switch_to_frame()
        self.driver.sleep(0.5)
        self.driver.click(self.element['文件复审']['待复审文件']['待复审文件按钮'])

    def open_expired_documents(self):
        """
        已过期文件
        :return:
        """

        self._switch_to_frame()
        self.driver.sleep(0.5)
        self.driver.click(self.element['文件复审']['已过期文件']['已过期文件按钮'])


if __name__ == '__main__':
    b = DRBasePage(get_driver())
    b.login()
    b.select_dms_page()
    b.select_document_review()
    b.driver.sleep(3)
    b.open_document_to_be_routine_reviewed()
    b.driver.sleep(3)
    b.open_expired_documents()
    b.driver.sleep(3)
    b.driver.quit()
