# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# Author: LiYangYang             
# Date: 2020 年
# Description:
#
# -----------------------------------------------------------------------------------

from base_page.base_page import get_driver
from gmp_dms.dms_base_page.dms_base_page import DmsBasePage


class BBasePage(DmsBasePage):
    """
    借阅续借的基础类
    """

    def open_borrowing_apply(self):
        """
        打开借阅申请页面
        :return:
        """

        self._switch_to_frame()
        self.driver.sleep(0.5)
        self.driver.click(self.element['借阅续借']['借阅申请']['借阅申请按钮'])

    def open_my_borrowing(self):
        """
        打开我的借阅页面
        :return:
        """

        self._switch_to_frame()
        self.driver.sleep(0.5)
        self.driver.click(self.element['借阅续借']['我的借阅']['我的借阅按钮'])


if __name__ == '__main__':
    b = BBasePage(get_driver())
    b.login()
    b.select_dms_page()
    b.select_borrowing()
    b.open_my_borrowing()
    b.driver.sleep(3)
    b.open_borrowing_apply()
    b.driver.sleep(3)
    b.driver.quit()
