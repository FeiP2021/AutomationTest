__author__ = 'gaoth'

import os, sys

from public.models.sendmail import send_mail

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import unittest, ddt, yaml
from config import setting
from public.models import myunit, screenshot
from public.page_obj.dhl_holidaypage import dhl_holiday
from public.models.log import Log

try:
    f = open(setting.TEST_DATA_YAML + '/' + 'holiday_data.yaml', encoding='utf-8')
    testData = yaml.load(f)
except FileNotFoundError as file:
    log = Log()
    log.error("文件不存在：{0}".format(file))


@ddt.ddt
class Demo_holiday1(myunit.MyTest):
    """各国节假日查询"""

    def user_holiday_verify(self, country):
        """
        用户登录
        :param country:国家
        :return:
        """
        dhl_holiday(self.driver).user_holiday()


    @ddt.data(*testData)
    def test_holiday(self, datayaml):
        """
        登录测试
        :param datayaml: 加载login_data登录测试数据
        :return:
        """
        log = Log()
        log.info("当前执行测试用例ID-> {0} ; 测试点-> {1}".format(datayaml['id'], datayaml['detail']))
        # 调用登录方法
        self.user_holiday_verify(datayaml['data'])
        po = dhl_holiday(self.driver)


if __name__ == '__main__':
    unittest.main()
