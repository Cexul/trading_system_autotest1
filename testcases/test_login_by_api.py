#! /usr/local/bin/python3.10
# coding=utf-8
# @Time: 2024/6/19 12:18
# @Author: xuliang
import time

import pytest

from page.LoginPage import LoginPage
from common.report_add_img import add_img_2_report
import allure


class TestLoginByApi(object):
    @pytest.mark.login
    @allure.feature('api登录')
    @allure.description('api登录')
    def test_login_by_api(self, driver):
        """api登录"""
        with allure.step('登录jay'):
            LoginPage().api_login(driver, 'jay')
            time.sleep(3)

        with allure.step('切换用户到will'):
            LoginPage().api_login(driver, 'william')
            time.sleep(3)
