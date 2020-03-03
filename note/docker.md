# Docker 常用命令

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

## CentOS 下安装 Docker

```bash
# 安装基础的工具yum-utils device-mapper-persistent-data lvm2
yum install -y yum-utils device-mapper-persistent-data lvm2
# 添加docker-ce yum仓库
yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
# 安装docker-ce
yum install docker-ce
```

## 更换国内源

`/etc/docker/daemon.json`

```json
{
  "registry-mirrors": [
    ["http://hub-mirror.c.163.com"],
    "http://registry.docker-cn.com",
    "http://docker.mirrors.ustc.edu.cn"
  ],
  "insecure-registries": [
    "registry.docker-cn.com",
    "docker.mirrors.ustc.edu.cn"
  ],
  "debug": true,
  "experimental": true
}
```

## Nginx Web 服务

```bash
docker run \
--name webserver \
-d -p 80:80 \
-v /root/workspace/webserver/nginx.conf:/etc/nginx/nginx.conf \
-v /root/workspace/react-demo/build:/usr/share/nginx/html \
nginx
```

## Gitlab

```bash
docker run --detach \
 -p 8443:443 \
 -p 80:80 \
 -p 10022:22 \
 --name gitlab \
 --restart=unless-stopped \
 --volume /var/lib/docker/volumes/gitlab-data/etc:/etc/gitlab \
 --volume /var/lib/docker/volumes/gitlab-data/log:/var/log/gitlab \
 --volume /var/lib/docker/volumes/gitlab-data/data:/var/opt/gitlab \
 gitlab/gitlab-ce
```

## 修改 gitlab.rb 配置文件

/var/lib/docker/volumes/gitlab-data/etc/gitlab.rb

```rb
## GitLab NGINX

nginx['listen_port'] = 80 # gitlab nginx 端口。默认端口为：80

## GitLab Unicorn

unicorn['listen'] = 'localhost'
unicorn['port'] = 8080 #默认是 8080 端口

## GitLab URL 配置 http 协议所使用的访问地址

external_url 'http://song.local' # clone 时显示的地址，gitlab 的域名

# 配置 ssh 协议所使用的访问地址和端口

gitlab_rails['gitlab_ssh_host'] = 'song.local'
gitlab_rails['gitlab_shell_ssh_port'] = 10022
```

## Jenkins

```bash
docker run -p 8008:8080 -v /var/lib/docker/volumes/jenkins:/var/jenkins_home --name jenkins -d jenkins
```
