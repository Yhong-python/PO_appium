#!/usr/bin/env python
# encoding: utf-8
'''
@author: yanghong
@file: createPasswd.py
@time: 2020/7/20 15:51
@desc:
'''
import os

from appium import webdriver
from ruamel import yaml
import ruamel
# import yaml
from tencent.Page.Config_Page import ConfigPage
from tencent.Page.Login_Page import loginPage
from tencent.Page.Main_Page import MainPage
from tencent.Page.PaintPasswd_Page import PaintPage


class PaintPasswdTestcase:
    def __init__(self):
        curPath = os.path.dirname(
            os.path.dirname(os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)), ".."))))
        yamlPath = os.path.join(curPath, "Yaml", "devices.yaml")
        # # open方法打开直接读出来
        f = open(yamlPath, 'r')
        cfg = f.read()
        # devicesInfo = yaml.load(cfg) #老语法
        devicesInfo = yaml.load(cfg,Loader=ruamel.yaml.RoundTripLoader)  # 用load方法转字典
        print(devicesInfo)
        capabilities = devicesInfo['truephone']['devices1']
        capabilities['appPackage'] = "com.tencent.mobileqq"
        capabilities['appActivity'] = ".activity.SplashActivity"
        print(capabilities)
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', capabilities)

    def paint(self):
        MainPage(self.driver).clickAgreeButton()
        MainPage(self.driver).waitInitPage()
        MainPage(self.driver).enterLoginPage()

        loginPage(self.driver).inputUsername()
        loginPage(self.driver).inputPasswd()
        loginPage(self.driver).clickLoginButton()
        loginPage(self.driver).clickToAuthorizeButton()
        loginPage(self.driver).clickYesButton()

        ConfigPage(self.driver).enterConfigPage()
        ConfigPage(self.driver).allowGPSAlways()
        ConfigPage(self.driver).clickConfigButton()
        ConfigPage(self.driver).clickAccountSafe()
        ConfigPage(self.driver).waitToOpen()
        ConfigPage(self.driver).clickFingerPasswdConfig()
        ConfigPage(self.driver).clickOpenFingerPasswd()

        PaintPage(self.driver).paint()


PaintPasswdTestcase().paint()
