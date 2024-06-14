#! /usr/local/bin/python3.10
# coding=utf-8
# @Time: 2024/6/14 16:36
# @Author: xuliang

class IframeBaiduMapBase(object):
    def search_button(self):
        return "//button[@id='search-button']"

    def baidu_map_iframe(self):
        return "//iframe[@src='https://map.baidu.com/']"
