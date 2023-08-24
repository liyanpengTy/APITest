# -*- coding: utf-8 -*-
# @File    :test_w
# @Date    :2023/4/21 11:32
# @Name    :LYP

import allure
from tools.common import *
from tools.get_wjson import *
from Config.api_path import ApiPath
from tools.get_headerjson import *
from tools.get_variable import *

@allure.feature("数据平台业务")
@allure.story("客户管理")
class TestW:
    """
        *** 实例化对象 ***
        /*
        apiPath： 接口域名
        getHeaderjson： 请求头
        getWjson： 获取数据平台数据
        getVariable： 获取之前接口存储的数据
        */
    """
    apiPath = ApiPath()
    getHeaderjson = GetHeaderjson(None)
    getWjson = GetWJson(None)
    getVariable = GetVariable(None)

    @allure.title("case1：业务场景1")
    def test_customer(self):
        with allure.step("step1: 查询角色资源列表"):
            #
            res_json = Common.r_get_data(url=self.apiPath.w_roleResourceIDs_url,
                                         headers= self.getHeaderjson.get_w_headers(),
                                         par={'roleId': self.getVariable.get_w_user_information_roleId()})
            self.getVariable.set_w_user_information_roleResourceIDs(res_json["data"])


if __name__ == '__main__':
    unittest.main()