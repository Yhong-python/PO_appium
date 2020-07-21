#!/usr/bin/env python
# encoding: utf-8
'''
@author: yanghong
@file: readyaml.py
@time: 2020/4/21 14:27
@desc:
'''
import os
import yaml
# yaml.warnings({'YAMLLoadWarning': False})

# 获取当前脚本所在文件夹路径
curPath = os.path.dirname(os.path.realpath(__file__))
# 获取yaml文件路径
yamlPath = os.path.join(curPath, "test2.yaml")

# open方法打开直接读出来
f = open(yamlPath, 'r')
cfg = f.read()
# print(type(cfg))  # 读出来是字符串
# print(cfg)
# d=yaml.load(cfg)
d = yaml.full_load(cfg)  # 用load方法转字典
print(d)
# print(type(d))
# print(d['user'])