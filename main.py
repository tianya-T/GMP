# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# Author: LiYangYang
# Date: 2020 年
# Description:
# 脚本启动入口，命令行调用此模块即可。
# -----------------------------------------------------------------------------------


from runner.runner import Runner


class Main:
    # 执行
    def start_testing(self):
        run = Runner()
        run.runner()


if __name__ == '__main__':
    Main().start_testing()
