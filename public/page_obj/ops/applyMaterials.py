#!python3.9
# -*- coding: utf-8 -*-
# ---
# @Software: PyCharm
# @File: applyMaterials.py
# @Author: zhaoyj
# @Site: 
# @Time: 9月 07, 2022
# ---
from time import sleep
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from config import setting
from public.models.GetYaml import getyaml
from public.models.log import Log
from public.page_obj.base import Page

testData = getyaml(setting.OPS_TEST_Element_YAML + '/' + 'applyMaterials.yaml')
log = Log()
class applyMaterials(Page):
    """
    备用物料申请页面
    """
    url = ''
    # 申请物料
    applyMaterials_click0=(By.XPATH, testData.get_elementinfo(0))
    applyMaterials_click1=(By.XPATH, testData.get_elementinfo(1))
    applyMaterials_click2=(By.XPATH, testData.get_elementinfo(2))
    applyMaterials_click3=(By.XPATH, testData.get_elementinfo(3))
    applyMaterials_click4=(By.XPATH, testData.get_elementinfo(4))
    applyMaterials_click5=(By.XPATH, testData.get_elementinfo(5))


    def applyMaterialsTest(self):
        """
        提交物料申请
        :return:
        """
        above = self.find_element(*self.applyMaterials_click0)
        ActionChains(self.driver).move_to_element(above).perform()
        sleep(2)
        self.find_element(*self.applyMaterials_click1).click()
        sleep(2)
        # self.find_element(*self.applyMaterials_click2).click()
        Select(self.find_element(*self.applyMaterials_click2)).select_by_index(2)
        sleep(2)
        self.find_element(*self.applyMaterials_click3).click()
        sleep(2)
        self.find_element(*self.applyMaterials_click4).click()
        sleep(2)
        self.find_element(*self.applyMaterials_click5).click()

