#! /usr/local/bin/python3.10
# coding=utf-8
# @Time: 2024/6/17 11:49
# @Author: xuliang

import pytest

from config.driver_config import DriverConfig

@pytest.fixture()
def driver():
    get_driver = DriverConfig().driver_config()
    yield get_driver
    get_driver.quit()
