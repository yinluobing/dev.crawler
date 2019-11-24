#!/usr/bin/python3
# -*-: coding: utf-8 -*-
"""
:author: icker
:date: 2019-11-24
:desc:
"""
from qichacha import crawler as QccCrawler
from util import log
import urllib3
urllib3.disable_warnings()


log.init("qichacha.log")
app = QccCrawler

if __name__ == '__main__':
    keys = ['软装', '家具', '民用家具', '酒店家具', '办公家具', '户外家具', '软装饰品', '软装灯饰', '软装墙饰', '软装吊饰', '软装画艺', '软装雕塑','软装酒店用品', '软装花器', '软装窗帘', '软装床品', '软装抱枕靠垫', '软装墙布墙纸', '软装地毯', '软装餐布', '软装布艺', '软装花植花器', '软装鲜花绿植','软装仿真干花']
    app.load_keys(keys)
    app.start()

