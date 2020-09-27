# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# Author: LiYangYang            # Date: 2020 年
# Description:
# 此模块为该项目基础操作的封装，请在测试套运行前执行login()方法，确保能正确打开浏览器。
# 通过继承可获得已封装webdriver的一些方法，具体方法请查看GmpAutoTesting\common\BaseDriver模块。
# 若非必要，无需修改此模块代码
# -----------------------------------------------------------------------------------

from common.base_driver import BaseDriver, BoxDriver
from common.get_data import GetYamlData, GetIniData
from common.get_path import GetPath


class BasePage(BaseDriver):
    __USERNAME = GetIniData().get_ini_data("UserName", "username")
    __PASSWORD = GetIniData().get_ini_data("PassWord", "password")

    def __get_dms_element(self):

        yaml_path = GetPath().get_path(r'AutoTesting\base_page\element.yaml')  # 获取element路径
        dms_base_element = GetYamlData().get_yaml_data(yaml_path)  # 获取element.yaml中的数据，返回字典。
        return dms_base_element

    def switch_to_main_frame(self):
        """
        进入RMS的主框架
        :return:
        """
        self.driver.switch_to_default()
        self.driver.switch_to_frame(self.__get_dms_element()["主框架"])

    def login(self, username=__USERNAME, passwd=__PASSWORD):
        """
        登录方法。
        :param username:
        :param passwd:
        :return:
        """
        self.driver.maximize_window()  # 最大化窗口
        self.driver.send_keys(self.__get_dms_element()["USERNAME_TEXT"], username)
        self.driver.send_keys(self.__get_dms_element()["PASSWD_TEXT"], passwd)
        self.driver.click(self.__get_dms_element()["LOGIN_BUTTON"])

    def logout(self):
        self.driver.switch_to_default()
        self.driver.click('xpath,/html/body/div[2]/div/div/div[2]/ul/li[5]/a')

    def select_doc_page(self):
        """
        admin用户使用方法，切换至文档模块
        :return:
        """
        self.driver.click(self.__get_dms_element()["DOC"])

    def select_my_page(self):
        """
        切换至我的工作站模块
        :return:
        """
        self.driver.click(self.__get_dms_element()["MY_"])

    def select_new_work_flow_page(self):
        """
        切换至工作流模块
        :return:
        """
        self.driver.click(self.__get_dms_element()["NEWWORKFLOW"])

    def select_admin_page(self):
        """
        admin用户使用方法，切换系统管理模块
        :return:
        """
        self.driver.click(self.__get_dms_element()["ADMIN_"])

    def select_dms_page(self):
        """
        切换至文件管理模块
        :return:
        """
        self.driver.click(self.__get_dms_element()["DMS"])

    def select_rms_page(self):
        """
        切换至记录管理模块
        :return:
        """
        self.driver.click(self.__get_dms_element()["RMS"])

    def select_tms_page(self):
        """
        切换至培训管理模块
        :return:
        """
        self.driver.click(self.__get_dms_element()["TMS"])

    def select_ams_page(self):
        """
        切换至档案管理模块
        :return:
        """
        self.driver.click(self.__get_dms_element()["AMS"])

    def _switch_to_signature(self):
        """
        进入电子签名所在的子框架
        :return:
        """

        self.driver.switch_to_default()
        self.driver.switch_to_frame(self.__get_dms_element()["电子签名"]['电子签名框架'])

    def get_signature_informathon(self):
        """
        获取电子签名窗口的信息，包括实例号，姓名，用户名，电子签名含义。返回列表。
        :return:
        """
        self._switch_to_signature()
        instance_variable = self.driver.get_text(self.__get_dms_element()["电子签名"]['实例号'])
        user_name = self.driver.get_text(self.__get_dms_element()["电子签名"]['姓名'])
        account = self.driver.get_attribute_text(self.__get_dms_element()["电子签名"]['用户名'], "value")
        signature_implication = self.driver.get_text(self.__get_dms_element()["电子签名"]['签名含义'])
        info_list = [instance_variable, user_name, account, signature_implication]
        return info_list

    def send_passwd(self, passwd=__PASSWORD):
        """
        向电子签名窗口发送密码
        :param passwd: 默认是登录密码
        :return:
        """
        self._switch_to_signature()
        self.driver.send_keys(self.__get_dms_element()["电子签名"]['密码框'], passwd)

    def click_confirm(self):
        """
        电子签名窗口点击确认
        :return:
        """
        self._switch_to_signature()
        self.driver.click(self.__get_dms_element()["电子签名"]['确认按钮'])

    def get_window_prompts_text(self):
        """
        获取密码错误时的弹窗内容
        :return:
        """
        self.switch_to_main_frame()
        self.driver.sleep(1)
        return self.driver.get_text(self.__get_dms_element()["电子签名"]['密码错误提示弹窗'])

    def click_deselect(self):
        """
        电子签名窗口点击取消
        :return:
        """
        self._switch_to_signature()
        self.driver.click(self.__get_dms_element()["电子签名"]['取消按钮'])

    def click_verify_confirm(self):
        """
        输入正确签名后弹出的提示框，点击确认
        :return:
        """
        self.switch_to_main_frame()
        self.driver.old_switch_to_frame(self.__get_dms_element()["确定弹窗"]['确定弹窗框架'])

        self.driver.mouse_double_click(self.__get_dms_element()["确定弹窗"]['确定'])

    def click_verify_deselect(self):
        """
        输入正确签名后弹出的提示框，点击取消
        :return:
        """
        self.switch_to_main_frame()
        self.driver.switch_to_frame(self.__get_dms_element()["确定弹窗"]['确定弹窗框架'])
        self.driver.click(self.__get_dms_element()["确定弹窗"]['取消'])

    def send_time(self, selector, time: str):
        """
        将时间框的readonly移除，输入时间。
        :param selector:
        :param time: 传入时间的格式2020-9-15,10:57:31或者2020-9-15
        :return:
        """
        # js脚本代码：移除readonly属性
        js = 'arguments[0].removeAttribute("readonly");'
        try:
            year_to_date = time.split(',')[0].replace(' ', '')
            hhmmss = time.split(',')[1].replace(' ', '')
            time_text = year_to_date + ' ' + hhmmss
            # 对元素执行js代码
            self.driver.execute_js_script(js, selector)
            # 将时间输入到文本框中
            self.driver.send_keys(selector, time_text)
            self.driver.click(selector)
            self.driver.keyboard_enter(selector)
        except IndexError:
            self.driver.execute_js_script(js, selector)
            # 将时间输入到文本框中
            time_text = time.replace(' ', '')
            self.driver.send_keys(selector, time_text)
            self.driver.click(selector)
            self.driver.keyboard_enter(selector)

    def get_warning_text(self):
        self.driver.sleep(1)
        text = self.driver.get_text(self.__get_dms_element()['警告'])
        return text


def get_driver():
    """
    返回一个dirver对象。
    :return:
    """
    driver = BoxDriver(GetIniData().get_ini_data("Browser", "browser"), GetIniData().get_ini_data("Url", "ProjectUrl"))

    return driver


if __name__ == '__main__':
    login = BasePage(get_driver())
    login.login()
    try:
        login.driver.sleep(2)
        login.select_dms_page()
        login.driver.sleep(2)
        login.select_tms_page()
        login.driver.sleep(2)
        login.select_ams_page()
        login.driver.sleep(2)
        login.select_rms_page()
        # login.driver.get_screen_shot(r"D:\Users\C0600\Desktop\text.png")
        login.driver.sleep(2)

    finally:
        login.driver.quit()
