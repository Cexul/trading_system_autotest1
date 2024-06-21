#! /usr/bin/python3.10
# coding=utf-8
# @Time: 2024/6/12 12:23
# @Author: xuliang

import datetime
import os.path

import requests


def get_now_time():
    return datetime.datetime.now()

def get_now_date_time_str():
    return datetime.datetime.now().strftime('%Y%m%d%H%M%S')

def get_project_path():
    """
    获取项目的绝对路径
    :return:
    """
    project_name = 'trading_system_autotest1'
    file_path = os.path.dirname(__file__)
    # print(file_path)
    # print(file_path.find(project_name))
    # print(file_path[:file_path.find(project_name)+len(project_name)])
    return file_path[:file_path.find(project_name)+len(project_name)]

def sep(path,add_sep_before=False,add_sep_after=False):
    """
    系统分隔符
    :param path: 路径列表，类型是数组
    :param add_sep_before: 是否需要在拼接的路径前加一个分隔符
    :param add_sep_after: 是否需要在拼接的路径后加一个分隔符
    :return:
    """
    all_path = os.sep.join(path)
    if add_sep_before:
        all_path = os.sep +all_path
    if add_sep_after:
        all_path = all_path +os.sep
    # print(all_path)
    return all_path

def get_img_path(img_name):
    """
    获取商品图片路径
    :param img_name:
    :return:
    """
    img_dir_path = get_project_path()+sep(['img',img_name],add_sep_before=True)
    return img_dir_path

def get_every_wallpaper():
    """
    从bing获取每日壁纸
    :return: 
    """
    everyday_wallpaper_url = 'http://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=10&mkt=zh-CN'
    try:
        res = requests.get(url=everyday_wallpaper_url)
        wallpaper_url = 'http://cn.bing.com'+res.json()['images'][0]['url'][:-7]
    except Exception as e:
        print(e)
        wallpaper_url =''
    return wallpaper_url


if __name__ == '__main__':
    # print(get_project_path())
    # print(get_project_path())
    # sep(['congif','environment.yaml'],add_sep_after=True)
    print(get_every_wallpaper())
