#!python3.9
# -*- coding: utf-8 -*-
# ---
# @Software: PyCharm
# @Author: zhaoyj
# @Site:
# @Time: 9月 07, 2022
# ---
from  .driver import browser
import unittest


class MyTest(unittest.TestCase):
    """
    自定义MyTest类
    """

    @classmethod
    def setUpClass(cls):
        cls.driver = browser()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()