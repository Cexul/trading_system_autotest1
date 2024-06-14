#! /usr/local/bin/python3.10
# coding=utf-8
# @Time: 2024/6/14 16:40
# @Author: xuliang

from selenium.webdriver.common.by import By

from base.IframeBaiduMapBase import IframeBaiduMapBase
from base.ObjectMap import ObjectMap


class IframeBaiduMapPage(IframeBaiduMapBase, ObjectMap):

    def get_baidu_map_search_button(self, driver):
        """
        获取百度地图搜索按钮
        :param driver:
        :return:
        """
        button_xpath = self.search_button()
        return self.element_click(driver, By.XPATH, button_xpath)

    def switch_2_baidu_map_iframe(self,driver):
        """
        切换到百度地图的iframe
        :param driver:
        :return:
        """
        iframe_xpath = self.baidu_map_iframe()
        return self.switch_into_iframe(driver,By.XPATH,iframe_xpath)

    def iframw_out(self,driver):
        """
        从百度地图切换回来
        :param driver:
        :return:
        """
        return self.switch_from_iframe_to_content(driver)