#!/usr/bin/env python
# encoding: utf-8
'''
@author: yanghong
@file: Login_Page.py
@time: 2020/7/20 15:02
@desc:
'''
from tencent.Com.BaseOperate import BaseOperate


class loginPage(BaseOperate):
    def inputUsername(self, value='3251739518'):
        username_loc = ('contentdesc', '请输入QQ号码或手机或邮箱')
        self.findElement(username_loc).send_keys(value)
        return

    def inputPasswd(self, value='yanghong1994'):
        passwd_loc = ('contentdesc', '密码 安全')
        self.findElement(passwd_loc).send_keys(value)
        return

    def clickLoginButton(self):
        loginButton_loc = ('id', 'com.tencent.mobileqq:id/login')
        self.findElement(loginButton_loc).click()
        return

    def clickToAuthorizeButton(self):
        toAuthorizeButton_loc = ('id', 'com.tencent.mobileqq:id/dialogRightBtn')
        self.findElement(toAuthorizeButton_loc).click()
        return

    def clickYesButton(self):
        clickYesButton_loc = ('id', 'android:id/button1')
        self.findElement(clickYesButton_loc).click()
        return


