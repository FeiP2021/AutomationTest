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

testData = getyaml(setting.OPS_TEST_Element_YAML+ '/' + 'declarationOnline_D.yaml')
log = Log()

class declarationOnline_D(Page):
    """
    首页---设置页面
    """
    url = ''

 #在线申报   -------------------------------------------------------------------------------------------------------------------------------------------------------
    # 查询和服务
    declarationOnline_D_button0 = (By.XPATH, testData.get_elementinfo(0))
    # 点击在线申报
    declarationOnline_D_button1 = (By.XPATH, testData.get_elementinfo(1))
    # 点击操作
    declarationOnline_D_button2 = (By.XPATH, testData.get_elementinfo(2))
    # 点击编辑申报信息
    declarationOnline_D_button3 = (By.XPATH, testData.get_elementinfo(3))
    # 选D类
    declarationOnline_D_button4 = (By.XPATH, testData.get_elementinfo(4))
    # 点击下一步
    declarationOnline_D_button5 = (By.XPATH, testData.get_elementinfo(5))
    # 选监管方式
    declarationOnline_D_button6 = (By.XPATH, testData.get_elementinfo(6))
    # 选第一个
    declarationOnline_D_button7 = (By.XPATH, testData.get_elementinfo(7))
    # 选成交方式
    declarationOnline_D_button8 = (By.XPATH, testData.get_elementinfo(8))
    # 选FOB
    declarationOnline_D_button9 = (By.XPATH, testData.get_elementinfo(9))
    # 填毛重
    declarationOnline_D_button10 = (By.XPATH, testData.get_elementinfo(10))
    # 填淨重
    declarationOnline_D_button11 = (By.XPATH, testData.get_elementinfo(11))
    # 填合同协议号
    declarationOnline_D_button12 = (By.XPATH, testData.get_elementinfo(12))
    # 选贸易国别
    declarationOnline_D_button13= (By.XPATH, testData.get_elementinfo(13))
    # 选ASM
    declarationOnline_D_button14 = (By.XPATH, testData.get_elementinfo(14))
    # 下一步
    declarationOnline_D_button15 = (By.XPATH, testData.get_elementinfo(15))
    # 选常用商品
    declarationOnline_D_button16 = (By.XPATH, testData.get_elementinfo(16))
    # 选第三个
    declarationOnline_D_button17 = (By.XPATH, testData.get_elementinfo(17))
    # 填法定数量
    declarationOnline_D_button18 = (By.XPATH, testData.get_elementinfo(18))
    # 选境内货源地
    declarationOnline_D_button19 = (By.XPATH, testData.get_elementinfo(19))
    # 选个区
    declarationOnline_D_button20= (By.XPATH, testData.get_elementinfo(20))
    # 点保存
    declarationOnline_D_button21 = (By.XPATH, testData.get_elementinfo(21))
    # 点下一步
    declarationOnline_D_button22 = (By.XPATH, testData.get_elementinfo(22))
    # 点预览
    declarationOnline_D_button23= (By.XPATH, testData.get_elementinfo(23))
    # 我同意
    declarationOnline_D_button24 = (By.XPATH, testData.get_elementinfo(24))
    # 提交
    declarationOnline_D_button25 = (By.XPATH, testData.get_elementinfo(25))
    # 确定
    declarationOnline_D_button26 = (By.XPATH, testData.get_elementinfo(26))










        #self.driver.switch_to_window(windows[0])  # 切换回窗口
        #sleep(3)

    def declarationOnline_D_user(self):
        """
        :param comment
        :return:
        """
        above = self.find_element(*self.declarationOnline_D_button0)
        ActionChains(self.driver).move_to_element(above).perform()
        sleep(1)
        self.find_element(*self.declarationOnline_D_button1).click()
        sleep(1)
        self.find_element(*self.declarationOnline_D_button2).click()
        sleep(1)
        self.find_element(*self.declarationOnline_D_button3).click()
        sleep(1)
        # self.find_element(*self.declarationOnline_D_button4).click()
        sleep(1)
        self.find_element(*self.declarationOnline_D_button5).click()
        sleep(1)
        #填监管方式
        self.find_element(*self.declarationOnline_D_button6).click()
        sleep(1)
        above1 = self.find_element(*self.declarationOnline_D_button7)
        ActionChains(self.driver).move_to_element(above1).perform()
       # sleep(1)
        self.find_element(*self.declarationOnline_D_button7).click()
        #填成交方式
        self.find_element(*self.declarationOnline_D_button8).click()
        sleep(1)
        above1 = self.find_element(*self.declarationOnline_D_button9)
        ActionChains(self.driver).move_to_element(above1).perform()
       # sleep(1)
        self.find_element(*self.declarationOnline_D_button9).click()
        sleep(1)
        #清除后填毛重
        self.find_element(*self.declarationOnline_D_button10).clear()
        sleep(1)
        self.find_element(*self.declarationOnline_D_button10).send_keys('2')
        sleep(1)
        #填净重
        self.find_element(*self.declarationOnline_button11).send_keys('100')
        sleep(1)
        #填协议号
        self.find_element(*self.declarationOnline_button12).send_keys('1234')
        sleep(1)
        #选贸易国别
        self.find_element(*self.declarationOnline_D_button13).click()
        sleep(1)
        above1 = self.find_element(*self.declarationOnline_D_button14)
        ActionChains(self.driver).move_to_element(above1).perform()
        # sleep(1)
        self.find_element(*self.declarationOnline_D_button14).click()
        sleep(1)
        self.find_element(*self.declarationOnline_D_button15).click()
        sleep(1)
        self.find_element(*self.declarationOnline_D_button16).click()
        sleep(1)
        #选第三个
        windows=self.driver.window_handles
        self.driver.switch_to_window(windows[-1])
        self.find_element(*self.declarationOnline_D_button17).click()
        sleep(1)
        self.find_element(*self.declarationOnline_D_button18).send_keys('1')
        #选境内货源地
        self.find_element(*self.declarationOnline_D_button19).click()
        sleep(1)
        above1 = self.find_element(*self.declarationOnline_D_button20)
        ActionChains(self.driver).move_to_element(above1).perform()
        # sleep(1)
        self.find_element(*self.declarationOnline_D_button20).click()
        sleep(1)
        #点保存
        self.find_element(*self.declarationOnline_D_button21).click()
        sleep(1)
        self.find_element(*self.declarationOnline_D_button22).click()
        sleep(1)
        self.find_element(*self.declarationOnline_D_button23).click()
        sleep(1)
        self.find_element(*self.declarationOnline_D_button24).click()
        sleep(1)
        self.find_element(*self.declarationOnline_D_button25).click()
        sleep(1)
        self.find_element(*self.declarationOnline_D_button26).click()
        sleep(1)

