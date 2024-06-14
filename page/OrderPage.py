#! /usr/local/bin/python3.10
# coding=utf-8
# @Time: 2024/6/14 15:41
# @Author: xuliang

import time

from selenium.webdriver.common.by import By

from base.OrderBase import OrderBase
from base.ObjectMap import ObjectMap


class OrderPage(OrderBase, ObjectMap):

    def click_order_tab(self, driver, tab_name):
        """
        点击订单tab栏按钮
        :param driver:
        :param tab_name:
        :return:
        """
        tab_xpath = self.order_tab(tab_name)
        return self.element_click(driver, By.XPATH, tab_xpath)
