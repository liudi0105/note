---
author: liudi
createTime: 2020-01-13
updateTime: 2020-01-13
---

# 常用命令

```bash
sudo groupadd docker
sudo gpasswd -a $USER docker
sudo service docker restart
docker run --name bct-postgresql -e POSTGRES_USER=bct -e POSTGRES_PASSWORD=kEaLJ9ZERLLN -e POSTGRES_DB=bct -p 5432:5432 -d postgres:9-alpine -c max_connections=300
docker run --name bct-redis -p 6379:6379 -d redis:alpine
docker run -di --name=tensquare_rabbitmq -p 5671:5671 -p 5672:5672 -p 4369:4369 -p 15671:15671  -p 15672:15672 -p 25672:25672
docker run --name swagger-ui -p 5005:8080 -d swaggerapi/swagger-ui -e SWAGGER_JSON=/foo/swagger.json
```

## windows_termianl_wsl2 --参考的对象类型不支持尝试的操作

```powershell
# wsl2 在使用 vpn 后会起不来，解决方案就是 cmd 下管理员权限执行
netsh winsock reset
```

## WSL2 安装 Docker

```powershell
# 开户 WSL
Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Windows-Subsystem-Linux
# 启用虚拟机平台
Enable-WindowsOptionalFeature -Online -FeatureName VirtualMachinePlatform
# 默认启用 WSL2
wsl --set-default-version 2
```

安装 Ubuntu

```bash
# 安装 Docker 依赖
sudo apt-get install apt-transport-https ca-certificates curl gnupg2 software-properties-common
# 安装 Docker 的GPG 公钥
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
# 对于 amd64 架构的计算机，添加软件仓库：
sudo add-apt-repository \
   "deb [arch=amd64] https://mirrors.tuna.tsinghua.edu.cn/docker-ce/linux/ubuntu \
   $(lsb_release -cs) \
   stable"
# 最后安装
sudo apt-get update
sudo apt-get install docker-ce
# 测试
docker run hello-world
# 将当前用户添加到 docker 用户组
sudo adduser $USER docker
# 启用 Docker 服务
sudo service docker start
# 测试
docker run hello-world
```

## 更换国内源

`/etc/docker/daemon.json`

```json
{
  "registry-mirrors": [
    "http://registry.docker-cn.com",
    "http://docker.mirrors.ustc.edu.cn",
    "http://hub-mirror.c.163.com"
  ],
  "insecure-registries": [
    "registry.docker-cn.com",
    "docker.mirrors.ustc.edu.cn"
  ],
  "debug": true,
  "experimental": true
}
```
