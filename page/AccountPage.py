#! /usr/local/bin/python3.10
# coding=utf-8
# @Time: 2024/6/14 15:59
# @Author: xuliang

import time

from selenium.webdriver.common.by import By

from base.AccountBase import AccountBase
from base.ObjectMap import ObjectMap
from common.tools import get_img_path


class AccountPage(AccountBase, ObjectMap):

    def upload_avatar(self, driver, img_name):
        """
        上传个人头像
        :param driver:
        :param img_name:
        :return:
        """
        img_path = get_img_path(img_name)
        upload_xpath = self.basic_info_avatar_input()
        return self.upload(driver, By.XPATH, upload_xpath, img_path)

    def click_save(self, driver):
        """
        点击保存按钮
        :param driver:
        :return:
        """
        button_xpath = self.basic_info_save_button()
        return self.element_click(driver, By.XPATH, button_xpath)

    def top_right_corner_avatar_mouse_hover(self,driver):
        """
        右上角头像鼠标悬停
        :param driver:
        :return:
        """
        avatar_xpath = self.top_right_corner_avatar()
        return self.mouse_hover(driver,By.XPATH,avatar_xpath)

    def user_logOut(self,driver):
        """
        用户头像logOut
        :param driver:
        :return:
        """
        button_xpath = self.avatar_user_quit_button()
        return self.element_click(driver,By.XPATH,button_xpath)
