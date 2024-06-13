#! /usr/local/bin/python3.10
# coding=utf-8
# @Time: 2024/6/13 10:53
# @Author: xuliang

class HomeBase(object):

    def wallet_switch(self):
        """
        首页的钱包开关
        :return:
        """
        return "//span[contains(@class,'switch')]"

    def logo(self):
        """
        进入系统后，首页左上角logo
        :return:
        """
        return "//div[contain(text(),'二手')]"

    def welcome(self):
        """
        首页欢迎您回来
        :return:
        """
        return "//span[starts-with(text(),'欢迎您回来')]"

    def show_date(self):
        """
        首页显示日期
        :return:
        """
        return "//div[text()='我的日历']/following-sibling::div"