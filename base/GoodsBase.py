#! /usr/local/bin/python3.10
# coding=utf-8
# @Time: 2024/6/14 12:15
# @Author: xuliang

class GoodsBase(object):

    def goods_title(self):
        """
        商品标题
        :return:
        """
        return "//form[@class='el-form']//textarea[@placeholder='请输入商品标题']"

    def goods_detail(self):
        """
        商品详情
        :return:
        """
        return "//form[@class='el-form']//textarea[@placeholder='请输入商品详情']"

    def goods_num(self, plus=True):
        """
        商品数量
        :param plus: 为True,使用+号，False使用数字
        :return:
        """
        if plus:
            return "//label[@for='product_stock']/following-sibling::div//i[@class='el-icon-plus']//parent::span"
        else:
            return "//label[@for='product_stock']/following-sibling::div//input[@placeholder='商品数量']"

    def goods_img(self):
        """
        商品图片
        :return:
        """
        return "//input[@type='file']"

    def goods_price(self):
        """
        商品单价
        :return:
        """
        return "//form[@class='el-form']//input[@placeholder='请输入商品单价']"

    def goods_status(self):
        """
        商品状态
        :return:
        """
        return "//form[@class='el-form']//input[@placeholder='请选择商品状态']"

    def goods_status_select(self, select_name):
        """
        选择商品状态
        :param select_name:
        :return:
        """
        return "//span[text()='" + select_name + "']//parent::li"

    def add_goods_bottom_button(self, button_name):
        """
        底部按钮
        :param button_name:
        :return:
        """
        return "//span[text()='" + button_name + "']//parent::button"
