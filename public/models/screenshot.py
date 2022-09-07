#!python3.9
# -*- coding: utf-8 -*-
# ---
# @Software: PyCharm
# @Author: zhaoyj
# @Site:
# @Time: 9月 07, 2022
# ---
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from config import setting


def insert_img(driver, file_name):
    """
    截图
    :param driver: 启动浏览器
    :param file_name: 截图文件名
    :return: 返回指定路径的截图文件
    """
    file_path = setting.TEST_REPORT + "/screenshot/" + file_name
    return driver.get_screenshot_as_file(file_path)
