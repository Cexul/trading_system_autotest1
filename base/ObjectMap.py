#! /usr/local/bin/python3.10
# coding=utf-8
# @Time: 2024/6/13 12:15
# @Author: xuliang


import time

from selenium.common.exceptions import ElementNotVisibleException, WebDriverException


class ObjectMap(object):

    def element_get(self, driver, locate_type, locator_expression, timeout=10, must_be_visible=False):
        """
        单个元素获取
        :param driver: 浏览器驱动
        :param locate_type: 定位方式类型
        :param locator_expression: 定位表达式
        :param timeout: 超时时间
        :param must_be_visible: 元素是否必须可见，True是必须可见，False是默认值
        :return: 逻辑判断成功，返回定位元素element
        """
        # 设置开始时间
        start_ms = time.time() * 1000
        # 设置结束时间
        end_ms = start_ms + (timeout * 1000)
        for x in range(int(timeout * 10)):

            # 查找元素
            try:
                element = driver.find_element(by=locate_type, value=locator_expression)
                # 如果元素不是必须可见的，就直接返回元素
                if not must_be_visible:
                    return element
                # 如果元素是必须可见的，就需要先判断元素是否可见
                else:
                    if element.is_displayed():
                        return element
                    else:
                        raise Exception()

            except Exception:
                now_ms = time.time() * 1000
                if now_ms >= end_ms:
                    break
                pass
            time.sleep(0.1)
        raise ElementNotVisibleException('元素定位失败，定位方式:' + locate_type + '定位表达式:' + locator_expression)

    def wait_for_ready_state_complete(self, driver, timeout=30):
        """

        :param driver: 浏览器驱动
        :param timeout: 超时时间
        :return:
        """
        # 开始时间
        start_ms = time.time() * 1000
        # 结束时间
        end_ms = start_ms + (timeout * 1000)
        for x in range(int(timeout * 10)):
            try:
                ready_state = driver.execute_scripe('return document.readyState')
            except WebDriverException:
                # 如果有driver的错误，执行js失败，就直接跳过
                time.sleep(0.03)
                return True
            if ready_state == 'complete':
                time.sleep(0.01)
                return True
            else:
                now_ms = time.time() * 1000
                if now_ms >= end_ms:
                    break
                time.sleep(0.1)
        raise Exception('打开网页时，页面元素在%s秒后仍然没有加载完成' % timeout)

    def element_disappear(self, driver, locate_type, locator_expression, timeout=30):
        """
        等待页面元素消失
        :param driver: 浏览器驱动
        :param locate_type: 定位方式
        :param locator_expression: 定位表达式
        :param timeout: 超时时间
        :return:
        """
        if locate_type:
            # 开始时间
            start_ms = time.time() * 1000
            # 结束时间
            end_ms = start_ms + (timeout * 1000)
            for x in range(int(timeout * 10)):
                try:
                    element = driver.find_element(by=locate_type, value=locator_expression)
                    if element.is_displayed():
                        now_ms = time.time() * 1000
                        if now_ms >= end_ms:
                            break
                        time.sleep(0.1)
                except Exception:
                    return True
            raise Exception('元素没有消失，定位方式：%s，定位表达式是：%s' % (locate_type, locator_expression))
        else:
            pass

    def element_appear(self, driver, locate_type, locator_expression, timeout=30):
        """
        等待页面元素出现
        :param driver: 浏览器驱动
        :param locate_type: 定位方式
        :param locator_expression: 定位表达式
        :param timeout: 超时时间
        :return:
        """
        if locate_type:
            # 开始时间
            start_ms = time.time() * 1000
            # 结束时间
            end_ms = start_ms + (timeout * 1000)
            for x in range(int(timeout * 10)):
                try:
                    element = driver.find_element(by=locate_type, value=locator_expression)
                    if element.is_displayed():
                        return element
                    else:
                        raise Exception()
                except Exception:
                    now_ms = time.time() * 1000
                    if now_ms >= end_ms:
                        break
                    time.sleep(0.1)
                    pass
            raise ElementNotVisibleException(
                '元素没有出现，定位方式：%s，定位表达式：%s' % (locate_type, locator_expression))
        else:
            pass
