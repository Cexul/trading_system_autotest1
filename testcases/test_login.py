#! /usr/local/bin/python3.10
# coding=utf-8
# @Time: 2024/6/12 17:32
# @Author: xuliang
import time

import pytest

from page.LoginPage import LoginPage
from config.driver_config import DriverConfig
from common.report_add_img import add_img_2_report
import allure

class TestLogin(object):

    @pytest.mark.login
    @allure.feature('登录')
    @allure.description('登录')
    def test_login(self, driver):
        """使用错请的账号登录"""
        with allure.step('登录'):

            LoginPage().login(driver, 'chen')
            time.sleep(3)
            add_img_2_report(driver,'登录',need_sleep=False)


