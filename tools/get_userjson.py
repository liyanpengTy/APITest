# -*- coding: utf-8 -*-
# @File    :get_userjson
# @Date    :2023/4/20 17:05
# @Name    :LYP

from tools.operate_config import get_yaml,OperateConfig

class GetuserJson:

    def __init__(self, env=None):
        if env is None:
            env = OperateConfig().get_node_value('ENV', 'env')
        self.env = env
        self.user_info = get_yaml(self.env)

    # 内部治理系统 登陆的用户信息
    def  get_n_login_info(self):
        n_login_info = self.user_info['n_login_info']
        return n_login_info

    # 数据平台系统 登陆的用户信息
    def  get_w_login_info(self):
        w_login_info = self.user_info['w_login_info']
        return w_login_info

    # 一号项目 登录的用户信息
    def get_y_login_info(self):
        y_login_info = self.user_info['y_login_info']
        return y_login_info
