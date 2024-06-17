#! /usr/local/bin/python3.10
# coding=utf-8
# @Time: 2024/6/17 14:29
# @Author: xuliang
import random

import pytest


class TestRerun(object):
    @pytest.mark.flaky(reruns=5,reruns_delay=1)
    def test_rerun(self):
        num = random.randint(1,3)
        print('num:',num)
        if num!=1:
            print('false')
            raise Exception('失败了')
        else:
            print('success')