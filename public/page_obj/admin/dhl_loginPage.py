#!python3.9
# -*- coding: utf-8 -*-
# ---
# @Software: PyCharm
# @Author: zhaoyj
# @Site:
# @Time: 9月 07, 2022
# ---
import os, sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from config import setting
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from public.page_obj.base import Page
from time import sleep
from public.models.GetYaml import getyaml

testData = getyaml(setting.ADMIN_TEST_Element_YAML + '/' + '5idhl_login.yaml')


class dhl_login(Page):
    """
    用户登录页面
    """
    url = ''
    dig_login_button_loc1 = (By.XPATH, testData.get_elementinfo(0))

    def dig_login1(self):
        """
        首页登录
        :return:
        """
        self.find_element(*self.dig_login_button_loc1).click()
        sleep(1)

    dig_login_button_loc2 = (By.XPATH, testData.get_elementinfo(1))

    def dig_login2(self):
        """
        首页登录
        :return:
        """
        self.find_element(*self.dig_login_button_loc2).click()
        sleep(1)

    # 定位器，通过元素属性定位元素对象
    # 手机号输入框
    login_phone_loc = (By.XPATH, testData.get_elementinfo(2))
    # 密码输入框
    login_password_loc = (By.XPATH, testData.get_elementinfo(3))
    # 验证码输入框
    login_code_loc = (By.XPATH, testData.get_elementinfo(4))
    # 点击登录
    login_button_loc3 = (By.XPATH, testData.get_elementinfo(5))
    # 点击退出
    logout_button1 = (By.XPATH, testData.get_elementinfo(6))

    def login_phone(self, phone):
        """
        登录手机号
        :param username:
        :return:
        """
        self.find_element(*self.login_phone_loc).send_keys(phone)

    def login_password(self, password):
        """
        登录密码
        :param password:
        :return:
        """
        self.find_element(*self.login_password_loc).send_keys(password)

    def login_code(self, code):
        """
        验证码
        :param code:
        :return:
        """
        self.find_element(*self.login_code_loc).send_keys(code)

    # def keeplogin(self):
    #     """
    #     取消单选自动登录
    #     :return:
    #     """
    #     self.find_element(*self.keeplogin_button_loc).click()

    def login_button3(self):
        """
        登录按钮
        :return:
        """
        self.find_element(*self.login_button_loc3).click()

    def logout_button(self):
        """
        退出按钮
        :return:
        """
        self.find_element(*self.logout_button1).click()

    def login_exit(self):
        """
        退出系统
        :return:
        """
        above = self.find_element(*self.login_exit_loc)
        ActionChains(self.driver).move_to_element(above).perform()
        sleep(2)
        self.find_element(*self.login_exit_button_loc).click()

    def user_login(self, phone, password, code):
        """
        登录入口
        :param username: 用户名
        :param password: 密码
        :param code: 验证码
        :return:
        """
        self.open()
        self.dig_login1()
        self.dig_login2()
        self.login_phone(phone)
        sleep(1)
        self.login_password(password)
        sleep(1)
        self.login_code(code)
        sleep(1)
        # self.keeplogin()
        self.login_button3()
        sleep(3)
        # self.logout_button
        # sleep(3)
