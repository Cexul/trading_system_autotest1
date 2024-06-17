#! /usr/local/bin/python3.10
# coding=utf-8
# @Time: 2024/6/12 17:32
# @Author: xuliang
import time

from page.LoginPage import LoginPage
from config.driver_config import DriverConfig


class TestLogin(object):

    def test_login(self):
        driver = DriverConfig().driver_config()
        # driver.get('http://www.tcpjwtester.top')
        # time.sleep(3)
        # LoginPage().login_input_value(driver,'用户名','周杰伦')
        # time.sleep(1)
        # LoginPage().login_input_value(driver,'密码','1234abcd!')
        # time.sleep(2)
        # LoginPage().click_login(driver,'登录')
        # time.sleep(1)
        LoginPage().login(driver,'jay')
        time.sleep(3)
        driver.close()