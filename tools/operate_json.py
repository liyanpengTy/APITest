# -*- coding: utf-8 -*-
# @File    :operate_json
# @Date    :2023/4/20 15:59
# @Name    :LYP

import os
import json
from Config.setting import CASE_DATA_PATH

data_path = os.path.join(CASE_DATA_PATH, "test.json")

class OperationJson:
    def __init__(self, file_names=None):
        if file_names:
            self.file_name = file_names
        else:
            self.file_name = data_path

    def open_json(self):
        """打开json文件
        :return:返回json文件数据
        """
        with open(self.file_name, 'r',encoding='utf-8') as fp:
            data = json.load(fp)
            return data
            fp.close()

    def key_get_data(self, key1, key2=None, key3=None):
        """通过key值获取数据
        :param key1:
        :param key2:
        :return:
        """
        if key2 is None:
            data = self.open_json()[key1]
        elif key3 is None:
            data = self.open_json()[key1][key2]
        else:
            data = self.open_json()[key1][key2][key3]
        return data

    def write_data(self, w_data, key1, key2=None):
        """修改json数据
        :param w_data: 修改后的数据
        :param key1: 要修改的键值1
        :param key2: 要修改的键值2
        :return:
        """
        data_dict = self.open_json()
        if key2 is None:
            data_dict[key1] = w_data
        else:
            data_dict[key1][key2] = w_data
        with open(self.file_name, 'w',encoding='utf-8') as fp:
            fp.write(json.dumps(data_dict, ensure_ascii=False, sort_keys=False, indent=2))  # 对写入的json数据进行格式化
            fp.close()

    def write_datas(self, w_data, key1, key2, key3=None):
        """修改json数据
        :param w_data: 修改后的数据
        :param key1: 要修改的键值1
        :param key2: 要修改的键值2
        :param key3: 要修改的键值3
        :return:
        """
        data_dict = self.open_json()
        if key3 is None and key2 is None:
            data_dict[key1] = w_data
        elif key3 is None and key2 is not None:
            data_dict[key1][key2] = w_data
        else:
            data_dict[key1][key2][key3] = w_data
        with open(self.file_name, 'w',encoding='utf-8') as fp:
            fp.write(json.dumps(data_dict, ensure_ascii=False, sort_keys=False, indent=2))  # 对写入的json数据进行格式化
            fp.close()


if __name__ == "__main__":
    #file_name = "test.json"
    a = OperationJson()
    b = a.key_get_data("login_header")
    #print(type(b))
    print(b)