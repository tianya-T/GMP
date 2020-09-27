# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# Author: LiYangYang
# Date: 2020 年
# Description:
# -----------------------------------------------------------------------------------

import time
import unittest
from tomorrow import threads
from common.beautiful_report import TestRunner
from common.create_dir import CreateDir
from common.get_case_list import GetCaseList
from common.get_data import GetIniData


class Runner:
    def __init__(self):
        self.ini_data = GetIniData()
        self.title = self.ini_data.get_ini_data("Report", "title")
        self.tester = self.ini_data.get_ini_data("Report", "tester")
        self.desc = self.ini_data.get_ini_data("Report", "description")
        self.templates = int(self.ini_data.get_ini_data("Report", "templates"))
        self.p_time = self.title + time.strftime('%H-%M-%S') + ".html"  # 获取当前的时分秒命名

    def runner(self):
        """
        用于运行测试整测试用例。
        :return:
        """

        case_list = GetCaseList().get_case_list()  # 获取含有测试用例的列表
        suite = unittest.TestSuite()
        suite.addTests(unittest.TestLoader().loadTestsFromNames(case_list))  # 加载测试用例
        parent_path = CreateDir().create_reports_dir()  # 已运行当天日期为名创建文件夹，若存在则不再创建

        test_renner = TestRunner(suite=suite,
                                 filename=self.p_time,
                                 report_dir=parent_path,
                                 title=self.title,
                                 tester=self.tester,
                                 desc=self.desc,
                                 templates=self.templates
                                 )
        test_renner.run()



if __name__ == '__main__':
    Runner().runner()
