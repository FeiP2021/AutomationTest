#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = 'YinJia'

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

testData = getyaml(setting.TEST_Element_YAML + '/' + 'onlinePay.yaml')
log = Log()

class onlinePay(Page):
    """
    首页---设置页面
    """
    url = '/'

    # 定位器，通过元素属性定位元素对象
    textsetup_loc = (By.XPATH, testData.get_elementinfo(0))
    def dig_setup(self,*data):
        """
        设置操作
        :param data:
        :return:
        """
        # 选择菜单-> 设置
        self.find_element(*self.textsetup_loc).click()
        sleep(1)
