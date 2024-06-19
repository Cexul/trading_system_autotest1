#! /usr/local/bin/python3.10
# coding=utf-8
# @Time: 2024/6/19 13:20
# @Author: xuliang

from selenium.webdriver.common.by import By

from base.HomeBase import HomeBase
from base.ObjectMap import ObjectMap


class HomePage(ObjectMap, HomeBase):

    def get_balance(self, driver):
        """
        获取首页的账户信息
        :param driver:
        :return:
        """
        balance_xpath = self.user_balance()
        return self.element_get(driver, By.XPATH, balance_xpath).text
