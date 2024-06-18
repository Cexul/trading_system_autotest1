#! /usr/local/bin/python3.10
# coding=utf-8
# @Time: 2024/6/17 14:38
# @Author: xuliang

import pytest
from pytest_assume.plugin import assume

@pytest.mark.skip('跳过')
class TestAssert(object):
    def test_assert(self):
        with assume: assert 'as' in 'wer'

        pytest.assume(1+1==3)
        assert 1+1==2
        print('over')
