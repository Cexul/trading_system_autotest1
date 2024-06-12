#! /usr/bin/python3.10
# coding=utf-8
# @Time: 2024/6/12 12:40
# @Author: xuliang

from time import sleep

from config.driver_config import DriverConfig

driver = DriverConfig.driver_config()
driver.get('http://www.tcpjwtester.top')
sleep(2)
driver.find_element_by_xpath('//input[@placeholder="用户名"]').send_keys('周杰伦')
sleep(2)
driver.find_element_by_xpath('//*[@id="app"]/div/form/div[4]/div/div/input').send_keys('1234abcd!')
sleep(2)
driver.find_element_by_xpath('//*[@id="app"]/div/form/button').click()
sleep(2)
driver.close()