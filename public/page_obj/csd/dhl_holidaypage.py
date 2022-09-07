__author__ = 'TH'

import os, sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from config import setting
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from public.page_obj.base import Page
from time import sleep
from public.models.GetYaml import getyaml

testData = getyaml(setting.CSD_TEST_Element_YAML + '/' + 'holiday.yaml')


class dhl_holiday(Page):
    """

    """
    url = ''
    holiday_button_loc1 = (By.XPATH, testData.get_elementinfo(0))

    def holiday1(self):
        """
        点击在线咨询
        :return:
        """
        self.find_element(*self.holiday_button_loc1).click()
        sleep(3)

    holiday_button_loc2 = (By.XPATH, testData.get_elementinfo(1))

    def holiday2(self):
        """
        点击我要查询
        :return:
        """
        self.find_element(*self.holiday_button_loc2).click()
        sleep(3)

    # 定位器，通过元素属性定位元素对象

    # 点击各国节假日
    holiday_button_loc3= (By.XPATH, testData.get_elementinfo(2))
    # 点击输入框
    holiday_button_locc= (By.XPATH, testData.get_elementinfo(3))
    #输入地区
    holiday_password_loc = (By.XPATH, testData.get_elementinfo(4))
    # 点击查询
    holiday_button_loc4 = (By.XPATH, testData.get_elementinfo(5))

    def holiday3(self):
        """
        点击各国节假日
        :return:
        """
        self.find_element(*self.holiday_button_loc3).click()

    def holidayc(self):
        """
        点击各国节假日
        :return:
        """
        self.find_element(*self.holiday_button_locc).click()


    def holiday4(self):
        """
        输入地区
        :param country:
        :return:
        """
        self.find_element(*self.holiday_password_loc).send_keys('ALBANIA')


    def holiday5(self):
        """
        点击查询
        :return:
        """
        self.find_element(*self.holiday_button_loc4).click()



    def user_holiday(self):
        """
        登录入口
        :param country
        :return:
        """
        self.open()
        sleep(1)
        self.holiday1()
        sleep(1)
        self.holiday2()
        sleep(1)
        self.holiday3()
        sleep(1)
        self.holidayc()
        sleep(3)
        self.holiday4()
        sleep(3)
        self.holiday5()
        sleep(3)
