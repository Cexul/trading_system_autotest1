#! /usr/local/bin/python3.10
# coding=utf-8
# @Time: 2024/6/12 17:08
# @Author: xuliang


from selenium import webdriver

from common.tools import get_project_path, sep


class DriverConfig(object):

    def driver_config(self):
        """
        浏览器驱动
        :return:
        """
        options = webdriver.EdgeOptions()
        # 设置窗口大小
        options.add_argument("disable-infobars")
        options.add_argument('window-size=1920,1080')
        # 去除‘正在说到自动测试软件的控制’的提示
        options.add_experimental_option(
            "excludeSwitches", ["enable-automation"]
        )
        # 解决selenium无法访问http的问题
        options.add_argument('--ignore-certificate-errors')
        # 允许忽略local host上的TLS/SSL错误
        options.add_argument('--allow-insecure-localhost')
        # 设置为无痕模式
        options.add_argument('--incognito')
        # 设置为无头模式
        # options.add_argument('--headless')
        # 解决卡顿
        options.add_argument('--disable-gpu')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        driver = webdriver.Edge(
            executable_path=get_project_path() + sep(['driver_files', 'msedgedriver'], add_sep_before=True),
            options=options
        )

        # 删除所有cookies
        driver.delete_all_cookies()

        return driver
