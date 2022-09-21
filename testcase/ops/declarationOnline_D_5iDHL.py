#!python3.9
# -*- coding: utf-8 -*-
# ---
# @Software: PyCharm
# @File: TestOnline.py
# @Author: feip
# @Site:
# @Time: 10:09,9月 20, 2022
# ---
#!python3.9
# -*- coding: utf-8 -*-
# ---
# @Software: PyCharm
# @File: declarationOnline_sta.py
# @Author: feip
# @Site:
# @Time: 10:43,9月 19, 2022
# ---
import os,sys

from public.page_obj.ops.createOrder_page import createOrder
from public.page_obj.ops.declarationOnline_D_page import declarationOnline_D

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import unittest,ddt,yaml
from config import setting
from public.models import myunit
from public.page_obj.ops.createOrder_page import createOrder
from public.page_obj.admin.dhl_loginPage import dhl_login
from public.models.log import Log


try:
    f_daily_lottery =open(setting.OPS_TEST_DATA_YAML + '/' + 'declarationOnline_D_data.yaml',encoding='utf-8')
    declarationOnline_D_Data = yaml.load(f_daily_lottery)
except FileNotFoundError as file:
    log = Log()
    log.error("文件不存在：{0}".format(file))

@ddt.ddt
class Demo_UI(myunit.MyTest):
    """在线申报"""
    def user_login_verify(self,phone,password,code):
        """
        用户登录
        :param phone: 手机号
        :param password: 密码
        :param code: 验证码
        :return:
        """
        dhl_login(self.driver).user_login(phone,password,code)

    def declarationOnline_D_user(self,*args):

        declarationOnline_D(self.driver).declarationOnline_D_user(*args)

    @ddt.data(*declarationOnline_D_Data)
    def test_declarationOnline_D(self,datayaml):
        """
        在线申报
        :param datayaml: 加载在线申报测试数据
        :return:
        """
        log = Log()
        log.info("当前执行测试用例ID-> {0} ; 测试点-> {1}".format(datayaml['id'],datayaml['detail']))
        # 调用登录方法
        self.user_login_verify('18734912442','asd123','pentestyz')
        self.declarationOnline_D_user()

if __name__=='__main__':
    unittest.main()