#!/usr/bin/env python

import os
import requests
import json
import sys

rootdir = 'D:\\Workspace\\article'
service_ip = '192.168.68.189'


def unsupport():
    print('unsupported operation')


def update(file):
    print('update works!' + data)


def create(data):
    return article_fetch('save', data)


def delete(data):
    print('delete works!')


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


def getmeta(content):
    count = 0
    for line in content:
        line = line.strip()
        if line == '':
            continue
        if line.startswith('# '):
            return {
                'title': line.replace('# ', '')
            }
        count = count + 1
        if count == 10:
            return {}


args = sys.argv[1:]

if args[0] not in ['update', 'delete', 'create']:
    print('当前仅支持 update, create, delete 操作')
    exit()

if not args[1].endswith('.md'):
    print(args[1] + ' 不是一个 markdown 文件！')
    exit()

func = {
    'update': update,
    'delete': delete,
    'create': create
}.get(args[0], unsupport)(args[1])


exit(0)
