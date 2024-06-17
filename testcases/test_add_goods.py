#! /usr/local/bin/python3.10
# coding=utf-8
# @Time: 2024/6/14 13:21
# @Author: xuliang
import time

from config.driver_config import DriverConfig
from page.LoginPage import LoginPage
from page.LeftMenuPage import LeftMenuPage
from page.GoodsPage import GoodsPage


class TestAddGoods(object):
    def test_add_goods_001(self):
        driver = DriverConfig().driver_config()
        LoginPage().login(driver, 'jay')
        LeftMenuPage().click_level_one_menu(driver, '产品')
        time.sleep(1)
        LeftMenuPage().click_level_two_menu(driver, '新增二手商品')
        time.sleep(1)
        GoodsPage().add_new_goods(
            driver,
            goods_title='新增商品测试jay',
            goods_detail='新增商品测试jay详情',
            goods_num=2,
            goods_pic_list=['img1.jpg'],
            goods_price=233,
            goods_status='上架',
            bottom_button_name='提交'
        )
        time.sleep(3)
        driver.close()
