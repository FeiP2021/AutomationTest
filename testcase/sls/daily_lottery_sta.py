#!python3.9
# -*- coding: utf-8 -*-
# ---
# @Software: PyCharm
# @File: daily_lottery_sta.py
# @Author: feip
# @Site: 
# @Time: 9月 09, 2022
# ---
import os,sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import unittest,ddt,yaml
from config import setting
from public.models import myunit
from public.page_obj.sls.daily_lottery_page import daily_lottery
from public.page_obj.admin.dhl_loginPage import dhl_login
from public.models.log import Log


try:
    f_daily_lottery =open(setting.SLS_TEST_DATA_YAML + '/' + 'daily_lottery_data.yaml',encoding='utf-8')
    daily_lotteryData = yaml.load(f_daily_lottery)
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

    def daily_lottery_test(self,*args):

        daily_lottery(self.driver).user_daily_lottery(*args)

    @ddt.data(*daily_lotteryData)
    def test_daily_lottery(self,datayaml):
        """
        首页---设置操作测试
        :param datayaml: 加载login_data登录测试数据
        :return:
        """
        log = Log()
        log.info("当前执行测试用例ID-> {0} ; 测试点-> {1}".format(datayaml['id'],datayaml['detail']))
        # 调用登录方法
        self.user_login_verify('18210853727','asd123','pentestyz')
        self.daily_lottery_test(datayaml['data']['comment'])
        po = daily_lottery(self.driver)

if __name__=='__main__':
    unittest.main()
