# -*- coding: utf-8 -*-
# @File    :get_variable
# @Date    :2023/4/21 10:28
# @Name    :LYP

import os
from Config.setting import CASE_DATA_PATH
from tools.operate_json import OperationJson
from tools.operate_config import OperateConfig

class GetVariable:

    def __init__(self,env=None):
        if env is not None:
            self.env = env
        else:
            self.env = OperateConfig().get_node_value('ENV', 'env')
        self.variable_json = os.path.join(CASE_DATA_PATH, "variable.json")

    # def get_n_user_information(self):
    #     return OperationJson(self.variable_json).key_get_data(self.env, "n_user_information")
    #
    # def get_w_user_information(self):
    #     return OperationJson(self.variable_json).key_get_data(self.env, "w_user_information")

    def get_w_user_information_userId(self):
        return OperationJson(self.variable_json).key_get_data(self.env, "w_user_information", "userId")

    def set_w_user_information_userId(self, userId):
        OperationJson(self.variable_json).write_datas(userId, self.env, "w_user_information", "userId")

    def get_w_user_information_roleId(self):
        return OperationJson(self.variable_json).key_get_data(self.env, "w_user_information", "roleId")

    def set_w_user_information_roleId(self, roleId):
        OperationJson(self.variable_json).write_datas(roleId, self.env, "w_user_information", "roleId")

    def get_w_user_information_roleResourceIDs(self):
        return OperationJson(self.variable_json).key_get_data(self.env, "w_user_information", "roleResourceIDs")

    def set_w_user_information_roleResourceIDs(self, roleResourceIDs):
        OperationJson(self.variable_json).write_datas(roleResourceIDs, self.env, "w_user_information", "roleResourceIDs")

    def get_w_user_information_roleIndexIDs(self):
        return OperationJson(self.variable_json).key_get_data(self.env, "w_user_information", "roleIndexIDs")

    def set_w_user_information_roleIndexIDs(self, roleIndexIDs):
        OperationJson(self.variable_json).write_datas(roleIndexIDs, self.env, "w_user_information", "roleIndexIDs")

    def get_w_user_information_userCustomerId(self):
        return OperationJson(self.variable_json).key_get_data(self.env, "w_user_information", "userCustomerId")

    def set_w_user_information_userCustomerId(self, userCustomerId):
        OperationJson(self.variable_json).write_datas(userCustomerId, self.env, "w_user_information", "userCustomerId")

    # def get_y_user_information(self):
    #     return OperationJson(self.variable_json).key_get_data(self.env, "y_user_information")