# -*- coding: utf-8 -*-
# @File    :operate_config
# @Date    :2023/4/20 15:53
# @Name    :LYP


import yaml
import configparser
from Config.setting import CONFIG_FILE,LOGIN_DATA_YAML_FILE

def get_yaml(goal):
    with open(LOGIN_DATA_YAML_FILE, encoding='utf-8') as f:
        yaml_log = yaml.load(f, Loader=yaml.FullLoader)
    goal_list = yaml_log.keys()
    if goal in goal_list:
        return yaml_log[goal]
    else:
        print('不存在的配置')

class OperateConfig:
    def __init__(self):
        self.config = configparser.ConfigParser()  # 调用外部的读取配置文件的方法
        self.config.read(CONFIG_FILE, encoding='GBK')

    def get_node_value(self,node, name):
        value = self.config.get(node, name)
        return value

    def set_node_value(self,section,node,name):
        """写入配置文件"""
        self.config.set(section,node,name)  # 修改指定section 的option
        self.config.write(open(CONFIG_FILE, 'w'))