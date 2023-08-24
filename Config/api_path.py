# -*- coding: utf-8 -*-
# @File    :api_path
# @Date    :2023/4/20 16:25
# @Name    :LYP

from tools.operate_config import OperateConfig
from urllib.parse import urljoin

class ApiPath:

    '''管理api地址'''

    def __init__(self,env=None):
        if env is None:
            self.env = OperateConfig().get_node_value('ENV', 'env')
        else:
            self.env = env
        self.api_url = OperateConfig().get_node_value(self.env,'api_url') # 读取配置文件config.ini的系统域名
        self.y_api_url = OperateConfig().get_node_value(self.env, 'y_api_url') # 读取配置文件config.ini的一号项目接口域名

        ''' 
            *** 内部治理系统 *** 
            /*
            n_login_url：登录
            */
        '''
        self.n_login_url = urljoin(self.api_url, "/service-user/user_info/login") # 登录

        ''' 
            *** 数据平台系统 *** 
            /*
            w_login_url: 登录功能
            w_roleResourceIDs_url: 角色资源
            w_roleIndexIDs_url: 菜单资源
            w_getAllIframe_url: 帆软资源
            w_getDownListByRole_url: 资源下载列表
            w_top_menu_url: 一级菜单
            w_get_current_customer_url: 机构信息
            w_detail_url: 账号信息
            w_getOneByPlatform_url: 获取系统公告信息
            w_getObj_url:
            w_announcement_config_url: 公告文案
            w_data_user_detail_permission_url: 用户详细信息
            w_get_model_tree_url:
            w_zjsc_url:
            w_zqlxy_url:
            w_zjlx_zdh_url:
            w_sellWay_url: 销售方式
            w_area_tree_url: 城市区县信息
            w_dealState_url: 土地交易状态
            w_landUse_url: 土地用途
            w_get_flock_url: 城市详细信息
            w_time_url: 时间维度
            w_singleSelectProvince_url: 省份
            w_tagTree_url: 指标树
            w_echarts_url: 
            w_mapList_url: 区域内指标信息
            w_dataArea_url: 区域信息
            */
        '''
        self.w_login_url = urljoin(self.api_url, "/service-user/user_info/login")
        self.w_roleResourceIDs_url = urljoin(self.api_url, "/service-user/data_sys_resource_info/roleResourceIDs")
        self.w_roleIndexIDs_url = urljoin(self.api_url, "/service-user/data_sys_resource_info/roleIndexIDs")
        self.w_getAllIframe_url = urljoin(self.api_url, "/service-insight/index_open/getAllIframe")
        self.w_getDownListByRole_url = urljoin(self.api_url, "/service-user/data_sys_resource_info/getDownListByRole")
        self.w_top_menu_url = urljoin(self.api_url, "/service-insight/my_info/top_menu")
        self.w_get_current_customer_url = urljoin(self.api_url, "/service-user/data_sys_customers/get_current_customer")
        self.w_detail_url = urljoin(self.api_url, "/service-user/data_user_info/detail")
        self.w_getOneByPlatform_url = urljoin(self.api_url, "/service-website/sysAnnouncement/getOneByPlatform")
        self.w_getObj_url = urljoin(self.api_url, "/service-user/user_info/getObj")
        self.w_announcement_config_url = urljoin(self.api_url, "/service-insight/announcement/announcement_config")
        self.w_data_user_detail_permission_url = urljoin(self.api_url,"/service-user/data_sys_customers/data_user_detail_permission")
        self.w_get_model_tree_url = urljoin(self.api_url, "/service-insight/index_open/get_model_tree")
        self.w_zjsc_url = urljoin(self.api_url, "/service-insight/finance_jnz/zjsc")
        self.w_zqlxy_url = urljoin(self.api_url, "/service-insight/finance_jnz/zqlxy")
        self.w_zjlx_zdh_url = urljoin(self.api_url, "/service-insight/finance_jnz/zjlx_zdh")
        self.w_sellWay_url = urljoin(self.api_url, "/service-insight/land_dim/sellWay")
        self.w_area_tree_url = urljoin(self.api_url, "/service-insight/land_dim/area_tree")
        self.w_dealState_url = urljoin(self.api_url, "/service-insight/land_dim/dealState")
        self.w_landUse_url = urljoin(self.api_url, "/service-insight/land_dim/landUse")
        self.w_get_flock_url = urljoin(self.api_url, "/service-insight/land_flock_area/get_flock")
        self.w_time_url = urljoin(self.api_url, "/service-insight/land_dim/time")
        self.w_singleSelectProvince_url = urljoin(self.api_url, "/service-insight/land_dim/singleSelectProvince")
        self.w_tagTree_url = urljoin(self.api_url, "/service-insight/macroeconomy/data/tagTree")
        self.w_echarts_url = urljoin(self.api_url, "/service-insight/macroeconomy/data/echarts")
        self.w_mapList_url = urljoin(self.api_url, "/service-insight/macroeconomy/data/map/list")
        self.w_dataArea_url = urljoin(self.api_url, "/service-insight/macroeconomy/data/area")

        ''' 
        *** 一号项目 *** 
        /*
        y_login_url：登录
        */
    '''
        self.y_login_url = urljoin(self.y_api_url, "/gt/sys/login/auth")