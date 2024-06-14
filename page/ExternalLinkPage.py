#! /usr/local/bin/python3.10
# coding=utf-8
# @Time: 2024/6/14 16:27
# @Author: xuliang

from base.ObjectMap import ObjectMap


class ExternalLinkPage(ObjectMap):

    def goto_imooc(self, driver):
        """
        切换窗口到imooc
        :param driver:
        :return:
        """
        self.switch_window_2_lastest_handle(driver)
        return driver.title
