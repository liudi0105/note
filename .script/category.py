import os
import requests
import json

rootdir = 'D:\\Workspace\\article'

dirMap = {
    "db": "数据库",
    "golang": "Go语言",
    "linux": "Linux",
    "middleware": "中间件",
    "network": "网络",
    "note": "笔记",
    "devops": "运维",
    "python": "Python",
    "web": "前端",
    "java": "Java"
}


def fetch(url, data=None, method="post", headers=None, params=None):
    print('url: ', url)
    # print('params: ', json.dumps(data, ensure_ascii=False, sort_keys=True, indent=4))
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
        # raise Exception(resp_data)
        return resp_data
    return resp_data["data"]


def save(data=None):
    if data is None:
        data = {
            "code": "code",
            "title": "标题",
            "authorCode": "作者",
            "abstract": "摘要",
            "content": "### 这是一个标题",
            "category": "tech",
        }
    return article_fetch('/save', data)


def article_fetch(url, data=None, method="post", params=None):
    # return fetch('http://118.25.154.161:5000/article' + url, data=data, method=method, params=params)
    return fetch('http://localhost:5000/article' + url, data=data, method=method, params=params)


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


for dir in list(dirMap.keys()):
    dirname = os.path.join(rootdir, dir)
    dirs = os.listdir(dirname)
    files = [os.path.join(rootdir, dir, elem)
             for elem in dirs if elem.endswith('.md') and not elem.startswith('quiz-')]
    for file in files:
        content = open(file, 'r', encoding='utf-8').readlines(20)
        metadata = getmeta(content)
        if metadata is None:
            print(file)
            continue
        metadata['category'] = 'tech:' + dir
        metadata['content'] = open(file, 'r', encoding='utf-8').read()
        save(data=metadata)
