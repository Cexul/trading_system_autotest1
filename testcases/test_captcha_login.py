#! /usr/local/bin/python3.10
# coding=utf-8
# @Time: 2024/6/19 11:35
# @Author: xuliang
import time

import pytest

from page.LoginPage import LoginPage
from config.driver_config import DriverConfig
from common.report_add_img import add_img_2_report
import allure


class TestCaptchaLogin(object):
    @pytest.mark.login
    @allure.feature('登录')
    @allure.description('验证码登录')
    def test_captcha_login(self, driver):
        """验证码登录"""
        with allure.step('登录'):
            LoginPage().login(driver, 'jay', need_captcha=True)
            time.sleep(3)
            add_img_2_report(driver, '验证码登录', need_sleep=False)
