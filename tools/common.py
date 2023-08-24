# -*- coding: utf-8 -*-
# @File    :common
# @Date    :2023/4/20 15:43
# @Name    :LYP

import requests
from tools.logger import log


class Common:
    '''封装通用接口'''

    ''' request-post请求，适用Content-Type:application/x-www-form-urlencoded，即表单传参，类似some=data&xxx=xxx 的形式 '''
    def r_post_form(url,headers,data):
        log.info("请求地址：{}".format(url))
        log.info("请求参数为：{}".format(data))
        res = requests.post(url,headers=headers,data=data).json()
        log.info("响应结果为：{}".format(res))
        return res

    ''' request-post请求，适用'Content-Type': 'application/json'，即json传参 '''
    def r_post(url,headers,json):
        log.info("请求地址：{}".format(url))
        log.info("请求参数为：{}".format(json))
        res = requests.post(url,headers=headers,json=json).json()
        log.info("响应结果为：{}".format(res))
        return res

    ''' request-post请求，适用'Content-Type': 'application/json'，即json传参——请求时不转换成json，适配s统一登录系统接口请求 '''
    def r_s_post(url, headers, json):
        log.info("请求地址：{}".format(url))
        log.info("请求参数为：{}".format(json))
        res = requests.post(url, headers=headers, json=json).json()
        log.info("响应结果为：{}".format(res.text))
        return res

    ''' request-get请求 '''
    def r_get(url, heasers, json):
        log.info("请求地址：{}".format(url))
        log.info("请求参数为：{}".format(json))
        res = requests.get(url,headers=heasers,json=json).json()
        log.info("响应结果为：{}".format(res))
        return res

    def r_get_data(url, headers, par):
        log.info("请求地址：{}".format(url))
        log.info("请求参数为：{}".format(par))
        res = requests.get(url, headers=headers, params=par).json()
        log.info("响应结果为：{}".format(res))
        return res

    # ''' 断言：统一登录系统的message=操作成功 '''
    # def assert_s_code_message(res_json):
    #     code = res_json['code']
    #     message = res_json['message']
    #     assert code == '200' and message == '操作成功'
    #
    # ''' 断言：业务系统的message=请求成功 '''
    # def assert_tg_code_message(res_json):
    #     code = res_json['code']
    #     message = res_json['message']
    #     assert code == '200' and message == '请求成功'