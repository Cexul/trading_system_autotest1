#! /usr/local/bin/python3.10
# coding=utf-8
# @Time: 2024/6/14 16:29
# @Author: xuliang

import time

from page.ExternalLinkPage import ExternalLinkPage
from page.LeftMenuPage import LeftMenuPage
from config.driver_config import DriverConfig
from page.LoginPage import LoginPage
import allure
from common.report_add_img import add_img_2_report


class TestWindowHandle(object):

    @allure.description('窗口句柄')
    @allure.epic('窗口句柄epic')
    @allure.feature('窗口句柄feature')
    @allure.story('窗口句柄story')
    @allure.tag('窗口句柄tag')
    def test_switch_window_handles(self, driver):
        with allure.step('登录'):
            LoginPage().login(driver, 'jay')
            time.sleep(2)
            add_img_2_report(driver,'登录')

        with allure.step('点击外部链接'):
            LeftMenuPage().click_level_one_menu(driver, '外链')
            time.sleep(1)
            # add_img_2_report(driver,'点击外部链接')


        with allure.step('断言title'):
            title = ExternalLinkPage().goto_imooc(driver)
            print(title)
            assert title == '慕课网-程序员的梦工厂'
