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
from selenium.common.exceptions import TimeoutException
from public.page_obj.base import Page
from time import sleep
from public.models.GetYaml import getyaml
from public.models.log import Log
#import selenium.webdriver.support.expected_conditions as EC
#import selenium.webdriver.support.ui as ui


from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC



testData = getyaml(setting.OPS_TEST_Element_YAML+ '/' + 'declare_info.yaml')
log = Log()


class declare_info(Page):
    """
    首页---设置页面
    """
    url = ''

 #在线申报   -------------------------------------------------------------------------------------------------------------------------------------------------------
    # 个人中心
    declare_message_begin0 = (By.XPATH, testData.get_elementinfo(0))
    # 常用申报信息
    declare_message_begin1 = (By.XPATH, testData.get_elementinfo(1))
    # 常用申报/消费单位
    declare_message_begin2 = (By.XPATH, testData.get_elementinfo(2))
#添加
    # 点击添加
    declare_message_alter0 = (By.XPATH, testData.get_elementinfo(3))
    # 输信用代码
    declare_message_alter1 = (By.XPATH, testData.get_elementinfo(4))
    # 填名称
    declare_message_alter2 = (By.XPATH, testData.get_elementinfo(5))


        #self.driver.switch_to_window(windows[0])  # 切换回窗口
        #sleep(3)

    def declare_info_user(self):
        """
        :param comment
        :return:
        """
        above = self.find_element(*self.declare_message_begin0)
        ActionChains(self.driver).move_to_element(above).perform()
        sleep(1)
        self.find_element(*self.declare_message_begin1).click()
        sleep(1)
        self.find_element(*self.declare_message_begin2).click()
        sleep(1)
        self.find_element(*self.declare_message_alter0).click()
        sleep(1)
        self.find_element(*self.declare_message_alter1).clear()
        self.find_element(*self.declare_message_alter1).send_keys('2323232323232323')
        sleep(1)
        self.find_element(*self.declare_message_alter2).click()
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.XPATH,"/html/body/app-root/div[2]/app-commonly-used-declaration-information/div/div[2]/div[2]/div/table/tbody/tr[2]/td[2]"),u'2323232323232323'))

