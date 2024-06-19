#! /usr/local/bin/python3.10
# coding=utf-8
# @Time: 2024/6/19 14:56
# @Author: xuliang

class TradingMarketBase(object):
    def search_input(self):
        """
        搜索宝贝输入框
        :return:
        """
        return "//div[text()='搜索宝贝']/following-sibling::input"

    def search(self):
        """
        搜索按钮
        :return:
        """
        # return "//div[text()='搜索宝贝']/following-sibling::div/button"
        return self.search_input() + "/following-sibling::div/button"

    def product_card(self, product_name):
        """
        商品卡片
        :param product_name:
        :return:
        """
        return "//div[text()='" + product_name + "']/ancestor::div[@class='el-card__body']"

    def i_want_button(self):
        """
        我想要按钮
        :return:
        """
        return "//span[text()='我想要']/parent::button"

    def receive_address(self):
        """
        收货地址
        :return:
        """
        return "//input[@placeholder='收货地址']"

    def receive_address_detail(self, num, address=None):
        """
        具体的收货地址
        :param num:
        :param address:
        :return:
        """
        if address:
            return "//span[text()='" + address + "']/parent::li"
        else:
            return "//ul[contains(@class,'list')]/li['" + str(num) + "']"

    def bottom_confirm(self):
        """
        确定按钮
        :return:
        """
        return "//span[text()='确 定']/parent::button"
