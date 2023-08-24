# -*- coding: utf-8 -*-
# @File    :test_config
# @Date    :2023/4/21 15:36
# @Name    :LYP

from tools.operate_config import OperateConfig

class TestConfig:
    def test_1(self):
        # 读取配置文件
        env = OperateConfig().get_node_value('ENV','env')
        print(env)

        # 修改配置文件，改成QA2
        OperateConfig().set_node_value('ENV','env','QA1')