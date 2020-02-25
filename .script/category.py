import os

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
filedict = {}
for dir in list(dirMap.keys()):
    dirname = os.path.join(rootdir, dir)
    dirs = os.listdir(dirname)
    filedict[dir] = [os.path.join(rootdir, dir, elem)
                     for elem in dirs if elem.endswith('.md')]

print(filedict)
