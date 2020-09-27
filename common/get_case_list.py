# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# Author: LiYangYang
# Date: 2020 年
# Description:
# 此模块用于将ini文件的所有值存到list中并返回，该list列表可用于unittest.TestLoader().loadTestsFromNames(list)
# -----------------------------------------------------------------------------------

from common.get_data import GetIniData, ExcelDataAlone, GetJsonData
from common.get_path import GetPath


class GetCaseList:

    def __init__(self):
        self.__get_ini = GetIniData()  # 实例化GetIniData
        __json_path = GetPath().get_path(GetIniData().get_ini_data("Path", "caseDataJson"))  # 返回json文件位置
        self.json_data = GetJsonData().get_json_data(__json_path)  # 获取json数据
        self._excel_file = GetPath().get_path(GetIniData().get_ini_data("Excel", "excelPath"))  # 获取Excel地址
        self._excel_sheet_name = GetIniData().get_ini_data("Excel", "sheetName")  # 获取ini文件中sheet页名字

    def get_case_list(self):
        """
        以列表形式返回caseconfig.ini文件中的数据。用于加载测试套
        :return:
        """
        excel_data = ExcelDataAlone(self._excel_file, self._excel_sheet_name)
        full_data = []
        for i in range(2, excel_data.get_max_row() + 1):
            product = excel_data.get_cell_data("A", i)
            module = excel_data.get_cell_data("B", i)
            case_class = excel_data.get_cell_data("C", i)
            if product is None or module is None or case_class is None:
                continue  # 获取的数据有空值跳过本次循环
            else:
                case_data = self.json_data[product][module][case_class]
                full_data.append(case_data)
        return full_data


if __name__ == '__main__':
    print(GetCaseList().get_case_list())
