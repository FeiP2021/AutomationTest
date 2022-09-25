#!python3.9
# -*- coding: utf-8 -*-
# @Software: PyCharm
# @File: declare_CommonInfo_5iDHL.py
# @Author: zhaoyj
# @Time: 15:59,9月 25, 2022
# ---
import os,sys
from public.page_obj.ops.declare_info_page import declare_info
from public.page_obj.ops.declare_management_page import declare_management
from public.page_obj.ops.declare_platform_page import declare_platform
from public.page_obj.ops.declare_use_page import declare_use
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import unittest,ddt,yaml
from config import setting
from public.models import myunit
from public.page_obj.admin.dhl_loginPage import dhl_login
from public.models.log import Log
try:
    f_daily_lottery =open(setting.OPS_TEST_DATA_YAML + '/' + 'declare_management_data.yaml',encoding='utf-8')
    declare_management_Data = yaml.load(f_daily_lottery)
except FileNotFoundError as file:
    log = Log()
    log.error("文件不存在：{0}".format(file))
@ddt.ddt
class declarationOnline_CommonInfo_5iDHL(myunit.MyTest):
    """在线申报-常用申报信息"""
    def user_login_verify(self,phone,password,code):
        """
        用户登录
        :param phone: 手机号
        :param password: 密码
        :param code: 验证码
        :return:
        """
        dhl_login(self.driver).user_login(phone,password,code)

    def declare_management_user(self,*args):

        declare_management(self.driver).declare_management_user(*args)
    def declare_info_user(self,*args):

        declare_info(self.driver).declare_info_user(*args)
    def declare_platform_user(self,*args):

        declare_platform(self.driver).declare_platform_user(*args)
    def declare_use_user(self,*args):

        declare_use(self.driver).declare_use_user(*args)

    @ddt.data(*declare_management_Data)
    def test_declare_management(self,datayaml):
        """
        在线申报-常用申报信息（新增、修改、删除等）
        :param datayaml: 加载在线申报测试数据
        :return:
        """
        log = Log()
        log.info("当前执行测试用例ID-> {0} ; 测试点-> {1}".format(datayaml['id'],datayaml['detail']))
        # 调用登录方法
        self.user_login_verify('18734912442','asd123','pentestyz')
        self.declare_management_user()
        self.declare_info_user()
        self.declare_platform_user()
        self.declare_use_user()

if __name__=='__main__':
    unittest.main()