#!python3.9
# -*- coding: utf-8 -*-
# ---
# @Software: PyCharm
# @File: payment_record_page.py
# @Author: feip
# @Site: 
# @Time: 17:26,9月 09, 2022
# ---
import os,sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from config import setting
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from public.page_obj.base import Page
from time import sleep
from public.models.GetYaml import getyaml
from public.models.log import Log


testData = getyaml(setting.FIN_TEST_Element_YAML + '/' + 'payment_record.yaml')
log = Log()

class payment_record(Page):
    """
    首页---设置页面
    """
    url = ''

    # 点击个人中心
    payment_record_button1 = (By.XPATH, testData.get_elementinfo(0))
    #点击付款记录
    payment_record_button2 = (By.XPATH, testData.get_elementinfo(1))
    #点击支付
    payment_record_button3 = (By.XPATH, testData.get_elementinfo(2))
    # 点击立即支付
    payment_record_button4 = (By.XPATH, testData.get_elementinfo(3))


    def payment_record1(self):
        """
        点击个人中心
        :return:
        """
        self.find_element(*self.payment_record_button1).click()


    def payment_record2(self):
        """
        点击付款记录
        :return:
        """
        self.find_element(*self.payment_record_button2).click()

    def payment_record3(self):
        """
        点击支付
        :return:
        """
        self.find_element(*self.payment_record_button3).click()

    def payment_record4(self):
        """
        点击立即付款
        :return:
        """
        self.find_element(*self.payment_record_button4).click()



    def user_payment_record(self):
        """
        登录入口
        :param country
        :param money
        :return:
        """

        above = self.find_element(*self.payment_record_button1)
        ActionChains(self.driver).move_to_element(above).perform()
        sleep(3)
        # self.dig_setup()
        # sleep(1)
        self.payment_record1()
        sleep(1)
        self.payment_record2()
        sleep(2)
        self.payment_record3()
        sleep(3)
        self.payment_record4()
        sleep(30)
