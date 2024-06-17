#! /usr/local/bin/python3.10
# coding=utf-8
# @Time: 2024/6/14 13:21
# @Author: xuliang
import time

import pytest

from config.driver_config import DriverConfig
from page.LoginPage import LoginPage
from page.LeftMenuPage import LeftMenuPage
from page.GoodsPage import GoodsPage

goods_info_list = [
    {
        'goods_title': '新增商品测试jay1',
        'goods_detail': '新增商品测试jay详情1',
        'goods_num': 2,
        'goods_pic_list': ['img1.jpg'],
        'goods_price': 233,
        'goods_status': '上架',
        'bottom_button_name': '提交'
    },
    {
        'goods_title': '新增商品测试jay2',
        'goods_detail': '新增商品测试jay详情2',
        'goods_num': 2,
        'goods_pic_list': ['img1.jpg'],
        'goods_price': 333,
        'goods_status': '上架',
        'bottom_button_name': '提交'
    },
]


class TestAddGoods(object):

    @pytest.mark.parametrize('goods_info', goods_info_list)
    def test_add_goods_001(self, driver, goods_info):
        # driver = DriverConfig().driver_config()
        LoginPage().login(driver, 'jay')
        LeftMenuPage().click_level_one_menu(driver, '产品')
        time.sleep(1)
        LeftMenuPage().click_level_two_menu(driver, '新增二手商品')
        time.sleep(1)
        GoodsPage().add_new_goods(
            driver,
            goods_title=goods_info['goods_title'],
            goods_detail=goods_info['goods_detail'],
            goods_num=goods_info['goods_num'],
            goods_pic_list=goods_info['goods_pic_list'],
            goods_price=goods_info['goods_price'],
            goods_status=goods_info['goods_status'],
            bottom_button_name=goods_info['bottom_button_name']
        )
        time.sleep(3)
