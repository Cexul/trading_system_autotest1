#! /usr/local/bin/python3.10
# coding=utf-8
# @Time: 2024/6/14 16:45
# @Author: xuliang

import time

from config.driver_config import DriverConfig
from page.LoginPage import LoginPage
from page.LeftMenuPage import LeftMenuPage
from page.IframeBaiduMapPage import IframeBaiduMapPage


class TestIframeBaiduMap(object):
    def test_iframe_baidu_map(self):
        driver = DriverConfig().driver_config()
        LoginPage().login(driver, 'jay')
        time.sleep(3)
        LeftMenuPage().click_level_one_menu(driver, 'iframe测试')
        time.sleep(2)
        IframeBaiduMapPage().switch_2_baidu_map_iframe(driver)
        IframeBaiduMapPage().get_baidu_map_search_button(driver)
        IframeBaiduMapPage().iframw_out(driver)
        time.sleep(3)
        LeftMenuPage().click_level_one_menu(driver, '首页')
        time.sleep(3)
        driver.close()
