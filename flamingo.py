#!/usr/bin/env python
import getopt
import os
import requests
import json
import sys

rootdir = 'D:\\Workspace\\article'
#service_ip = '192.168.68.189'
service_ip = '129.28.148.128'

category = None
title = None
content = None
author = None
update = False
abstract = None
path = None

categories = ['linux', 'java', 'js', 'python', 'devops', 'note']

opts, args = getopt.getopt(
    sys.argv[1:], 'hc:a:u',  ['help', 'category=', 'author=', 'update'])

#print(opts)
#print(args)

for opt, arg in opts:
    if opt in ('-h', '--help'):
        print('flamingo.py -c linux -a rudy linux/bash.md\nflamingo.py -c linux -a rudy --update linux/bash.md')
        sys.exit()
    if opt in ('-c', '--category'):
        if arg not in categories:
            print('Error: 不支持的category(' + ','.join(categories) + '): ' + arg)
            exit()
        category = arg
    if opt in ('-a', '--author'):
        author = arg
    if opt in ('-u', '--update'):
        update = True

if args.__len__() == 0:
    print('Error: 请选择要操作的文件')
    exit()

if args.__len__() > 1:
    print('Error: 一次只能操作一个文件')
    exit()

if not args[0].endswith('.md'):
    print('文件 ' + args[0] + ' 不是 Markdown 类型！')
    exit()

if category is None:
    print('Error: 未指定文章所属类型')
    exit()

if author is None:
    print('Error: 未指定作者')
    exit()

path = args[0].strip('./')
file = open(args[0], encoding='utf-8')
lines = file.readlines()
firstline = lines[0]
if not firstline.startswith('# '):
    raise Exception('markdown 文件必须以一级标题开始')
title = firstline[2:].strip('\n')
content = ''.join(lines)


def fetch(url, data=None, method="post", headers=None, params=None):
    print('url: ', url)
    params = json.dumps(data, ensure_ascii=False, sort_keys=True, indent=4)
    print('params: ', params)
    if method.lower() == "get":
        resp = requests.get(url, headers=headers, params=params)
    else:
        resp = requests.post(url, json=data, headers=headers, params=params)
    resp = checkdata(resp)
    print('response: ', json.dumps(
        resp, ensure_ascii=False, sort_keys=True, indent=4))
    return resp


def checkdata(resp):
    resp_data = json.loads(resp.text)
    if resp_data["status"] != 0:
        return resp_data
    return resp_data["data"]


def article_fetch(url, data=None, method="post", params=None):
    return fetch('http://' + service_ip + ':5000/article/' + url, data=data, method=method, params=params)


params = {
    'title': title,
    'authorCode': author,
    'abstract': abstract,
    'content': content,
    'category': category,
    'path': path
}

if (update is True):
    article_fetch('updateByPath', data=params)
else:
    article_fetch('save', data=params)
