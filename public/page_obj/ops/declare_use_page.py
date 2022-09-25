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



testData = getyaml(setting.OPS_TEST_Element_YAML+ '/' + 'declare_use.yaml')
log = Log()


class declare_use(Page):
    """
    首页---设置页面
    """
    url = ''

 #在线申报   -------------------------------------------------------------------------------------------------------------------------------------------------------
    # 个人中心
    declare_use_begin0 = (By.XPATH, testData.get_elementinfo(0))
    # 常用申报信息
    declare_use_begin1 = (By.XPATH, testData.get_elementinfo(1))
    # 常用申报/消费单位
    declare_platform_begin2 = (By.XPATH, testData.get_elementinfo(13))
#添加
    # 点击添加
    declare_use_add0 = (By.XPATH, testData.get_elementinfo(2))
    # 输信用代码
    declare_use_add1 = (By.XPATH, testData.get_elementinfo(3))
    # 填名称
    declare_use_add2 = (By.XPATH, testData.get_elementinfo(4))
    # 填编号
    declare_use_add3 = (By.XPATH, testData.get_elementinfo(5))
    # 点确定
    declare_use_add4 = (By.XPATH, testData.get_elementinfo(6))
#编辑
    # 点编辑
    declare_use_alter0 = (By.XPATH, testData.get_elementinfo(7))
    # 修改名称
    declare_use_alter1 = (By.XPATH, testData.get_elementinfo(8))
    # 点确定
    declare_use_alter2 = (By.XPATH, testData.get_elementinfo(9))
#删除
    # 点编辑
    declare_use_delete0 = (By.XPATH, testData.get_elementinfo(10))
    # 点删除
    declare_use_delete1 = (By.XPATH, testData.get_elementinfo(11))
    # 点确定
    declare_use_delete2 = (By.XPATH, testData.get_elementinfo(12))

        #self.driver.switch_to_window(windows[0])  # 切换回窗口
        #sleep(3)

    def declare_use_user(self):
        """
        :param comment
        :return:
        """
        above = self.find_element(*self.declare_use_begin0)
        ActionChains(self.driver).move_to_element(above).perform()
        sleep(1)
        self.find_element(*self.declare_use_begin1).click()
        sleep(1)
        self.find_element(*self.declare_use_begin2).click()
        sleep(1)
        self.find_element(*self.declare_use_add0).click()
        sleep(1)
        self.find_element(*self.declare_use_add1).send_keys('123412341234111111')
        sleep(1)
        self.find_element(*self.declare_use_add2).click()
        sleep(5)
      #  ui.WebDriverWait(driver,10).until(EC.visibility_of_element_located(By.XPATH,locator='//body[@id='BodyID']/app-root/div[5]/span'))
        self.find_element(*self.declare_use_add2).send_keys('测试添加经营单位')
        sleep(1)
        self.find_element(*self.declare_use_add3).send_keys('1234123412')
        sleep(1)
        self.find_element(*self.declare_use_add4).click()
       # WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element_value((By.CSS_SELECTOR, '#position_relative'), u'测试添加经营单位'))

        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.XPATH, "/html/body/app-root/div[2]/app-commonly-used-declaration-information/div/div[2]/div[2]/div/table/tbody/tr[2]/td[1]"), u'测试添加经营单位'))

       # WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(*self.declare_management_add4))
      #  ui.WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element_value((By.XPATH, "/html/body/app-root/div[2]/app-commonly-used-declaration-information/div/div[2]/div[2]/div/table/tbody/tr[2]/td[1]"),u'测试添加'))

       # WebDriverWait(driver,10).until(EC.visibility_of(driver.find_element(by=By.ID,value='测试添加经营单位')))

        self.find_element(*self.declare_use_alter0).click()
        sleep(1)
        self.find_element(*self.declare_use_alter1).send_keys('修改嘎嘎嘎')
        sleep(1)
        self.find_element(*self.declare_use_alter2).click()
        sleep(1)

        self.find_element(*self.declare_use_delete0).click()
        sleep(1)
        self.find_element(*self.declare_use_delete1).click()
        sleep(1)
        self.find_element(*self.declare_use_delete2).click()
        sleep(1)
