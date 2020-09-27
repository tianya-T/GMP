# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# Author: LiYangYang             
# Date: 2020 年
# Description:
#
# -----------------------------------------------------------------------------------
from base_page.base_page import get_driver
from gmp_dms.dms_base_page.dms_base_page import DmsBasePage


class SRBasePage(DmsBasePage):
    """
    系统报表
    """

    def open_document_number_list(self):
        """
        文件编号清单
        :return:
        """

        self._switch_to_frame()
        self.driver.sleep(0.5)
        self.driver.click(self.element['系统报表']['文件编号清单']['文件编号清单按钮'])

    def open_document_borrowed_records(self):
        """
        借阅记录清单
        :return:
        """

        self._switch_to_frame()
        self.driver.sleep(0.5)
        self.driver.click(self.element['系统报表']['借阅记录清单']['借阅记录清单按钮'])

    def open_audit_information_check(self):
        """
        审计信息查询
        :return:
        """

        self._switch_to_frame()
        self.driver.sleep(0.5)
        self.driver.click(self.element['系统报表']['审计信息查询']['审计信息查询按钮'])

    def open_department_paper_document(self):
        """
        部门纸质文件
        :return:
        """

        self._switch_to_frame()
        self.driver.sleep(0.5)
        self.driver.click(self.element['系统报表']['部门纸质文件']['部门纸质文件按钮'])


if __name__ == '__main__':
    b = SRBasePage(get_driver())
    b.login()
    b.select_dms_page()
    b.select_system_report()
    b.open_document_number_list()
    b.driver.sleep(3)
    b.open_document_borrowed_records()
    b.driver.sleep(3)
    b.open_audit_information_check()
    b.driver.sleep(3)
    b.open_department_paper_document()
    b.driver.sleep(3)

    b.driver.quit()
