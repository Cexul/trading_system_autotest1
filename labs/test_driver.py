#! /usr/local/bin/python3.10
# coding=utf-8
# @Time: 2024/6/12 16:17
# @Author: xuliang

from config.driver_config import DriverConfig

driver = DriverConfig().driver_config()
driver.get('www.baidu.com')
