# -*- coding: utf-8 -*-
# @File    :get_wjson
# @Date    :2023/4/21 11:26
# @Name    :LYP

import os
from Config.setting import CASE_DATA_PATH
from tools.operate_json import OperationJson
from tools.operate_config import OperateConfig

class GetWJson:

    def __init__(self,env=None):
        if env is not None:
            self.env = env
        else:
            self.env = OperateConfig().get_node_value('ENV', 'env')
        self.variable_json = os.path.join(CASE_DATA_PATH, "w.json")

    def get_w_user_information(self):
        return OperationJson(self.variable_json).key_get_data(self.env, "w_user_information")

    def set_w_user_information_userId(self, userId):
        OperationJson(self.variable_json).write_datas(userId, self.env, "w_user_information", "userId")