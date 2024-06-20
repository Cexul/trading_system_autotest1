#! /usr/local/bin/python3.10
# coding=utf-8
# @Time: 2024/6/17 11:49
# @Author: xuliang

import pytest
import time

from config.driver_config import DriverConfig
from common.report_add_img import add_img_2_report
from common.process_redis import Process


@pytest.fixture()
def driver():
    global get_driver
    get_driver = DriverConfig().driver_config()
    yield get_driver
    get_driver.quit()


def pytest_terminal_summary(terminalreporter, exitstatus, config):
    '''收集测试结果'''
    # print(terminalreporter.stats)
    print("total:", terminalreporter._numcollected)
    print('passed:', len([i for i in terminalreporter.stats.get('passed', []) if i.when != 'teardown']))
    print('failed:', len([i for i in terminalreporter.stats.get('failed', []) if i.when != 'teardown']))
    print('error:', len([i for i in terminalreporter.stats.get('error', []) if i.when != 'teardown']))
    print('skipped:', len([i for i in terminalreporter.stats.get('skipped', []) if i.when != 'teardown']))
    # print('成功率：%.2f' % (len(terminalreporter.stats.get('passed', []))/terminalreporter._numcollected*100)+'%')

    # terminalreporter._sessionstarttime 会话开始时间
    duration = time.time() - terminalreporter._sessionstarttime
    print('total times:', duration, 'seconds')


def pytest_collection_finish(session):
    # 所有用例个数
    total = len(session.items)
    print(f"当前执行测试的用例数为：{len(session.items)}")
    # 重置用例进度和失败用例进度
    Process().reset_all()
    # 初始化进度
    Process().init_process(total)


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    # 获取钩子方法的调用结果
    out = yield
    # 从钩子方法的调用结果中获取测试报告
    report = out.get_result()
    report.description = str(item.function.__doc__)

    if report.when == 'call':
        if report.failed:
            # 失败了就截图
            add_img_2_report(get_driver, '失败截图', need_sleep=False)
            # 更新失败用例个数
            Process().update_fail()
            # 增加失败用例名称
            Process().insert_into_fail_testcase_names(report.description)
        elif report.passed:
            # 更新成功用例个数
            Process().update_success()
        else:
            pass
        process = Process().get_process()
        print(process)
