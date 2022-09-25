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



testData = getyaml(setting.OPS_TEST_Element_YAML+ '/' + 'declare_comgood.yaml')
log = Log()


class declare_comgood(Page):
    """
    首页---设置页面
    """
    url = ''

 #在线申报   -------------------------------------------------------------------------------------------------------------------------------------------------------
    # 个人中心
    declare_commongood_begin0 = (By.XPATH, testData.get_elementinfo(0))
    # 常用申报信息
    declare_commongood_begin1 = (By.XPATH, testData.get_elementinfo(1))
    # 常用商品
    declare_commongood_begin2 = (By.XPATH, testData.get_elementinfo(2))
#添加
    # 点击新增
    declare_commongood_add0 = (By.XPATH, testData.get_elementinfo(3))
    # 选择商品编码
    declare_commongood_add1 = (By.XPATH, testData.get_elementinfo(4))
    # 输入商品名称
    declare_commongood_add2 = (By.XPATH, testData.get_elementinfo(5))
    # 点击查询商品编码
    declare_commongood_add3 = (By.XPATH, testData.get_elementinfo(6))
    # 选择第一个
    declare_commongood_add4 = (By.XPATH, testData.get_elementinfo(7))
    # 点击确定
    declare_commongood_add5 = (By.XPATH, testData.get_elementinfo(8))
    # 选择成交单位
    declare_commongood_add6 = (By.XPATH, testData.get_elementinfo(9))
    # 选择单位个
    declare_commongood_add7 = (By.XPATH, testData.get_elementinfo(10))
    # 输入品牌
    declare_commongood_add8 = (By.XPATH, testData.get_elementinfo(11))
    # 选择征免方式
    declare_commongood_add9 = (By.XPATH, testData.get_elementinfo(12))
    # 选照章征税
    declare_commongood_add10 = (By.XPATH, testData.get_elementinfo(13))
    # 选原产国
    declare_commongood_add11= (By.XPATH, testData.get_elementinfo(14))
    # 选择中国
    declare_commongood_add12= (By.XPATH, testData.get_elementinfo(15))
    # 输入繁体字發財趙貓
    declare_commongood_add13= (By.XPATH, testData.get_elementinfo(16))
    # 点击确定添加
    declare_commongood_add14= (By.XPATH, testData.get_elementinfo(17))




#编辑
    # 点编辑
    declare_commongood_alter0 = (By.XPATH, testData.get_elementinfo(18))
    # 修改名称
    declare_commongood_alter1 = (By.XPATH, testData.get_elementinfo(19))
    # 点确定
    declare_commongood_alter2 = (By.XPATH, testData.get_elementinfo(20))
#删除
    # 点编辑
    declare_commongood_delete0 = (By.XPATH, testData.get_elementinfo(21))
    # 点删除
    declare_commongood_delete1 = (By.XPATH, testData.get_elementinfo(22))
    # 点确定
    declare_commongood_delete2 = (By.XPATH, testData.get_elementinfo(23))

        #self.driver.switch_to_window(windows[0])  # 切换回窗口
        #sleep(3)

    def declare_comgood_user(self):
        """
        :param comment
        :return:
        """
        above = self.find_element(*self.declare_commongood_begin0)
        ActionChains(self.driver).move_to_element(above).perform()
        sleep(1)
        self.find_element(*self.declare_commongood_begin1).click()
        sleep(1)
        self.find_element(*self.declare_commongood_begin2).click()
        sleep(1)
        self.find_element(*self.declare_commongood_add0).click()
        sleep(1)
        self.find_element(*self.declare_commongood_add1).click()
        sleep(1)
        self.find_element(*self.declare_commongood_add2).send_keys('眼镜')
        sleep(1)
        self.find_element(*self.declare_commongood_add3).click()
        sleep(1)
        self.find_element(*self.declare_commongood_add4).click()
        sleep(1)
        self.find_element(*self.declare_commongood_add5).click()
        sleep(1)
#选择成交单位
        self.find_element(*self.declare_commongood_add6).click()
        sleep(1)
        above1 = self.find_element(*self.declare_commongood_add7)
        ActionChains(self.driver).move_to_element(above1).perform()
        # sleep(1)
        self.find_element(*self.declare_commongood_add7).click()
        sleep(1)

        self.find_element(*self.declare_commongood_add8).send_keys('234')
        sleep(1)
#选择征免方式
        self.find_element(*self.declare_commongood_add9).click()
        sleep(1)
        above1 = self.find_element(*self.declare_commongood_add10)
        ActionChains(self.driver).move_to_element(above1).perform()
        # sleep(1)
        self.find_element(*self.declare_commongood_add10).click()
        sleep(1)
#选原产国
        self.find_element(*self.declare_commongood_add11).click()
        sleep(1)
        above1 = self.find_element(*self.declare_commongood_add12)
        ActionChains(self.driver).move_to_element(above1).perform()
        # sleep(1)
        self.find_element(*self.declare_commongood_add12).click()
        sleep(1)
        self.find_element(*self.declare_commongood_add13).send_keys('發財趙貓')
        sleep(1)
        self.find_element(*self.declare_commongood_add14).click()
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.XPATH,"/html/body/modal-container/div/div/div/form/ul/li[4]/span/span"),
                                                                             u'商品中文名称不能包含繁体字'))
        sleep(1)
        self.find_element(*self.declare_commongood_add13).clear()
        self.find_element(*self.declare_commongood_add13).send_keys('眼镜')
        sleep(1)
        self.find_element(*self.declare_commongood_add14).click()
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.XPATH,"/html/body/app-root/div[2]/app-commonly-used-declaration-information/div/div[2]/div[2]/div/table/tbody/tr[2]/td[1]/p"),
                                                                             u'眼镜'))






        self.find_element(*self.declare_commongood_alter0).click()
        sleep(1)
        self.find_element(*self.declare_commongood_alter1).send_keys('修改第一次')
        sleep(1)
        self.find_element(*self.declare_commongood_alter2).click()
        sleep(1)

        self.find_element(*self.declare_commongood_delete0).click()
        sleep(1)
        self.find_element(*self.declare_commongood_delete1).click()
        sleep(1)
        self.find_element(*self.declare_commongood_delete2).click()
        sleep(1)
