#!/usr/bin/env python
# encoding: utf-8
'''
@author: yanghong
@file: PaintPasswd_Page.py
@time: 2020/7/20 15:48
@desc:
'''
from tencent.Com.BaseOperate import BaseOperate
from appium.webdriver.common.touch_action import TouchAction


class PaintPage(BaseOperate):
    def paint(self):
        # 定位九宫格元素位置
        jiugongge = self.findElement(('id', 'com.tencent.mobileqq:id/ctc'))
        print("获取九宫格坐标位置：%s" % jiugongge.location)  # {'x': 108, 'y': 755}
        print("获取九宫格宽和高：%s" % jiugongge.size)  # {'height': 864, 'width': 864}
        jiugonggeweizhi = {}
        jiugonggeweizhi[1] = (None, jiugongge.location['x'] + jiugongge.size['width'] / 6,
                              jiugongge.location['y'] + jiugongge.size['height'] / 6)  # 数字1的x，y坐标
        jiugonggeweizhi[2] = (None, jiugongge.location['x'] + jiugongge.size['width'] * 3 / 6,
                              jiugongge.location['y'] + jiugongge.size['height'] / 6)  # 数字2的x，y坐标
        jiugonggeweizhi[3] = (None, jiugongge.location['x'] + jiugongge.size['width'] * 5 / 6,
                              jiugongge.location['y'] + jiugongge.size['height'] / 6)  # 数字3的x，y坐标
        jiugonggeweizhi[4] = (None, jiugongge.location['x'] + jiugongge.size['width'] / 6,
                              jiugongge.location['y'] + jiugongge.size['height'] * 3 / 6)  # 数字4的x，y坐标
        jiugonggeweizhi[5] = (None, jiugongge.location['x'] + jiugongge.size['width'] * 3 / 6,
                              jiugongge.location['y'] + jiugongge.size['height'] * 3 / 6)  # 数字5的x，y坐标
        jiugonggeweizhi[6] = (None, jiugongge.location['x'] + jiugongge.size['width'] * 5 / 6,
                              jiugongge.location['y'] + jiugongge.size['height'] * 3 / 6)  # 数字6的x，y坐标
        jiugonggeweizhi[7] = (None, jiugongge.location['x'] + jiugongge.size['width'] / 6,
                              jiugongge.location['y'] + jiugongge.size['height'] * 5 / 6)  # 数字6的x，y坐标
        jiugonggeweizhi[8] = (None, jiugongge.location['x'] + jiugongge.size['width'] * 3 / 6,
                              jiugongge.location['y'] + jiugongge.size['height'] * 5 / 6)  # 数字6的x，y坐标
        jiugonggeweizhi[9] = (None, jiugongge.location['x'] + jiugongge.size['width'] * 5 / 6,
                              jiugongge.location['y'] + jiugongge.size['height'] * 5 / 6)  # 数字6的x，y坐标

        # TouchAction(driver).press(x=252,y=899).wait(300).move_to(None,x=540,y=899).wait(300).move_to(x=828,y=899).release().perform()
        TouchAction(self.driver).press(*jiugonggeweizhi[1]).wait(300).move_to(*jiugonggeweizhi[2]).wait(300).move_to(
            *jiugonggeweizhi[3]).wait(
            300).move_to(*jiugonggeweizhi[5]).wait(300).move_to(*jiugonggeweizhi[7]).wait(300).move_to(
            *jiugonggeweizhi[8]).wait(300).move_to(*jiugonggeweizhi[9]).wait(
            300).release().perform()

        TouchAction(self.driver).press(*jiugonggeweizhi[1]).wait(300).move_to(*jiugonggeweizhi[2]).wait(300).move_to(
            *jiugonggeweizhi[3]).wait(
            300).move_to(*jiugonggeweizhi[5]).wait(300).move_to(*jiugonggeweizhi[7]).wait(300).move_to(
            *jiugonggeweizhi[8]).wait(300).move_to(*jiugonggeweizhi[9]).wait(
            300).release().perform()