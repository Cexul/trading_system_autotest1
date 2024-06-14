#! /usr/local/bin/python3.10
# coding=utf-8
# @Time: 2024/6/13 12:15
# @Author: xuliang


import time

from selenium.common.exceptions import ElementNotVisibleException, WebDriverException, NoSuchElementException, \
    StaleElementReferenceException

from selenium.webdriver.common.keys import Keys

from common.yaml_config import *


class ObjectMap(object):
    # 获取基础地址
    url = GetConf().get_url()

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
                ready_state = driver.execute_script('return document.readyState')
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

    def element_to_url(self, driver, url, locate_type_disappear=None, locator_expression_disappear=None,
                       locate_type_appear=None, locator_expression_appear=None):
        """
        跳转地址
        :param driver: 浏览器驱动
        :param url: 跳转的地址
        :param locate_type_disappear: 等待页面元素消失的定位方式
        :param locator_expression_disappear: 等待页面元素消失的定位表达式
        :param locate_type_appear: 等待页面元素出现的定位方式
        :param locator_expression_appear: 等待页面元素出现的定位表达式
        :return:
        """
        try:
            driver.get(self.url + url)
            # 等待页面元素加载完成
            self.wait_for_ready_state_complete(driver)
            # 等待页面元素消失
            self.element_disappear(driver, locate_type_disappear, locator_expression_disappear)
            # 等待页面元素出现
            self.element_appear(driver, locate_type_appear, locator_expression_appear)
        except Exception as e:
            print('跳转地址失败，原因是：%s' % e)
            return False
        return True

    def element_is_display(self, driver, locate_type, locator_expression):
        """
        元素是否展示
        :param driver:
        :param locate_type:
        :param locator_expression:
        :return:
        """
        try:
            driver.find_element(by=locate_type, value=locator_expression)
            return True
        except NoSuchElementException:
            # 发生了NoSuchElementException异常后，说明页面中没有找到这个元素，返回False
            return False

    def element_fill_value(self, driver, locate_type, locator_expression, fill_value, timeout=30):
        """
        元素填值
        :param driver: 浏览器驱动
        :param locate_type: 定位方式
        :param locator_expression: 定位表达式
        :param fill_value: 填入的值
        :param timeout: 超时时间
        :return:
        """
        element = self.element_appear(driver, locate_type=locate_type, locator_expression=locator_expression,
                                      timeout=timeout)
        try:
            # 清除元素中的原有值
            element.clear()
        except StaleElementReferenceException:  # 对页面元素没有刷新的异常进行捕获
            self.wait_for_ready_state_complete(driver=driver)
            # 等待页面刷新重试一次
            time.sleep(0.06)
            element = self.element_appear(driver, locate_type=locate_type, locator_expression=locator_expression,
                                          timeout=timeout)
            try:
                element.clear()
            except Exception as e:
                pass
        except Exception as e:
            pass
        if type(fill_value) is int or type(fill_value) is float:
            fill_value = str(fill_value)
            try:
                if not fill_value.endswith('\n'):
                    element.send_keys(fill_value)
                    self.wait_for_ready_state_complete(driver=driver)
                else:
                    fill_value = fill_value[:-1]
                    element.send_keys(fill_value)
                    element.send_keys(Keys.RETURN)
                    self.wait_for_ready_state_complete(driver=driver)
            except StaleElementReferenceException:
                self.wait_for_ready_state_complete(driver=driver)
                time.sleep(0.06)
                element = self.element_appear(driver, locate_type=locate_type, locator_expression=locator_expression,
                                              timeout=timeout)
                element.clear()
                if not fill_value.endswith('\n'):
                    element.send_keys(fill_value)
                    self.wait_for_ready_state_complete(driver=driver)
                else:
                    fill_value = fill_value[:-1]
                    element.send_keys(fill_value)
                    element.send_keys(Keys.RETURN)
                    self.wait_for_ready_state_complete(driver=driver)
            except Exception:
                raise Exception('元素填写失败')
        else:
            try:
                element.send_keys(fill_value)
                self.wait_for_ready_state_complete(driver=driver)
            except Exception as e:
                print('填写失败', e)
        return True

    def element_click(
            self,
            driver,
            locate_type,
            locator_expression,
            locate_type_disappear=None,
            locator_expression_disappear=None,
            locate_type_appear=None,
            locator_expression_appear=None,
            timeout=30):
        """
        元素点击
        :param driver: 浏览器驱动
        :param locate_type: 定位方式类型
        :param locator_expression: 定位表达式
        :param locate_type_disappear: 等待元素消失的定位方式类型
        :param locator_expression_disappear: 等待元素消失的定位表达式
        :param locate_type_appear: 等待元素出现的定位方式类型
        :param locator_expression_appear: 等待元素出现的定位表达式
        :param tiamout: 超时时间
        :return:
        """
        # 元素要可见
        element = self.element_appear(driver, locate_type=locate_type, locator_expression=locator_expression,
                                      timeout=timeout)
        try:
            element.click()
        except StaleElementReferenceException:
            self.wait_for_ready_state_complete(driver=driver)
            time.sleep(0.06)
            element = self.element_appear(driver, locate_type=locate_type, locator_expression=locator_expression,
                                          timeout=timeout)
            element.click()
        except Exception as e:
            print('页面元素出现异常，元素不可点击', e)
            return False
        try:
            # 点击元素后的元素出现或者消失
            self.element_appear(driver, locate_type=locate_type_appear, locator_expression=locator_expression_appear,
                                timeout=timeout)
            self.element_disappear(driver, locate_type_disappear, locator_expression_disappear)
        except Exception as e:
            print('等待元素消失或者出现失败', e)
            return False
        return True

    def upload(self, driver, locate_type, locator_expression, file_path):
        """
        文件上传
        :param driver:
        :param locate_type:
        :param locator_expression:
        :param file_path:
        :return:
        """
        element = self.element_get(driver, locate_type, locator_expression)
        return element.send_keys(file_path)
