#! /usr/local/bin/python3.10
# coding=utf-8
# @Time: 2024/6/14 16:10
# @Author: xuliang

import time

from page.AccountPage import AccountPage
from page.LeftMenuPage import LeftMenuPage
from config.driver_config import DriverConfig
from page.LoginPage import LoginPage


class TestPersonalInfo(object):
    def test_upload_personal_avatar(self):
        driver = DriverConfig().driver_config()
        LoginPage().login(driver, 'jay')
        LeftMenuPage().click_level_one_menu(driver, '账户设置')
        time.sleep(1)
        LeftMenuPage().click_level_two_menu(driver, '个人资料')
        time.sleep(1)
        AccountPage().upload_avatar(driver, 'img2.jpeg')
        time.sleep(3)
        AccountPage().click_save(driver)
        time.sleep(3)
        driver.close()
