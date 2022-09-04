#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = 'YinJia'

import os,sys
from selenium.webdriver import ActionChains
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from config import setting
from selenium.webdriver.common.by import By
from public.page_obj.base import Page
from time import sleep
from public.models.GetYaml import getyaml
from public.models.log import Log

testData = getyaml(setting.TEST_Element_YAML + '/' + 'onlinePay.yaml')
log = Log()

class onlinePay(Page):
    """
    首页---设置页面
    """
    url = ''
    # 点击查询和服务
    onlinePay_click0=(By.XPATH, testData.get_elementinfo(0))
    # 点击在线付款
    onlinePay_click1=(By.XPATH, testData.get_elementinfo(1))
    # 输入赊销账号
    onlinePay_click2=(By.NAME, testData.get_elementinfo(2))
    # 输入付款金额
    onlinePay_click3=(By.NAME, testData.get_elementinfo(3))
    # 提交订单并支付
    onlinePay_click4=(By.XPATH, testData.get_elementinfo(4))
    # 立即支付
    onlinePay_click5=(By.XPATH, testData.get_elementinfo(5))

    def onlinePay_Credit(self, dhlCreditCode, count):
        """
        生成付款码
        :param dhlCreditCode:
        :param count:
        :return:
        """
        above = self.find_element(*self.onlinePay_click0)
        ActionChains(self.driver).move_to_element(above).perform()
        sleep(3)
        self.find_element(*self.onlinePay_click1).click()
        sleep(1)
        self.find_element(*self.onlinePay_click2).send_keys(dhlCreditCode)
        sleep(1)
        self.find_element(*self.onlinePay_click3).send_keys(count)
        sleep(1)
        self.find_element(*self.onlinePay_click4).click()
        sleep(1)
        self.find_element(*self.onlinePay_click5).click()
        sleep(5)