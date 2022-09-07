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
from public.page_obj.ops.applyMaterialsALL import applyMaterialsALL

f_login = open(setting.ADMIN_TEST_DATA_YAML + '/' + 'dhl_login_data.yaml',encoding='utf-8')
LoginData = yaml.load(f_login)
ph = LoginData[2]['data']['phone']
pwd = LoginData[2]['data']['password']
code = LoginData[2]['data']['code']

try:
    f_applyMaterials =open(setting.OPS_TEST_DATA_YAML + '/' + 'applyMaterialsALL_data.yaml',encoding='utf-8')
    applyMaterialsData = yaml.load(f_applyMaterials)
except FileNotFoundError as file:
    log = Log()
    log.error("文件不存在：{0}".format(file))

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

    def exit_login_check(self):
        """
        退出登录
        :return:
        """
        dhl_login(self.driver).login_exit()
    def applyMaterialsTest_verify(self,*args):

        applyMaterialsALL(self.driver).applyMaterialsTestALL(*args)

    @ddt.data(*applyMaterialsData)
    def test_applyMaterialsALL(self,datayaml):
        """
        物料申请
        :param datayaml: 加载测试数据
        :return:
        """
        log = Log()
        # 调用登录方法
        self.user_login_verify(ph, pwd, code)
        log.info("当前执行测试用例ID-> {0} ; 测试点-> {1}".format(datayaml['id'], datayaml['detail']))
        self.applyMaterialsTest_verify(datayaml['data']['materialstype'])
        po = applyMaterialsALL(self.driver)


if __name__=='__main__':
    unittest.main()