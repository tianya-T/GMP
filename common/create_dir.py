# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# Author: LiYangYang            # Date: 2020 年
# Description:
# 该模块一般用于自动创建保存测试结果的文件夹。
# -----------------------------------------------------------------------------------
import os
from datetime import datetime

from common.get_path import GetPath


class CreateDir:

    def __get_full_path(self):
        """
        在results文件夹下，创建一个以年月日命名的文件夹。
        :return: 返回文件夹创建后的全路径
        """
        now_time = datetime.now().strftime("%Y-%m-%d")
        path = "AutoTesting\\results\\"
        result_path = GetPath().get_path(path)
        full_path = os.path.join(result_path, now_time)

        try:
            if os.path.isdir(full_path):
                return full_path
            else:
                os.mkdir(full_path)
                return full_path

        except FileNotFoundError:
            os.mkdir(result_path)
            os.mkdir(full_path)
            return full_path

    def __mk_moduel_name(self, moduel_name):
        super_path = self.__get_full_path()
        moduel_path = moduel_name
        full_path = os.path.join(super_path, moduel_path)

        try:
            if os.path.isdir(full_path):
                return full_path
            else:
                os.mkdir(full_path)
                return full_path

        except FileNotFoundError:
            os.mkdir(super_path)
            os.mkdir(full_path)
            return full_path

    def create_images_dir(self, moduel_name, img_name):
        """
        在\results\*\目录下创建images文件夹，用于存放测试用例执行过程中的截图。
        :return: 返回全路径
        """
        super_path = self.__mk_moduel_name(moduel_name)
        images_path = os.path.join(super_path, "images")
        creat_time = datetime.now().strftime("%H-%M-%S")
        if os.path.isdir(images_path):
            file_path = "{}{}.png".format(img_name, creat_time)

            return os.path.join(images_path, file_path)
        else:
            os.mkdir(images_path)
            file_path = "{}{}.png".format(img_name, creat_time)
            path = os.path.join(images_path, file_path)
            return path

    def create_logs_file(self, moduel_name):
        """
        在\results\*\目录下创建logs文件夹，并生成一个日志文件。
        :return: 返回创建文件夹后的全路径
        """

        file_name_time = datetime.now().strftime('%m{}%d{}%H{}').format('月', '日', '时')
        tt = datetime.now().strftime('%H{}%M{}%S').format('时', '分', '秒')

        log_name = '{}.log'.format(file_name_time)
        super_path = self.__mk_moduel_name(moduel_name)
        logs_path = os.path.join(super_path, "logs")
        if os.path.isdir(logs_path):
            pass
        else:
            os.mkdir(logs_path)

        file_path = os.path.join(logs_path, log_name)
        with open(file_path, mode='a', encoding='utf8') as fp:
            fp.write('\n\n----------------------------日志打印时间 {}:----------------------------\n\n'.format(tt))

        return file_path

    def create_reports_dir(self):
        """
        在\results\*\目录下创建repotrs文件夹，用于存放测试用例执行后的测试报告。
        :return: 返回创建文件夹后的全路径
        """
        super_path = self.__get_full_path()
        reports_path = os.path.join(super_path, "reports")
        if os.path.isdir(reports_path):
            return reports_path
        else:
            os.mkdir(reports_path)
            return reports_path

    def path_join(self, parent_path, file_name):
        return os.path.join(parent_path, file_name)


if __name__ == '__main__':
    print(CreateDir().create_images_dir("hello", "hello"))
