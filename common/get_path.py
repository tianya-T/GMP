# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# Author: LiYangYang            # Date: 2020 年
# Description:
# -----------------------------------------------------------------------------------

import os


class GetPath:

    def get_path(self, pro_path):
        """
        获取路径
        :param pro_path:
        :return:
        """
        pro_name = pro_path.split('\\')[0]  # 取项目名称
        file_path = os.path.dirname(__file__).split(pro_name)  # 通过项目名称分割当前文件目录
        win_path = file_path[0]  # 取项目名称之前的整个目录
        all_path = str(win_path) + pro_path  # 拼接最终的项目名字
        return all_path


if __name__ == '__main__':
    path = GetPath().get_path("gmp\\config.ini")
    print(path)
