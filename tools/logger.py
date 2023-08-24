# -*- coding: utf-8 -*-
# @File    :logger
# @Date    :2023/4/20 15:45
# @Name    :LYP

from loguru import logger
from datetime import datetime
from Config.setting import os, LOG_PATH


class Logger:
    '''
    loguru封装日志记录器
    '''

    def __new__(cls, *args, **kwargs):
        '''
        1.os.path.abspath 作用： 获取当前脚本的完整路径
        2.os.path.dirname 功能：去掉文件名，返回目录
        3.os.path.join() 连接两个或更多的路径名组件
        :param args:
        :param kwargs:
        :return:
        '''

        log_name = datetime.now().strftime("%Y-%m-%d")    # 以时间命名日志文件，格式为"年-月-日"
        sink = os.path.join(LOG_PATH,"{}.log".format(log_name)) # 日志记录文件路径
        level = "DEBUG"  # 记录的最低日志级别为DEBUG
        encoding = "utf-8"  # 写入日志文件时编码格式为utf-8
        enqueue = True # 多线程多进程时保证线程安全
        rotation = "500MB" # 日志文件最大为500MB，超过则新建文件记录日志
        retention = "1 week"    # 日志保留时长为一星期，超时则清除
        logger.add(
            sink=sink, level=level, encoding=encoding,
            enqueue=enqueue, rotation=rotation, retention=retention
        )
        return logger


log = Logger()