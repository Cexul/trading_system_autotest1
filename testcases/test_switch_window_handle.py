#! /usr/local/bin/python3.10
# coding=utf-8
# @Time: 2024/6/14 16:29
# @Author: xuliang

import time

from page.ExternalLinkPage import ExternalLinkPage
from page.LeftMenuPage import LeftMenuPage
from config.driver_config import DriverConfig
from page.LoginPage import LoginPage


class TestWindowHandle(object):

    def test_switch_window_handles(self):
        driver = DriverConfig().driver_config()
        LoginPage().login(driver, 'jay')
        LeftMenuPage().click_level_one_menu(driver, '外链')
        time.sleep(3)
        title = ExternalLinkPage().goto_imooc(driver)
        print(title)
        driver.close()
