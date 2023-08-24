# -*- coding: utf-8 -*-
# @File    :get_headerjson
# @Date    :2023/4/20 17:17
# @Name    :LYP

import os
from Config.setting import CASE_DATA_PATH
from tools.operate_json import OperationJson
from tools.operate_config import OperateConfig

class GetHeaderjson:

    def __init__(self,env=None):
        if env is not None:
            self.env = env
        else:
            self.env = OperateConfig().get_node_value('ENV', 'env')
        self.headers_json = os.path.join(CASE_DATA_PATH, "headers.json")

    def get_login_n_headers(self):
        return OperationJson(self.headers_json).key_get_data(self.env, "login_n_headers")

    def get_n_headers(self):
        return OperationJson(self.headers_json).key_get_data(self.env, "n_headers")

    def set_n_headers(self,s_token):
        OperationJson(self.headers_json).write_datas("Bearer " + s_token, self.env, "n_headers", "Authorization")

    def get_login_w_headers(self):
        return OperationJson(self.headers_json).key_get_data(self.env, "login_w_headers")

    def get_w_headers(self):
        return OperationJson(self.headers_json).key_get_data(self.env, "w_headers")

    def set_w_headers(self,s_token):
        OperationJson(self.headers_json).write_datas("Bearer " + s_token, self.env, "w_headers", "Authorization")

    def get_y_login_headers(self):
        return OperationJson(self.headers_json).key_get_data(self.env, "y_login_headers")

    def get_y_headers(self):
        return OperationJson(self.headers_json).key_get_data(self.env, "y_headers")

    def set_y_headers(self,s_token):
        OperationJson(self.headers_json).write_datas("Bearer " + s_token, self.env, "y_headers", "Authorization")