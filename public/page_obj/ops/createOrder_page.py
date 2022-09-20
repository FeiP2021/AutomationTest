#!python3.9
# -*- coding: utf-8 -*-
# ---
# @Software: PyCharm
# @File: declarationOnline_page.py
# @Author: feip
# @Site: 
# @Time: 10:43,9月 19, 2022
# ---
import os,sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from config import setting
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from public.page_obj.base import Page
from time import sleep
from public.models.GetYaml import getyaml
from public.models.log import Log

testData = getyaml(setting.OPS_TEST_Element_YAML+ '/' + 'createOrder.yaml')
log = Log()

class createOrder(Page):
    """
    首页---设置页面
    """
    url = ''

    # 点击我要寄件
    declarationOnline_button1 = (By.XPATH, testData.get_elementinfo(0))
    #点击创建运单
    declarationOnline_button2 = (By.XPATH, testData.get_elementinfo(1))
    #选择账号制单
    declarationOnline_button3 = (By.XPATH, testData.get_elementinfo(2))
    # 选账号
    declarationOnline_button4 = (By.XPATH, testData.get_elementinfo(3))
    # 点确定
    declarationOnline_button5 = (By.XPATH, testData.get_elementinfo(4))
    # 选地址1
    declarationOnline_button6 = (By.XPATH, testData.get_elementinfo(5))
    # 点确定
    declarationOnline_button7 = (By.XPATH, testData.get_elementinfo(6))
    # 选地址2
    declarationOnline_button8 = (By.XPATH, testData.get_elementinfo(7))
    # 点确定
    declarationOnline_button9 = (By.XPATH, testData.get_elementinfo(8))
    # 选说明
    declarationOnline_button10 = (By.XPATH, testData.get_elementinfo(9))
    # 点确定
    declarationOnline_button11 = (By.XPATH, testData.get_elementinfo(10))
    # 填金额
    declarationOnline_button12 = (By.XPATH, testData.get_elementinfo(11))
    # 点我同意
    declarationOnline_button13 = (By.XPATH, testData.get_elementinfo(12))
    # 选明细
    declarationOnline_button14 = (By.XPATH, testData.get_elementinfo(13))
    # 点确定
    declarationOnline_button15 = (By.XPATH, testData.get_elementinfo(14))
    # 点提交
    declarationOnline_button16 = (By.XPATH, testData.get_elementinfo(15))
    # 点继续打印
    declarationOnline_button17 = (By.XPATH, testData.get_elementinfo(16))





    def createOrder_test(self):
        """
        :param comment
        :return:
        """
        above = self.find_element(*self.declarationOnline_button1)
        ActionChains(self.driver).move_to_element(above).perform()
        sleep(1)
        self.find_element(*self.declarationOnline_button2).click()
        sleep(1)
        self.find_element(*self.declarationOnline_button3).click()
        sleep(1)
        windows=self.driver.window_handles
        self.driver.switch_to_window(windows[-1])   # 切换窗口
        self.find_element(*self.declarationOnline_button4).click()
        sleep(1)
        windows=self.driver.window_handles
        self.driver.switch_to_window(windows[-1])
        self.find_element(*self.declarationOnline_button5).click()
        sleep(1)
        windows=self.driver.window_handles
        self.driver.switch_to_window(windows[-1])
        self.find_element(*self.declarationOnline_button6).click()
        sleep(1)
        windows=self.driver.window_handles
        self.driver.switch_to_window(windows[-1])
        self.find_element(*self.declarationOnline_button7).click()
        sleep(1)
        windows=self.driver.window_handles
        self.driver.switch_to_window(windows[-1])
        self.find_element(*self.declarationOnline_button8).click()
        sleep(1)
        windows=self.driver.window_handles
        self.driver.switch_to_window(windows[-1])
        self.find_element(*self.declarationOnline_button9).click()
        sleep(1)
        windows=self.driver.window_handles
        self.driver.switch_to_window(windows[-1])
        self.find_element(*self.declarationOnline_button10).click()
        sleep(1)
        windows=self.driver.window_handles
        self.driver.switch_to_window(windows[-1])
        self.find_element(*self.declarationOnline_button11).click()
        sleep(1)
        windows=self.driver.window_handles
        self.driver.switch_to_window(windows[-1])
        self.find_element(*self.declarationOnline_button12).send_keys('100')
        sleep(1)
        self.driver.switch_to_window(windows[-1])
        self.find_element(*self.declarationOnline_button13).click()
        sleep(1)
        windows=self.driver.window_handles
        self.driver.switch_to_window(windows[-1])
        self.find_element(*self.declarationOnline_button14).click()
        sleep(1)
        windows=self.driver.window_handles
        self.driver.switch_to_window(windows[-1])
        self.find_element(*self.declarationOnline_button15).click()
        sleep(1)
       # self.driver.switch_to_window(windows[-1])
        print("开始提交")
        windows=self.driver.window_handles
        self.driver.switch_to_window(windows[-1])
        self.find_element(*self.declarationOnline_button16).click()
        sleep(3)
        windows=self.driver.window_handles
        self.driver.switch_to_window(windows[-1])
        self.find_element(*self.declarationOnline_button17).click()
        sleep(3)
        print("结束提交")
        self.driver.close()
        windows=self.driver.window_handles
        self.driver.switch_to_window(windows[0])
        sleep(3)
        self.driver.refresh()
        sleep(5)
