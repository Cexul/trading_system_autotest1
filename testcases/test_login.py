#! /usr/local/bin/python3.10
# coding=utf-8
# @Time: 2024/6/12 17:32
# @Author: xuliang
import time

from page.LoginPage import LoginPage
from config.driver_config import DriverConfig
import allure

class TestLogin(object):

    def test_login(self, driver):
        with allure.step('登录'):

            LoginPage().login(driver, 'jay')
            time.sleep(3)

