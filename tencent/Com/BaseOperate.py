#!/usr/bin/env python
# encoding: utf-8
'''
@author: yanghong
@file: BaseOperate.py
@time: 2020/7/20 15:00
@desc:
'''
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BaseOperate(object):
    def __init__(self, driver, timeout=30):
        self.driver = driver
        # self.driver.implicitly_wait(timeout)  # 默认5秒超时
        self.timeout = timeout

    def findElement(self, loc):
        if len(loc) != 2:
            raise ValueError('传参错误，必须为两个参数')
        else:
            if loc[0].upper() == 'ID':
                return self.findById(loc[1])
            elif loc[0].upper() == 'XPATH':
                return self.findByXpath(loc[1])
            elif loc[0].upper() == 'CLASSNAME':
                return self.findByClassName(loc[1])
            elif loc[0].upper() == 'CONTENTDESC':
                return self.findByContentDesc(loc[1])
            else:
                raise KeyError('第一个参数必须为id/xpath/classname/CONTENTDESC')

    def findByXpath(self, value):
        '''xpath定位'''
        try:
            WebDriverWait(self.driver, timeout=self.timeout).until(EC.presence_of_element_located((By.XPATH, value)))
            return self.driver.find_element_by_xpath(value)
        except Exception as e:
            print("未能找到元素:", value)
            raise

    def findById(self, value):
        '''resource-id定位'''
        try:
            WebDriverWait(self.driver, timeout=self.timeout).until(EC.presence_of_element_located((By.ID, value)))
            return self.driver.find_element_by_id(value)
        except Exception as e:
            print("未能找到元素:", value)
            raise

    def findByClassName(self, value):
        '''class定位'''
        try:
            WebDriverWait(self.driver, timeout=self.timeout).until(
                EC.presence_of_element_located((By.CLASS_NAME, value)))
            return self.driver.find_element_by_class_name(value)
        except Exception as e:
            print("未能找到元素:", value)
            raise

    def findByContentDesc(self, value):
        '''ContentDesc定位'''
        try:
            return self.driver.find_element_by_accessibility_id(value)
        except Exception as e:
            print("未能找到元素:", value)
            raise

    def swipeUp(self, during=500, times=1):
        l = self.driver.get_window_size()
        x1 = l['width'] * 0.5  # x坐标
        y1 = l['height'] * 0.75  # 起始y坐标
        y2 = l['height'] * 0.25  # 终点y坐标
        for i in range(times):
            time.sleep(1)
            self.driver.swipe(x1, y1, x1, y2, duration=during)

    def swipeDown(self, during=500, times=1):
        l = self.driver.get_window_size()
        x1 = l['width'] * 0.5  # x坐标
        y1 = l['height'] * 0.25  # 起始y坐标
        y2 = l['height'] * 0.75  # 终点y坐标
        for i in range(times):
            time.sleep(1)
            self.driver.swipe(x1, y1, x1, y2, duration=during)

    def swipeLeft(self, during=500, times=1):
        l = self.driver.get_window_size()
        x1 = l['width'] * 0.9  # x坐标
        y1 = l['height'] * 0.5  # 起始y坐标
        x2 = l['height'] * 0.1  # 终点x坐标
        for i in range(times):
            time.sleep(1)
            self.driver.swipe(x1, y1, x2, y1, duration=during)

    def swipeRight(self, during=500, times=1):
        l = self.driver.get_window_size()
        x1 = l['width'] * 0.25  # 起点x坐标
        x2 = l['width'] * 0.75  # 起点x坐标
        y = l['height'] * 0.5  # y坐标
        for i in range(times):
            time.sleep(1)
            self.driver.swipe(x1, y, x2, y, duration=during)


if __name__ == "__main__":
    # driver = webdriver.Chrome()
    # driver.get('http://www.baidu.com')
    # a = BaseOperate(driver)
    # loc = ('id', 'kw')
    # a.findElement(loc).send_keys('appium')
    pass
