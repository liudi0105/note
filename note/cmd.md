---
author: liudi
createTime: 2020-01-13
updateTime: 2020-01-13
---

# 常用命令

## 压缩/解压缩

```bash
tar zxvf file.tar.gz outdir/
tar zcvf file.tar.gz indir/
tar xvJf file.tar.gz outdir/
tar cvjf file.tar.bz2 indir/
tar xvjf file.tar.bz2 outdir/
```

## 本地端口映射

```bash
ssh -L 0.0.0.0:9229:localhost:9222 localhost -N
```

## 命令提示符

```bash
export PS1='\[\e]0;\u@\h: \w\a\]\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\$ '

export PS1="\[\e]0;\u@\h:\w\a\]\[\033[37;45m\]\u@\h\[\033[35;46m\]\[\033[01;37;46m\]\w\[\033[00;36;40m\]\[\033[00m\] "
```

## aliyun apt source list for ubuntu

```text
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

## Git 常用设置

```bash
git config --global core.filemode false
git config --global --add core.filemode false
git config --global alias.sub 'submodule foreach git'
git config --global alias.s 'status'
git config --global core.autocrlf input
git config --global credential.helper store
```
