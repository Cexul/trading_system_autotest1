#! /usr/local/bin/python3.10
# coding=utf-8
# @Time: 2024/6/19 14:38
# @Author: xuliang

import pytest
import allure
import time

from page.LoginPage import LoginPage
from page.GoodsPage import GoodsPage
from page.OrderPage import OrderPage
from page.LeftMenuPage import LeftMenuPage
from page.TradingMarketPage import TradingMarketPage
from common.report_add_img import add_img_2_report
from common.tools import get_now_date_time_str


class TestTradingFlow(object):

    @pytest.mark.trading_flow
    @allure.feature('交易流')
    @allure.description('交易流')
    def test_trading_flow(self, driver):
        """交易流"""
        with allure.step('登录卖家'):
            LoginPage().api_login(driver, 'jay')
            add_img_2_report(driver, '登录卖家')

        with allure.step('新增二手商品'):
            LeftMenuPage().click_level_one_menu(driver, '产品')
            LeftMenuPage().click_level_two_menu(driver, '新增二手商品')
            time.sleep(2)
            add_img_2_report(driver, '进入新增二手商品')

        with allure.step('新增商品'):
            good_title = '交易流测试' + get_now_date_time_str()
            GoodsPage().add_new_goods(
                driver,
                goods_title=good_title,
                goods_detail='交易流测试',
                goods_num=2,
                goods_pic_list=['img1.jpg'],
                goods_price=233,
                goods_status='上架',
                bottom_button_name='提交'
            )
            add_img_2_report(driver, '新增商品')
            time.sleep(3)

        with allure.step('切换买家用户'):
            LoginPage().api_login(driver,'william')
            add_img_2_report(driver, '登录买家')

        with allure.step('进入交易市场'):
            LeftMenuPage().click_level_one_menu(driver,'交易市场')
            add_img_2_report(driver, '进入交易市场')

        with allure.step('搜索宝贝'):
            TradingMarketPage().input_search_input(driver, good_title)
            TradingMarketPage().click_search(driver)
            add_img_2_report(driver, '搜索宝贝')

        with allure.step('点击商品卡片'):
            TradingMarketPage().click_product_card(driver, good_title)
            time.sleep(1)
            add_img_2_report(driver, '点击商品卡片')

        with allure.step('点击我想要'):
            TradingMarketPage().click_i_want(driver)
            time.sleep(1)
            add_img_2_report(driver, '点击我想要')

        with allure.step('选择收货地址'):
            TradingMarketPage().click_address(driver)
            time.sleep(1)
            TradingMarketPage().select_detail_address(driver, 1)
            add_img_2_report(driver, '选择收货地址')

        with allure.step('点击确认按钮'):
            TradingMarketPage().click_bottom_button(driver)
            time.sleep(1)
            add_img_2_report(driver, '点击确认按钮后')

        with allure.step('买家支付'):
            OrderPage().click_coder_operation(driver,good_title,'去支付')
            time.sleep(1)
            OrderPage().click_order_operation_confirm(driver)
            add_img_2_report(driver,'买家支付并确认')

        with allure.step('切换卖家用户'):
            LoginPage().api_login(driver,'jay')
            add_img_2_report(driver, '登录卖家')

        with allure.step('进入已卖出的宝贝'):
            LeftMenuPage().click_level_one_menu(driver,'我的订单')
            time.sleep(1)
            LeftMenuPage().click_level_two_menu(driver,'已卖出的宝贝')
            add_img_2_report(driver, '进入已卖出的宝贝')

        with allure.step('卖家发货'):
            OrderPage().click_coder_operation(driver,good_title,'去发货')
            time.sleep(1)
            OrderPage().click_delivery_logistics(driver)
            OrderPage().click_select_logistics(driver,'顺丰速运')
            time.sleep(1)
            OrderPage().input_logistics_order_no(driver,'3245478921637')
            time.sleep(1)
            OrderPage().click_order_operation_confirm(driver)
            add_img_2_report(driver, '卖家发货')
            time.sleep(1)

        with allure.step('切换买家用户'):
            LoginPage().api_login(driver,'william')
            add_img_2_report(driver, '登录买家')


        with allure.step('进入已买到的宝贝'):
            LeftMenuPage().click_level_one_menu(driver,'我的订单')
            time.sleep(1)
            LeftMenuPage().click_level_two_menu(driver,'已买到的宝贝')
            add_img_2_report(driver, '进入已买到的宝贝')

        with allure.step('买家确认收货'):
            OrderPage().click_coder_operation(driver,good_title,'去确认收货')
            time.sleep(1)
            OrderPage().click_order_operation_confirm(driver)
            add_img_2_report(driver, '买家确认收货')

        with allure.step('买家评价'):
            OrderPage().click_coder_operation(driver,good_title,'去评价')
            time.sleep(1)
            OrderPage().click_evaluation(driver,5)
            time.sleep(1)
            OrderPage().click_evaluation_confirm(driver)
            time.sleep(1)
            add_img_2_report(driver, '买家评价')









