#!python3.9
# -*- coding: utf-8 -*-
# ---
# @Software: PyCharm
# @File: daily_lottery.py
# @Author: feip
# @Site: 
# @Time: 9月 09, 2022
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

testData = getyaml(setting.SLS_TEST_Element_YAML+ '/' + 'daily_lottery.yaml')
log = Log()

class daily_lottery(Page):
    """
    首页---设置页面
    """
    url = ''

    # 点击市场活动
    daily_lottery_button1 = (By.XPATH, testData.get_elementinfo(0))
    #点击每日抽奖
    daily_lottery_button2 = (By.XPATH, testData.get_elementinfo(1))
    #选择账号
    daily_lottery_button3 = (By.XPATH, testData.get_elementinfo(2))
    # 点击进入抽奖页
    daily_lottery_button4 = (By.XPATH, testData.get_elementinfo(3))
    # 点击抽奖
    daily_lottery_button5 = (By.XPATH, testData.get_elementinfo(4))
    # 点击领取奖品
    daily_lottery_button6 = (By.XPATH, testData.get_elementinfo(5))
    # 点击确定
    daily_lottery_button7 = (By.XPATH, testData.get_elementinfo(6))
    # 点击评价1
    daily_lottery_button8 = (By.XPATH, testData.get_elementinfo(7))
    # 点击评价2
    daily_lottery_button9 = (By.XPATH, testData.get_elementinfo(8))
    # 点击评价3
    daily_lottery_button10 = (By.XPATH, testData.get_elementinfo(9))
    # 输入评语
    daily_lottery_button11= (By.XPATH, testData.get_elementinfo(10))
    # 点击提交
    daily_lottery_button12= (By.XPATH, testData.get_elementinfo(11))

    def user_daily_lottery(self,comment):
        """
        :param comment
        :return:
        """
        above = self.find_element(*self.daily_lottery_button1)
        ActionChains(self.driver).move_to_element(above).perform()
        sleep(1)
        self.find_element(*self.daily_lottery_button2).click()
        sleep(1)
        self.find_element(*self.daily_lottery_button3).click()
        sleep(1)
        self.find_element(*self.daily_lottery_button4).click()
        sleep(1)
        self.find_element(*self.daily_lottery_button5).click()
        sleep(1)
        self.find_element(*self.daily_lottery_button6).click()
        sleep(1)
        self.find_element(*self.daily_lottery_button7).click()
        sleep(1)
        self.find_element(*self.daily_lottery_button8).click()
        sleep(1)
        self.find_element(*self.daily_lottery_button9).click()
        sleep(1)
        self.find_element(*self.daily_lottery_button10).click()
        sleep(1)
        self.find_element(*self.daily_lottery_button11).send_keys(comment)
        sleep(1)
        self.find_element(*self.daily_lottery_button12).click()
        sleep(1)