#! /usr/local/bin/python3.10
# coding=utf-8
# @Time: 2024/6/12 17:12
# @Author: xuliang


class LoginBase(object):

    def login_input(self, input_placeholder):
        """
        登录用户名、密码输入框
        :param input_placeholder:
        :return:
        """
        return '//input[@placeholder="' + input_placeholder + '"]'

    def login_button(self, button_name):
        """
        登录按钮
        :param button_name:
        :return:
        """
        return '//span[text()="' + button_name + '"]/parent::button'

    def login_success(self):
        """
        登录成功
        :return:
        """
        return '//p[text()="登录成功"]'


# if __name__ == '__main__':
#     print(LoginBase().login_input('用户名'))
#     print(LoginBase().login_button('登录'))
