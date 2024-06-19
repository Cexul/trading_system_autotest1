#! /usr/local/bin/python3.10
# coding=utf-8
# @Time: 2024/6/12 13:57
# @Author: xuliang

import yaml
from common.tools import get_project_path, sep


class GetConf(object):

    def __init__(self):
        with open(get_project_path() + sep(['config', 'environment.yaml'], add_sep_before=True), 'r',
                  encoding='utf-8') as env_file:
            self.env = yaml.load(env_file, Loader=yaml.FullLoader)
            # print(self.env)

    def get_username_password(self, user):
        # return self.env['username'],self.env['password']
        return self.env['user'][user]['username'], self.env['user'][user]['password']

    def get_url(self):
        return self.env['url']

    def get_mysql_config(self):
        return self.env['mysql']


if __name__ == '__main__':
    print(GetConf().get_mysql_config())
