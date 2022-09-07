#!python3.9
# -*- coding: utf-8 -*-
# ---
# @Software: PyCharm
# @Author: zhaoyj
# @Site:
# @Time: 9月 07, 2022
# ---


import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)

# base配置文件
CONFIG_DIR = os.path.join(BASE_DIR,"database","user.ini")
# 测试报告目录
TEST_REPORT = os.path.join(BASE_DIR,"report")
# 日志目录
LOG_DIR = os.path.join(BASE_DIR,"logs")

# 全部测试用例目录
TEST_DIR = os.path.join(BASE_DIR,"testcase")


# admin
# 测试用例目录
ADMIN_TEST_DIR = os.path.join(BASE_DIR,"testcase/admin")
# 测试数据文件
ADMIN_TEST_DATA_YAML = os.path.join(BASE_DIR,"testdata/admin")
# 元素控件
ADMIN_TEST_Element_YAML = os.path.join(BASE_DIR,"testyaml/admin")

# csd
# 测试用例目录
CSD_TEST_DIR = os.path.join(BASE_DIR,"testcase/csd")
# 测试数据文件
CSD_TEST_DATA_YAML = os.path.join(BASE_DIR,"testdata/csd")
# 元素控件
CSD_TEST_Element_YAML = os.path.join(BASE_DIR,"testyaml/csd")

# fin
# 测试用例目录
FIN_TEST_DIR = os.path.join(BASE_DIR,"testcase/fin")
# 测试数据文件
FIN_TEST_DATA_YAML = os.path.join(BASE_DIR,"testdata/fin")
# 元素控件
FIN_TEST_Element_YAML = os.path.join(BASE_DIR,"testyaml/fin")

# ops
# 测试用例目录
OPS_TEST_DIR = os.path.join(BASE_DIR,"testcase/ops")
# 测试数据文件
OPS_TEST_DATA_YAML = os.path.join(BASE_DIR,"testdata/ops")
# 元素控件
OPS_TEST_Element_YAML = os.path.join(BASE_DIR,"testyaml/ops")