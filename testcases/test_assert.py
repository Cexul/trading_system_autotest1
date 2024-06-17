#! /usr/local/bin/python3.10
# coding=utf-8
# @Time: 2024/6/17 11:28
# @Author: xuliang
class TestAssert:
    def test_assert(self):
        # ==,!=,<,>,<=,>=
        assert "dd" == "dd"
        assert "aa" != "bb"
        assert 0 < 1
        assert 2 > 1
        assert 3 <= 7 - 2
        assert 4 >= 1 + 2
        # 包含和不包含
        assert "测开" in "从测试到测开"
        assert "java" not in "从测试到测开"
        # true和false
        assert 1
        assert (9<10) is True
        assert not False
        # 判断元素是否存在，在元素定位的时候，返回true和false，就直接断言了，不需要再去定义一个变量
