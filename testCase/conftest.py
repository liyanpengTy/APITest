# -*- coding: utf-8 -*-
# @File    :conftest
# @Date    :2023/4/20 17:39
# @Name    :LYP

import pytest
from Config.api_path import ApiPath
from tools.common import *
from tools.get_userjson import GetuserJson
from tools.get_variable import GetVariable
from tools.get_headerjson import GetHeaderjson

''' 处理登录：内部治理(n)、数据平台(y)、一号项目(Y)系统登录 '''

# 实例化对象
api_path = ApiPath()
get_userinfo = GetuserJson(None)
get_header = GetHeaderjson(None)
get_variable = GetVariable(None)

@pytest.fixture(scope="session",autouse=True)
def test_n_login():
    '''
        ***内部治理：用户名密码登录***
        /*
        调用api_path方法获取url；
        调用get_header方法获取内部治理的请求头；
        调用get_userinfo方法获取入参；
        调用Common类的r_post方法发起http请求，获取返回结果；
        调用get_header方法，将accessToken写入headers.json文件中
        */
    '''
    url = api_path.n_login_url
    headers = get_header.get_n_headers()
    data = get_userinfo.get_n_login_info()
    res_json = Common.r_post(url=url, headers=headers, json=data)
    get_header.set_n_headers(res_json["data"]["accessToken"])

@pytest.fixture(scope="session",autouse=True)
def test_w_login():
    '''
        ***数据平台：用户名密码登录***
        /*
        调用api_path方法获取url；
        调用get_header方法获取数据平台的请求头；
        调用get_userinfo方法获取入参；
        调用Common类的r_post方法发起http请求，获取返回结果；
        调用get_header方法，将accessToken写入headers.json文件中
        */
    '''
    url = api_path.w_login_url
    headers = get_header.get_w_headers()
    data = get_userinfo.get_w_login_info()
    res_json = Common.r_post(url=url, headers=headers, json=data)
    get_header.set_w_headers(res_json["data"]["accessToken"])
    get_variable.set_w_user_information_userId(res_json["data"]["userId"])
    get_variable.set_w_user_information_roleId(res_json["data"]["roleId"])

@pytest.fixture(scope="session",autouse=True)
def test_y_login():
    '''
        ***一号项目：用户名密码登录***
        /*
        调用api_path方法获取url；
        调用get_header方法获取一号项目的请求头；
        调用get_userinfo方法获取入参；
        调用Common类的r_post方法发起http请求，获取返回结果；
        调用get_header方法，将tk写入headers.json文件中
        */
    '''
    url = api_path.y_login_url
    headers = get_header.get_y_login_headers()
    data = get_userinfo.get_y_login_info()
    res_json = Common.r_post(url=url, headers=headers, json=data)
    get_header.set_y_headers(res_json["obj"]["tk"])
