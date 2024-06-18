#! /usr/local/bin/python3.10
# coding=utf-8
# @Time: 2024/6/18 10:31
# @Author: xuliang

import aircv as ac
from common.tools import get_project_path, sep


class FindImg(object):
    def img_imread(self, img_path):
        """
        读取图片
        """

        return ac.imread(img_path)

    def get_confindence(self, source_path, search_path):
        """
        查找图片
        :param source_path:原图路径
        :param search_path:需要查找的图片的路径
        """
        img_src = self.img_imread(source_path)
        img_sch = self.img_imread(search_path)
        result = ac.find_template(img_src, img_sch)
        print(result)


if __name__ == '__main__':
    source_path = get_project_path() + sep(['img', 'source.png'], add_sep_before=True)
    search_path = get_project_path() + sep(['img', 'search.png'], add_sep_before=True)
    FindImg().get_confindence(source_path,search_path)
