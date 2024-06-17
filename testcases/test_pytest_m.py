#! /usr/local/bin/python3.10
# coding=utf-8
# @Time: 2024/6/17 10:17
# @Author: xuliang

import time
import pytest

from config.driver_config import DriverConfig

class TestPytestMClass:

    @pytest.fixture(scope='class')
    def scope_class(self):
        print('level class')

    @pytest.fixture(scope='function')
    def driver(self):
        get_driver = DriverConfig().driver_config()
        return get_driver

    @pytest.mark.bing
    def test_open_bing(self,driver,scope_class):

        driver.get('https://cn.bing.com')
        time.sleep(3)
        driver.close()

    @pytest.mark.baidu
    def test_open_baidu(self,driver,scope_class):
        # driver = DriverConfig().driver_config()
        driver.get('https://www.baidu.com')
        time.sleep(3)
        driver.close()