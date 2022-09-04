#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = 'Zhaoyj'

import os, sys

from public.models.sendmail import send_mail
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import unittest, ddt, yaml
from config import setting
from public.models import myunit, screenshot
from public.page_obj.dhl_loginPage import dhl_login
from public.models.log import Log

try:
    f = open(setting.TEST_DATA_YAML + '/' + 'dhl_login_data.yaml', encoding='utf-8')
    testData = yaml.load(f)
except FileNotFoundError as file:
    log = Log()
    log.error("文件不存在：{0}".format(file))


@ddt.ddt
class Demo_UI(myunit.MyTest):
    """5idhl登录功能模块自检测试"""

    def user_login_verify(self, phone, password, code):
        """
        用户登录
        :param phone: 手机号
        :param password: 密码
        :param code: 验证码
        :return:
        """
        dhl_login(self.driver).user_login(phone, password, code)

    # def exit_login_check(self):
    #     """
    #     退出登录
    #     :return:
    #     """
    #     login(self.driver).login_exit()

    @ddt.data(*testData)
    def test_login(self, datayaml):
        """
        登录测试
        :param datayaml: 加载login_data登录测试数据
        :return:
        """
        log = Log()
        log.info("当前执行测试用例ID-> {0} ; 测试点-> {1}".format(datayaml['id'], datayaml['detail']))
        # 调用登录方法
        self.user_login_verify(datayaml['data']['phone'], datayaml['data']['password'], datayaml['data']['code'])
        po = dhl_login(self.driver)


if __name__ == '__main__':
    unittest.main()
