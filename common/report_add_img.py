#! /usr/local/bin/python3.10
# coding=utf-8
# @Time: 2024/6/18 11:45
# @Author: xuliang
import time

import allure


def add_img_2_report(driver, step_name, need_sleep=True):
    """
    截图并插入allure报告
    :param driver:
    :param step_name:
    :param need_sleep:
    :return:
    """

    if need_sleep:
        time.sleep(2)
    allure.attach(
        driver.get_screenshot_as_png(),
        step_name + '.png',
        allure.attachment_type.PNG
    )


def add_img_path_2_report(img_path, step_name):
    """
    将图片插入到allure报告
    :param img_path: 图片路径
    :param step_name: 步骤名称
    :return:
    """
    allure.attach.file(img_path, step_name, allure.attachment_type.PNG)
