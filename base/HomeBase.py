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
        return "//div[contains(text(),'二手')]"

    def welcome(self):
        """
        首页欢迎您回来
        :return:
        """
        return "//span[starts-with(text(),'欢迎您回来')]"

    def show_date(self):
        """
        首页显示日期
        :return: following-sibling同级元素的下一级元素
        """
        return "//div[text()='我的日历']/following-sibling::div"

    def home_user_avatar(self):
        """
        首页用户头像大图
        :return: preceding-sibling同级元素的上一级元素，parent父级方法
        """
        return "//span[contains(text(),'欢迎您')]/parent::div/preceding-sibling::div//img"

    def home_user_avatar_2(self):
        """
        首页用户头像大图2
        :return: ancestor方法
        """
        return "//span[text()='我的地址']/ancestor::div[@class='first_card']/div[contains(@class,'avatar')]//img"

    def user_balance(self):
        """
        首页的账户余额
        :return:
        """
        return "//th[text()='账户余额']/parent::tr/following-sibling::tr/td[1]"
