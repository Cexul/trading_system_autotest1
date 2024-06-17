#! /usr/local/bin/python3.10
# coding=utf-8
# @Time: 2024/6/14 15:45
# @Author: xuliang

import time

import pytest

from config.driver_config import DriverConfig
from page.LoginPage import LoginPage
from page.LeftMenuPage import LeftMenuPage
from page.OrderPage import OrderPage

tab_list = ['全部', '待付款', '待发货', '运输中', '待确认', '待评价']
# tab_list = ['全部', '待付款']


class TestOrderBuy(object):
    @pytest.mark.parametrize('tab', tab_list)
    def test_order_buy(self, driver, tab):
        # driver = DriverConfig().driver_config()
        LoginPage().login(driver, 'jay')
        LeftMenuPage().click_level_one_menu(driver, '我的订单')
        time.sleep(1)
        LeftMenuPage().click_level_two_menu(driver, '已买到的宝贝')
        time.sleep(1)
        OrderPage().click_order_tab(driver, tab)
        time.sleep(2)
        # tab_list = ['全部', '待付款', '待发货', '运输中', '待确认', '待评价']
        # for tab in tab_list:
        #     OrderPage().click_order_tab(driver, tab)
        #     time.sleep(2)
        # driver.quit()
