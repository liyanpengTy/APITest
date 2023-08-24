# -*- coding: utf-8 -*-
# @File    :setting
# @Date    :2023/4/20 15:48
# @Name    :LYP

import os

""" 文件存放路径 """

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

REPORT_PATH = os.path.join(BASE_PATH,'report') #报告存放的目录

CASE_PATH = os.path.join(BASE_PATH,'testCase') #测试用例的目录

CASE_DATA_PATH = os.path.join(BASE_PATH,'Data') #测试数据的目录

LOG_PATH = os.path.join(BASE_PATH,"log")

CONFIG_FILE = os.path.join(BASE_PATH,'Config','config.ini') #配置文件的目录

LOGIN_DATA_YAML_FILE = os.path.join(BASE_PATH, 'Data', 'userInfo.yaml') #配置文件的目录