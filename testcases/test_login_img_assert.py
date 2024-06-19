#! /usr/local/bin/python3.10
# coding=utf-8
# @Time: 2024/6/18 11:04
# @Author: xuliang
import time

import allure
import pytest
from page.LoginPage import LoginPage
from common.report_add_img import add_img_2_report


class TestLoginAssert(object):
    @pytest.mark.login
    @allure.feature('登录')
    @allure.description('登录后断言图片')
    def test_login_assert(self, driver):
        """登录后断言图片"""
        with allure.step('登录'):
            LoginPage().login(driver, 'jay')
            time.sleep(2)
            add_img_2_report(driver, '登录')

        with allure.step('断言图片'):
            assert LoginPage().login_assert(driver, 'head_img.png') > 0.9
