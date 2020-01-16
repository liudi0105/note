---
author: liudi
createTime: 2020-01-13
updateTime: 2020-01-13
---

# 压缩/解压缩

```bash
tar zxvf file.tar.gz outdir/
tar zcvf file.tar.gz indir/
tar xvJf file.tar.gz outdir/
tar cvjf file.tar.bz2 indir/
tar xvjf file.tar.bz2 outdir/
```

# install MySQL for CentOS

```bash
wget -i -c http://dev.mysql.com/get/mysql57-community-release-el7-10.noarch.rpm
yum -y install mysql57-community-release-el7-10.noarch.rpm
yum -y install mysql-community-server
yum clean all
yum makecache
set global validate_password_policy=0;
yum -y remove mysql57-community-release-el7-10.noarch
GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' IDENTIFIED BY '123456' WITH GRANT OPTION;
GRANT ALL PRIVILEGES ON *.* TO 'jack'@’10.10.50.127’ IDENTIFIED BY '654321' WITH GRANT OPTION;
```

# 修改MySQL密码

```bash
mysqld --skip-grant-tables
update user set authentication_string = password('root'), password_expired = 'N', password_last_changed = now() where user = 'root';
```

# 本地端口映射

```bash
ssh -L 0.0.0.0:9229:localhost:9222 localhost -N
```

# 命令提示符

```bash
export PS1='\[\e]0;\u@\h: \w\a\]\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\$ '

export PS1="\[\e]0;\u@\h:\w\a\]\[\033[37;45m\]\u@\h\[\033[35;46m\]\[\033[01;37;46m\]\w\[\033[00;36;40m\]\[\033[00m\] "
```

# aliyun apt source list for ubuntu

```
deb http://mirrors.aliyun.com/ubuntu/ bionic main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ bionic main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ bionic-security main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ bionic-security main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ bionic-updates main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ bionic-updates main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ bionic-backports main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ bionic-backports main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ bionic-proposed main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ bionic-proposed main restricted universe multiverse
```

# set python package source list

```
清华：https://pypi.tuna.tsinghua.edu.cn/simple
阿里云：http://mirrors.aliyun.com/pypi/simple/
中国科技大学 https://pypi.mirrors.ustc.edu.cn/simple/
华中理工大学：http://pypi.hustunique.com/
山东理工大学：http://pypi.sdutlinux.org/ 
豆瓣：http://pypi.douban.com/simple/

~/.pip/pip.conf
[global]
index-url = https://pypi.douban.com/simple/
[install]
trusted-host=pypi.douban.com
```

# Git 常用设置

```bash
git config --global core.filemode false
git config --global --add core.filemode false
git config --global alias.sub 'submodule foreach git'
git config --global alias.s 'status'
git config --global core.autocrlf input
git config --global credential.helper store
```



