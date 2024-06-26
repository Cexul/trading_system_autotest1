#! /usr/local/bin/python3.10
# coding=utf-8
# @Time: 2024/6/14 15:53
# @Author: xuliang

class AccountBase(object):
    def basic_info_avatar_input(self):
        """
        基本资料，个人头像
        :return:
        """
        return "//input[@type='file']"

    def basic_info_save_button(self):
        """
        基本资料，保存按钮
        :return:
        """
        return "//span[text()='保存']//parent::button"

    def top_right_corner_avatar(self):
        """
        获取左上角头像定位
        :return:
        """
        return "//span[@role='button']"

    def avatar_user_quit_button(self):
        """
        头像里退出登录
        :return:
        """
        return "//li[text()='退出登录']"