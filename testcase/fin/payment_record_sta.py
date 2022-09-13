#!python3.9
# -*- coding: utf-8 -*-
# ---
# @Software: PyCharm
# @File: payment_record_sta.py
# @Author: feip
# @Site: 
# @Time: 17:28,9月 09, 2022
# ---
import os,sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import unittest,ddt,yaml
from config import setting
from public.models import myunit
from public.page_obj.fin.payment_record_page import payment_record
from public.page_obj.admin.dhl_loginPage import dhl_login
from public.models.log import Log

f_login = open(setting.ADMIN_TEST_DATA_YAML + '/' + 'dhl_login_data.yaml',encoding='utf-8')
LoginData = yaml.load(f_login)
ph = LoginData[2]['data']['phone']
pwd = LoginData[2]['data']['password']
code = LoginData[2]['data']['code']

try:
    f_payment_record =open(setting.FIN_TEST_DATA_YAML + '/' + 'payment_record_data.yaml',encoding='utf-8')
    payment_recordData = yaml.load(f_payment_record)
except FileNotFoundError as file:
    log = Log()
    log.error("文件不存在：{0}".format(file))

@ddt.ddt
class Demo_UI(myunit.MyTest):
    """待付款账单支付"""
    def user_login_verify(self,phone,password,code):
        """
        用户登录
        :param phone: 手机号
        :param password: 密码
        :param code: 验证码
        :return:
        """
        dhl_login(self.driver).user_login(phone,password,code)
    #
    # def exit_login_check(self):
    #     """
    #     退出登录
    #     :return:
    #     """
    #     dhl_login(self.driver).login_exit()

    def payment_record_test(self,*args):
        payment_record(self.driver).user_payment_record(*args)

    # @ddt.data(*payment_recordData)
    def test_payment_record(self):
        """
        待付款账单支付
        :param datayaml: 加载login_data登录测试数据
        :return:
        """
        log = Log()
        # log.info("当前执行测试用例ID-> {0} ; 测试点-> {1}".format(datayaml['id'],datayaml['detail']))

        # 调用登录方法
        self.user_login_verify(ph,pwd,code)

        # 调用设置接口
        # self.onlinePay_test(datayaml['data']['name'],datayaml['data']['sign'])
        self.payment_record_test()

        po = payment_record(self.driver)

if __name__=='__main__':
    unittest.main()
