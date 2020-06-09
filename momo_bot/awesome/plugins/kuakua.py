#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/6/8 18:42
# @Author  : Momo Lan| LAN LINLING
# @FileName: kuakua.py
# @Software: PyCharm

from nonebot import on_command,CommandSession
import nonebot
import time,random
import re,os
import requests,json

@on_command('kuakua', aliases=('夸夸',"夸奖","舔狗","夸我","夸夸我"))
async def kuakua(session:CommandSession):
    praise_time = session.get('time', prompt='哦，夸个几毛钱呢？')
    try:
        praise_time=int(re.findall(r"(\d+)",praise_time)[0])
        print(praise_time)
    except:
        session.pause('无法识别您输入的时间呢，请重新输入')

    print(os.path.join(os.path.dirname(__file__),"kuakua_clean.txt" ))
    try:
        with open(os.path.join(os.path.dirname(__file__),"kuakua_clean.txt" ),"r",encoding="utf-8") as f:
            lines=f.readlines()
            text=random.sample(lines,praise_time)
            for t in text:
                await session.send(t.strip())
                time.sleep(1)
    except:
        session.send("o(╥﹏╥)o哭哭，程序出错了呢")



