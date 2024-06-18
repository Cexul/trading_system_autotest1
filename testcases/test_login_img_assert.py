#! /usr/local/bin/python3.10
# coding=utf-8
# @Time: 2024/6/18 11:04
# @Author: xuliang
import time

import pytest
from page.LoginPage import LoginPage


class TestLoginAssert(object):
    @pytest.mark.login
    def test_login_assert(self,driver):
        """
        登录后断言图片
        :param driver:
        :return:
        """
        LoginPage().login(driver,'jay')
        time.sleep(2)
        assert LoginPage().login_assert(driver,'head_img.png') > 0.9

