# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# Author: LiYangYang            # Date: 2020 年
# Description:
# 对webdirver的二次封装。
# -----------------------------------------------------------------------------------

from time import sleep

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

POLL_FREQUENCY = 0.5  # How long to sleep inbetween calls to the method
TIME_OUT = 8  # 等待时长


class BoxDriver:

    def __init__(self, bowser_driver, url):
        option = webdriver.ChromeOptions()
        option.add_experimental_option("useAutomationExtension", False)
        option.add_experimental_option("excludeSwitches", ["enable - automation"])
        # 不自动关闭浏览器
        option.add_experimental_option("detach", True)

        if bowser_driver == 'Chrome':
            driver = webdriver.Chrome()

        elif bowser_driver == 'Firefox':
            driver = webdriver.Firefox()

        else:
            driver = webdriver.Ie()
        try:
            self._base_driver = driver

        except NameError:
            raise NameError('请输入正确浏览器名称')

        self.implicitly_wait(10)
        self._base_driver.get(url)

    def maximize_window(self):
        """
        最大化窗口
        :return:
        """
        self._base_driver.maximize_window()

    def minimize_window(self):
        """
        最小化窗口
        :return:
        """
        self._base_driver.minimize_window()

    def implicitly_wait(self, second):
        """
        隐式等待
        :param second:等待时间:s
        :return:
        """
        self._base_driver.implicitly_wait(second)

    def _web_driver_wait(self, selector, timeout=TIME_OUT, poll_frequency=POLL_FREQUENCY):
        """
        显式等待
        :return:
        """
        locator = self.__convert_selector_to_locator(selector)
        eme_selector = WebDriverWait(self._base_driver, timeout, poll_frequency).until(
            EC.presence_of_element_located(locator))
        return eme_selector

    def __convert_selector_to_locator(self, selector):
        """
        将selector数据(id,account)转换为(By.ID,account)格式
        :param selector: 元素定位方式和对应的值 如id,account
        :return:
        """
        try:
            selector_by = selector.split("=")[0].strip()  # 将selector的值切割成对应的方式和值
            selector_value = selector.split("=")[1].strip()

        except IndexError:
            selector_by = selector.split(",")[0].strip()  # 将selector的值切割成对应的方式和值
            selector_value = selector.split(",")[1].strip()
        try:
            if selector_by == 'i' or selector_by == 'id':
                locator = (By.ID, selector_value)

            elif selector_by == 'n' or selector_by == 'name':
                locator = (By.NAME, selector_value)

            elif selector_by == 'c' or selector_by == 'class':
                locator = (By.CLASS_NAME, selector_value)

            elif selector_by == 'l' or selector_by == 'linkText':
                locator = (By.LINK_TEXT, selector_value)

            elif selector_by == 'p' or selector_by == 'partial_link_text':
                locator = (By.PARTIAL_LINK_TEXT, selector_value)

            elif selector_by == 't' or selector_by == 'tag_name':
                locator = (By.TAG_NAME, selector_value)

            elif selector_by == 'x' or selector_by == 'xpath':
                locator = (By.XPATH, selector_value)

            elif selector_by == 'css' or selector_by == 'css_selector':
                locator = (By.CSS_SELECTOR, selector_value)

            else:
                raise NameError("参数不正确")
            return locator
        except NameError:
            selector_by = selector.split(",")[0].strip()  # 将selector的值切割成对应的方式和值
            selector_value = selector.split(",")[1].strip()
            if selector_by == 'i' or selector_by == 'id':
                locator = (By.ID, selector_value)

            elif selector_by == 'n' or selector_by == 'name':
                locator = (By.NAME, selector_value)

            elif selector_by == 'c' or selector_by == 'class':
                locator = (By.CLASS_NAME, selector_value)

            elif selector_by == 'l' or selector_by == 'linkText':
                locator = (By.LINK_TEXT, selector_value)

            elif selector_by == 'p' or selector_by == 'partial_link_text':
                locator = (By.PARTIAL_LINK_TEXT, selector_value)

            elif selector_by == 't' or selector_by == 'tag_name':
                locator = (By.TAG_NAME, selector_value)

            elif selector_by == 'x' or selector_by == 'xpath':
                locator = (By.XPATH, selector_value)

            elif selector_by == 'css' or selector_by == 'css_selector':
                locator = (By.CSS_SELECTOR, selector_value)

            else:
                raise NameError("参数不正确")
            return locator

    def __locate_element(self, selector):
        """
        定位单个元素
        :param selector:元素的定位方式和对应的值：如：id ，account
        :return:    ele
        """
        locator = self.__convert_selector_to_locator(selector)
        ele = self._base_driver.find_element(*locator)
        return ele

    def send_keys(self, selector, text):
        """
        显示等待selector元素,传入内容text
        :param selector: 元素对象
        :param text: 输入内容
        :return:
        """
        self._web_driver_wait(selector).clear()
        self._web_driver_wait(selector).send_keys(text)

    def click(self, selector):
        """
        显式等待对象元素,对该元素点击.
        :param selector:元素对象
        :return:
        """

        self._web_driver_wait(selector).click()

    def get_attribute_text(self, selector, attribute):
        """
        获取元素的属性值
        :param selector:
        :param attribute: 属性名字，例如：value
        :return:
        """
        ele = self._web_driver_wait(selector)
        text = ele.get_attribute(attribute)
        return text

    def get_text(self, selector):
        """
        获取目标文本内容并返回
        :param selector:
        :return:
        """
        ele_text = self._web_driver_wait(selector)
        get_txt = ele_text.text
        return get_txt

    def switch_to_frame_index(self, index):
        # int_index = int(index)
        self._base_driver.switch_to.frame(index)

    def switch_to_frame(self, selector):
        """
        进入iframe
        :param selector:
        :return:
        """
        iframe = self._web_driver_wait(selector)
        self._base_driver.switch_to.frame(iframe)

    def old_switch_to_frame(self, selector):

        iframe = self.__locate_element(selector)
        self._base_driver.switch_to.frame(iframe)

    def switch_to_parent(self):
        """
        退出到上一层iframe
        :return:
        """
        self._base_driver.switch_to.parent_frame()

    def switch_to_default(self):
        """
        退出到iframe最外层
        :return:
        """
        self._base_driver.switch_to.default_content()

    def switch_to_alert(self, verdict):
        """
        处理alert框
        :param verdict:'y'确认删除,'n'取消
        :return:
        """
        if verdict == 'yes':
            self._base_driver.switch_to.alert.accept()
        if verdict == 'no':
            self._base_driver.switch_to.alert.dismiss()

    def send_keys_alert(self, text):
        """
        向alert框发送文本
        :param text:
        :return:
        """
        self.sleep(1)
        self._base_driver.switch_to.alert().send_keys(text)

    def get_alert_text(self):
        self.sleep(1)
        return self._base_driver.switch_to.alert().text

    def switch_to_window(self, index):
        """
        根据句柄进入窗口
        :param index:0代表第一个窗口,1代表第二个窗口
        :return:
        """
        window_handle = self._base_driver.window_handles[index].strip()
        self._base_driver.switch_to.window(window_handle)

    def select_by_index(self, selector, num):
        """
        通过索引定位
        :param selector:
        :param num:
        :return:
        """
        on_element = self._web_driver_wait(selector)
        Select(on_element).select_by_index(num)

    def select_by_value(self, selector, value):
        """
        通过value值定位
        :param selector: 素定位方式和相对应的值，如'id,account'
        :param value: 值
        :return:
        """
        on_element = self._web_driver_wait(selector)
        Select(on_element).select_by_value(value)

    def select_by_visible_text(self, selector, text):
        """
        通过文本定位
        :param selector: 素定位方式和相对应的值，如'id,account'
        :param text: 文本
        :return:
        """
        on_element = self._web_driver_wait(selector)
        Select(on_element).select_by_visible_text(text)

    def get_screen_shot(self, file_name):
        """
        对浏览器当前页面进行截图
        :param file_name:存储截图的完整路径
        :return:
        """
        self._base_driver.get_screenshot_as_file(file_name)

    def keyboard_enter(self, selector):
        """
        模拟键盘点击回车键
        :param selector:
        :return:
        """
        self._web_driver_wait(selector).send_keys(Keys().ENTER)

    def mouse_click(self, selector):
        """
        模拟鼠标单击元素。
        :param selector:（id,kw）
        :return:
        """
        on_element = self._web_driver_wait(selector)
        ActionChains(self._base_driver).click(on_element).perform()

    def mouse_double_click(self, selector):
        """
        模拟鼠标双击元素
        :param selector: （id,kw）
        :return:
        """
        on_element = self._web_driver_wait(selector)
        ActionChains(self._base_driver).double_click(on_element).perform()

    def mouse_move_to_element(self, selector):
        """
        移动鼠标指针到指定元素上
        :param selector:
        :return:
        """
        on_element = self._web_driver_wait(selector)
        ActionChains(self._base_driver).move_to_element(on_element).perform()

    def execute_js_script(self, js_script: str, selector):
        """
        执行JS脚本
        """
        ele = self._web_driver_wait(selector)
        self._base_driver.execute_script(js_script, ele)

    def sleep(self, second):
        """
        基于time.sleep的封装
        :param second: 睡眠时长,单位秒
        :return:
        """
        sleep(second)

    def refresh_windows(self):
        # 刷新窗口
        self._base_driver.refresh()

    def close(self):
        """
        关闭浏览器页面
        :return:
        """
        self._base_driver.close()

    def quit(self):
        """
        关闭浏览器进程
        :return:
        """
        self._base_driver.quit()


class BaseDriver:
    """
    driver是用来接收BOxdriver类的实例化对象
    """

    def __init__(self, driver: BoxDriver):
        self.driver = driver


if __name__ == '__main__':
    a = BoxDriver('Chrome', r'https://www.baidu.com/')
    d = BaseDriver(a)
    d.driver.maximize_window()

    try:
        js = '"arguments[0].scrollIntoView();"'
        d.driver.send_keys('xpath=//*[@id,"kw"]',"测试")


    finally:
        d.driver.sleep(5)
        d.driver.quit()
