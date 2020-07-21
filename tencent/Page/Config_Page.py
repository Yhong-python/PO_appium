#!/usr/bin/env python
# encoding: utf-8
'''
@author: yanghong
@file: Config_Page.py
@time: 2020/7/20 15:32
@desc:
'''
from tencent.Com.BaseOperate import BaseOperate
from selenium.common.exceptions import NoSuchElementException

class ConfigPage(BaseOperate):
    def enterConfigPage(self):
        enterConfigPage_loc = ('id', 'com.tencent.mobileqq:id/e3u')
        self.findElement(enterConfigPage_loc).click()
        return

    def allowGPSAlways(self):
        allowGPSAlways_loc = ('id', "com.android.permissioncontroller:id/permission_allow_always_button")
        self.findElement(allowGPSAlways_loc).click()
        return

    def clickConfigButton(self):
        clickConfigButton_loc = ('id', "com.tencent.mobileqq:id/gso")
        self.findElement(clickConfigButton_loc).click()
        return

    def clickAccountSafe(self):
        clickAccountSafe_loc = ('id', "com.tencent.mobileqq:id/gub")
        self.findElement(clickAccountSafe_loc).click()
        return

    def waitToOpen(self):
        try:
            self.findElement(('xpath', "//*[@text='稍后开启']")).click()
        except NoSuchElementException:
            pass

    def clickFingerPasswdConfig(self):
        clickFingerPasswdConfig_loc = ('id', "com.tencent.mobileqq:id/ct5")
        self.findElement(clickFingerPasswdConfig_loc).click()
        return

    def clickOpenFingerPasswd(self):
        clickOpenFingerPasswd_loc = ('id', "com.tencent.mobileqq:id/cte")
        self.findElement(clickOpenFingerPasswd_loc).click()
        return


