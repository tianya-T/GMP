# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# Author: LiYangYang
# Date: 2020 年
# Description:
#
# -----------------------------------------------------------------------------------


import logging
import sys


class GetLog:
    """
    日志打印
    """

    def __init__(self, log_path):
        self.file_name = log_path  # 全局化
        self.logger = logging.getLogger()  # 返回指定名称的日志文件
        self.logger.setLevel(logging.DEBUG)  # 设置bug等级,默认debug
        # 设置bug打印格式
        fmt = '%(asctime)s-%(filename)s-[%(levelname)s]: %(message)s'
        self.formatter = logging.Formatter(fmt,'%H:%M:%S-')


    def _console(self, level, msg):

        fh = logging.FileHandler(self.file_name, "a", encoding="utf-8")  # 创建FileHandler对象，把日志写入文件
        fh.setLevel(logging.DEBUG)  # 设置日志等级
        fh.setFormatter(self.formatter)  # 设置日志打印模式
        self.logger.addHandler(fh)  # 将内容添加至文件

        # sh = logging.StreamHandler(sys.stdout)  # 创建StreamHandler对象，将日志输出到控制台
        # sh.setLevel(logging.DEBUG)  # 设置日志等级
        # sh.setFormatter(self.formatter)  # 设置日志格式
        # self.logger.addHandler(sh)  # 添加内容

        if level == "info":
            self.logger.info(msg)
        elif level == "debug":
            self.logger.debug(msg)
        elif level == 'warning':
            self.logger.warning(msg)
        elif level == "error":
            self.logger.error(msg)
        # 避免日志重复，每次打印完后，都要清理一遍
        self.logger.removeHandler(fh)
        # self.logger.removeHandler(sh)

        fh.close()  # 关闭文件

    def info(self, msg):
        self._console("info", msg)

    def debug(self, msg):
        self._console("debug", msg)

    def warning(self, msg):
        self._console("warning", msg)

    def error(self, msg):
        self._console("error", msg)


if __name__ == '__main__':
    pass
