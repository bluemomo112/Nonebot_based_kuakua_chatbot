
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/6/8 18:50
# @Author  : Momo Lan| LAN LINLING
# @FileName: bk.py
# @Software: PyCharm
from os import path
import nonebot
import config

path=path.join(path.dirname(__file__), 'awesome', 'plugins')

if __name__ == '__main__':
    nonebot.init(config)
    nonebot.load_plugins(path,'awesome.plugins')
    nonebot.run()
