#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = 'Zhaoyj'
import os,sys
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import unittest,ddt,yaml
from config import setting
from public.models import myunit,screenshot
from public.page_obj.onlinePayPage import onlinePay
from public.page_obj.dhl_loginPage import dhl_login
from public.models.log import Log

f_login = open(setting.TEST_DATA_YAML + '/' + 'dhl_login_data.yaml',encoding='utf-8')
LoginData = yaml.load(f_login)
ph = LoginData[2]['data']['phone']
pwd = LoginData[2]['data']['password']
code = LoginData[2]['data']['code']

try:
    f_onlinePay =open(setting.TEST_DATA_YAML + '/' + 'online_data.yaml',encoding='utf-8')
    onlinePayData = yaml.load(f_onlinePay)
except FileNotFoundError as file:
    log = Log()
    log.error("文件不存在：{0}".format(file))

@ddt.ddt
class Demo_UI(myunit.MyTest):
    """首页---设置"""
    def user_login_verify(self,phone,password,code):
        """
        用户登录
        :param phone: 手机号
        :param password: 密码
        :param code: 验证码
        :return:
        """
        dhl_login(self.driver).user_login(phone,password,code)

    # def exit_login_check(self):
    #     """
    #     退出登录
    #     :return:
    #     """
    #     dhl_login(self.driver).login_exit()

    def onlinePay_verify(self,*args):

        onlinePay(self.driver).onlinePay_Credit(*args)

    @ddt.data(*onlinePayData)
    def test_onlinePay(self,datayaml):
        """
        在线付款
        :param datayaml: 加载测试数据
        :return:
        """
        log = Log()
        # 调用登录方法
        self.user_login_verify(ph, pwd, code)
        log.info("当前执行测试用例ID-> {0} ; 测试点-> {1}".format(datayaml['id'], datayaml['detail']))
        self.onlinePay_verify(datayaml['data']['dhlCreditCode'], datayaml['data']['count'])

        po = onlinePay(self.driver)

if __name__=='__main__':
    unittest.main()