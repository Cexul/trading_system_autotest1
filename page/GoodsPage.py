#! /usr/local/bin/python3.10
# coding=utf-8
# @Time: 2024/6/14 12:52
# @Author: xuliang
import time

from selenium.webdriver.common.by import By

from base.GoodsBase import GoodsBase
from base.ObjectMap import ObjectMap
from common.tools import get_img_path


class GoodsPage(GoodsBase, ObjectMap):
    def input_goods_title(self, driver, input_value):
        """
        输入商品标题
        :param driver:
        :param input_value:
        :return:
        """
        goods_title_xpath = self.goods_title()
        return self.element_fill_value(driver, By.XPATH, goods_title_xpath, input_value)

    def input_goods_details(self, driver, input_value):
        """
        输入商品详情
        :param drvier:
        :param input_value:
        :return:
        """
        goods_details_xpath = self.goods_detail()
        return self.element_fill_value(driver, By.XPATH, goods_details_xpath, input_value)

    def select_goods_num(self, driver, num):
        """
        选择商品数量
        :param driver:
        :param num:
        :return:
        """
        goods_num_add_xpath = self.goods_num(plus=True)
        for i in range(num):
            self.element_click(driver, By.XPATH, goods_num_add_xpath)
            time.sleep(0.5)

    def upload_goods_img(self, driver, img_name):
        """
        上传图片
        :param driver:
        :param img_name:
        :return:
        """
        img_path = get_img_path(img_name)
        upload_xpath = self.goods_img()
        return self.upload(driver, By.XPATH, upload_xpath, img_path)

    def input_goods_price(self, driver, input_value):
        """
        输入商品单价
        :param driver:
        :param input_value:
        :return:
        """
        goods_price_xpath = self.goods_price()
        return self.element_fill_value(driver, By.XPATH, goods_price_xpath, input_value)

    def select_goods_status(self, driver, select_name):
        """
        选择商品状态
        :param driver:
        :param select_name: 上架还是下架
        :return:
        """
        goods_status_xpath = self.goods_status()
        self.element_click(driver, By.XPATH, goods_status_xpath)
        time.sleep(1)
        goods_status_select_xpath = self.goods_status_select(select_name)
        return self.element_click(driver, By.XPATH, goods_status_select_xpath)

    def click_bottom_button(self, driver, button_name):
        """
        点击底部按钮
        :param driver:
        :param button_name:
        :return:
        """
        button_xpth = self.add_goods_bottom_button(button_name)
        return self.element_click(driver, By.XPATH, button_xpth)

    def add_new_goods(
            self,
            driver,
            goods_title,
            goods_detail,
            goods_num,
            goods_pic_list,
            goods_price,
            goods_status,
            bottom_button_name
    ):
        """
        新增二手商品
        :param driver:
        :param goods_title:
        :param goods_detail:
        :param goods_num:
        :param goods_pic_list:
        :param goods_price:
        :param goods_status:
        :param bottom_button_name:
        :return:
        """
        self.input_goods_title(driver, goods_title)
        self.input_goods_details(driver, goods_detail)
        self.select_goods_num(driver, goods_num)
        for good_pic in goods_pic_list:
            self.upload_goods_img(driver, good_pic)
        time.sleep(5)
        self.input_goods_price(driver, goods_price)
        self.select_goods_status(driver, goods_status)
        self.click_bottom_button(driver, bottom_button_name)
        return True
