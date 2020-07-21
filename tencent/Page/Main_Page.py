#!/usr/bin/env python
# encoding: utf-8
'''
@author: yanghong
@file: Main_Page.py
@time: 2020/7/20 15:13
@desc:
'''
from tencent.Com.BaseOperate import BaseOperate
import os,yaml
from appium import webdriver

class MainPage(BaseOperate):
    def clickAgreeButton(self):
        agreeButton_loc = ('id', 'com.tencent.mobileqq:id/dialogRightBtn')
        self.findElement(agreeButton_loc).click()
        return

    def waitInitPage(self):
        self.driver.wait_activity(".activity.LoginActivity", 20)
        return

    def enterLoginPage(self):
        loginButton_loc = ('id', 'com.tencent.mobileqq:id/btn_login')
        self.findElement(loginButton_loc).click()
        return

# curPath = os.path.dirname(os.path.dirname(os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)),".."))))
# yamlPath = os.path.join(curPath, "Yaml", "devices.yaml")
# # # open方法打开直接读出来
# f = open(yamlPath, 'r')
# cfg = f.read()
# devicesInfo = yaml.full_load(cfg)  # 用load方法转字典
# print(devicesInfo)
# capabilities = devicesInfo['truephone']['devices1']
# capabilities['appPackage'] = "com.tencent.mobileqq"
# capabilities['appActivity'] = ".activity.SplashActivity"
# print(capabilities)
# driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', capabilities)
# a=MainPage(driver)
# print(dir(a))
# print(a.clickAgreeButton())