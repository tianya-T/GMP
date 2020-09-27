# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# Author: LiYangYang             
# Date: 2020 年
# Description:
#
# -----------------------------------------------------------------------------------

from base_page.base_page import get_driver
from gmp_dms.dms_base_page.dms_base_page import DmsBasePage


class PHBasePage(DmsBasePage):
    """
    流程审批
    """

    def open_my_to_do_items(self):
        """
        打开我的待办
        :return:
        """

        self._switch_to_frame()
        self.driver.sleep(0.5)
        self.driver.click(self.element['流程审批']['我的待办']['我的待办按钮'])

    def open_my_completed_items(self):
        """
        我的已办
        :return:
        """

        self._switch_to_frame()
        self.driver.sleep(0.5)
        self.driver.click(self.element['流程审批']['我的已办']['我的已办按钮'])

    def open_my_closed_items(self):
        """
        我的归档
        :return:
        """

        self._switch_to_frame()
        self.driver.sleep(0.5)
        self.driver.click(self.element['流程审批']['我的归档']['我的归档按钮'])

    def open_my_application(self):
        """
        我的申请
        :return:
        """

        self._switch_to_frame()
        self.driver.sleep(0.5)
        self.driver.click(self.element['流程审批']['我的申请']['我的申请按钮'])

    def open_my_draft_work(self):
        """
        我的草稿
        :return:
        """

        self._switch_to_frame()
        self.driver.sleep(0.5)
        self.driver.click(self.element['流程审批']['我的草稿']['我的草稿按钮'])

    def open_my_print_task(self):
        """
        我的打印
        :return:
        """

        self._switch_to_frame()
        self.driver.sleep(0.5)
        self.driver.click(self.element['流程审批']['我的打印']['我的打印按钮'])


if __name__ == '__main__':
    b = PHBasePage(get_driver())
    b.login()
    b.select_dms_page()
    b.driver.sleep(3)
    b.open_my_to_do_items()
    b.driver.sleep(3)
    b.open_my_completed_items()
    b.driver.sleep(3)
    b.open_my_closed_items()
    b.driver.sleep(3)
    b.open_my_application()
    b.driver.sleep(3)
    b.open_my_draft_work()
    b.driver.sleep(3)
    b.open_my_print_task()
    b.driver.sleep(3)

    b.driver.quit()
