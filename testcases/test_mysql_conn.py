#! /usr/local/bin/python3.10
# coding=utf-8
# @Time: 2024/6/19 13:13
# @Author: xuliang

import time
import allure
import pytest

from page.LoginPage import LoginPage
from page.HomePage import HomePage
from common.mysql_operate import MysqlOperate
from logs.log import log


class TestMysqlConn(object):
    def test_mysql(self, driver):
        """获取账户余额"""
        with allure.step('登录'):
            LoginPage().login(driver, 'jay')
            time.sleep(2)

        with allure.step('获取账户余额'):
            balance = HomePage().get_balance(driver)
            log.info(balance)

        with allure.step('从数据库中获取账户余额'):
            db_user_id = MysqlOperate().query('select id from user where user ="周杰伦";')[0][0]
            sql = 'select balance from wallet where user_id = %s;' % db_user_id
            db_balance = MysqlOperate().query(sql)[0][0]
            log.info(db_balance)

        with allure.step('断言数据库中的值是否和页面数据一致'):
            assert str(balance) == str(db_balance)
