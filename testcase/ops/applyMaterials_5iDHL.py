#!python3.9
# -*- coding: utf-8 -*-
# ---
# @Software: PyCharm
# @Author: zhaoyj
# @Site: 
# @Time: 9月 07, 2022
# ---
import unittest
import ddt
import yaml
from config import setting
from public.models import myunit
from public.models.log import Log
from public.page_obj.admin.dhl_loginPage import dhl_login
from public.page_obj.ops.applyMaterials import applyMaterials

f_login = open(setting.ADMIN_TEST_DATA_YAML + '/' + 'dhl_login_data.yaml',encoding='utf-8')
LoginData = yaml.load(f_login)
ph = LoginData[2]['data']['phone']
pwd = LoginData[2]['data']['password']
code = LoginData[2]['data']['code']

@ddt.ddt
class Demo_UI(myunit.MyTest):
    """物料申请"""
    def user_login_verify(self,phone,password,code):
        """
        用户登录
        :param phone: 手机号
        :param password: 密码
        :param code: 验证码
        :return:
        """
        dhl_login(self.driver).user_login(phone,password,code)

    def test_applyMaterials(self):
        """
        物料申请
        :return:
        """
        log = Log()
        # 调用登录方法
        self.user_login_verify(ph, pwd, code)
        applyMaterials(self.driver).applyMaterialsTest()
        po = applyMaterials(self.driver)

if __name__=='__main__':
    unittest.main()