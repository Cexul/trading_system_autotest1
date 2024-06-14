#! /usr/local/bin/python3.10
# coding=utf-8
# @Time: 2024/6/14 15:36
# @Author: xuliang

class OrderBase(object):
    def order_tab(self, tab_name):
        """
        订单tab按钮
        :param tab_name:
        :return:
        """

        # return "//main[contains(@class,'el-main')]//div[text()='" + tab_name + "']"
        return "//div[@role='tab' and text()='" + tab_name + "']"
