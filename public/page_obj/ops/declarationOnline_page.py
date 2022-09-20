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

from selenium.webdriver.support.select import Select

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from config import setting
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from public.page_obj.base import Page
from time import sleep
from public.models.GetYaml import getyaml
from public.models.log import Log

testData = getyaml(setting.OPS_TEST_Element_YAML+ '/' + 'declarationOnline.yaml')
log = Log()

class declarationOnline(Page):
    """
    首页---设置页面
    """
    url = ''

 #在线申报   -------------------------------------------------------------------------------------------------------------------------------------------------------
    # 查询和服务
    declarationOnline_button0 = (By.XPATH, testData.get_elementinfo(0))
    # 点击在线申报
    declarationOnline_button1 = (By.XPATH, testData.get_elementinfo(1))
    # 点击操作
    declarationOnline_button2 = (By.XPATH, testData.get_elementinfo(2))
    # 点击编辑申报信息
    declarationOnline_button3 = (By.XPATH, testData.get_elementinfo(3))
    # 选C类
    declarationOnline_button4 = (By.XPATH, testData.get_elementinfo(4))
    # 点击下一步
    declarationOnline_button5 = (By.XPATH, testData.get_elementinfo(5))
    # 选1
    declarationOnline_button6 = (By.XPATH, testData.get_elementinfo(6))
    # 选2
    declarationOnline_button7 = (By.XPATH, testData.get_elementinfo(7))
    # 填1
    declarationOnline_button8 = (By.XPATH, testData.get_elementinfo(8))
    # 选3
    declarationOnline_button9 = (By.XPATH, testData.get_elementinfo(9))
    # 下一步
    declarationOnline_button10 = (By.XPATH, testData.get_elementinfo(10))
    # 选常用
    declarationOnline_button11 = (By.XPATH, testData.get_elementinfo(11))
    # 点预览
    declarationOnline_button12 = (By.XPATH, testData.get_elementinfo(12))
    # 点击我同意
    declarationOnline_button13 = (By.XPATH, testData.get_elementinfo(13))
    # 点击提交
    declarationOnline_button14 = (By.XPATH, testData.get_elementinfo(14))
    # 点击确定
    declarationOnline_button15 = (By.XPATH, testData.get_elementinfo(15))

        #self.driver.switch_to_window(windows[0])  # 切换回窗口
        #sleep(3)

    def declarationOnline_user(self):
        """
        :param comment
        :return:
        """
        above = self.find_element(*self.declarationOnline_button0)
        ActionChains(self.driver).move_to_element(above).perform()
        sleep(1)
        self.find_element(*self.declarationOnline_button1).click()
        sleep(1)
        self.find_element(*self.declarationOnline_button2).click()
        sleep(1)
        self.find_element(*self.declarationOnline_button3).click()
        sleep(1)
        self.find_element(*self.declarationOnline_button4).click()
        sleep(1)
        self.find_element(*self.declarationOnline_button5).click()
        sleep(1)
        Select(self.find_element(*self.declarationOnline_button6)).select_by_index(0)
        sleep(2)
        Select(self.find_element(*self.declarationOnline_button7)).select_by_index(0)
        sleep(2)
        self.find_element(*self.declarationOnline_button8).send_keys('100')
        sleep(1)
        Select(self.find_element(*self.declarationOnline_button9)).select_by_index(1)
        sleep(2)
        self.find_element(*self.declarationOnline_button10).click()
        sleep(1)
        self.find_element(*self.declarationOnline_button11).click()
        sleep(1)
        self.find_element(*self.declarationOnline_button12).click()
        sleep(1)
        self.find_element(*self.declarationOnline_button13).click()
        sleep(1)
        self.find_element(*self.declarationOnline_button14).click()
        sleep(1)
        self.find_element(*self.declarationOnline_button15).click()
        sleep(1)
