# 常用命令速查

## 压缩/解压缩

```bash
tar zxvf file.tar.gz outdir/
tar zcvf file.tar.gz indir/
tar xvJf file.tar.xz outdir/
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

## Ubuntu 设置阿里云源

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

## Git 常用设置

```bash
git config --global core.filemode false
git config --global --add core.filemode false
git config --global alias.sub 'submodule foreach git'
git config --global alias.s 'status'
git config --global core.autocrlf input
git config --global credential.helper store
```

## chrome debug 模式启动

```bash
chrome --remote-debugging-port=9222
```

## Redis 防火墙设置

```bash
firewall-cmd --zone=public --add-port=6379/tcp --permanent
firewall-cmd --reload
/etc/init.d/redisd stop
redis-server /etc/redis/6379.conf &
```

## conda 国内源

```
- https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/
- https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
- https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge/
- https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/pytorch/ ssl_verify: true
  channels:
- https://mirrors.sjtug.sjtu.edu.cn/anaconda/pkgs/main/
- https://mirrors.sjtug.sjtu.edu.cn/anaconda/pkgs/free/
- https://mirrors.sjtug.sjtu.edu.cn/anaconda/cloud/conda-forge/ ssl_verify: true
  channels:
- https://mirrors.ustc.edu.cn/anaconda/pkgs/main/
- https://mirrors.ustc.edu.cn/anaconda/pkgs/free/
- https://mirrors.ustc.edu.cn/anaconda/cloud/conda-forge/ ssl_verify: true
```

```bash
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
conda config --set show_channel_urls yes
```

channels:

## set python package source list

```
清华：https://pypi.tuna.tsinghua.edu.cn/simple
阿里云：http://mirrors.aliyun.com/pypi/simple/
中国科技大学 https://pypi.mirrors.ustc.edu.cn/simple/
华中理工大学：http://pypi.hustunique.com/
山东理工大学：http://pypi.sdutlinux.org/
豆瓣：http://pypi.douban.com/simple/
```

linux 下编辑 ~/.pip/pip.conf

windows 下编辑 ~/pip/pip.ini 如不生效，编辑 %APPDATA%/pip/pip.ini

```conf
[global]
index-url = https://pypi.douban.com/simple/
[install]
trusted-host=pypi.douban.com
```

## 禁用笔记本自带键盘

```bat
sc config i8042prt start=disabled
sc config i8042prt start=auto
```

## maven install file

```bash
mvn install:install-file -DgroupId=javax.transaction -DartifactId=jta -Dpackaging=jar -Dversion=1.0.1B -Dfile=ojdbc14-10.2.0.1.0.jar -DgeneratePom=true -DarchetypeCatalog=internal
```

## MySQL 常见问题的解决办法

### install MySQL for CentOS

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

### 修改 MySQL 密码

```bash
mysqld --skip-grant-tables
update user set authentication_string = password('root'), password_expired = 'N', password_last_changed = now() where user = 'root';
```

### MySQL 中文乱码

```ini
# vim /etc/my.ini
[mysqld]
character-set-server=utf8  collation-server=utf8_general_ci
```

### 从 Git 仓库中删除已被管理的文件

```bash
git filter-branch --force --index-filter 'git rm --cached --ignore-unmatch "testFolder/2017-2-5 testFile.md" ' --prune-empty --tag-name-filter cat -- --all
git push origin --force --all
git push origin --force --tags
git for-each-ref --format='delete %(refname)' refs/original | git update-ref --stdin
git reflog expire --expire=now --all
git gc --prune=now
git count-objects -v
```

### Yarn 和 NPM 国内源

```bash
npm config set registry https://registry.npm.taobao.org
npm config set disturl https://npm.taobao.org/dist
npm config set electron_mirror https://npm.taobao.org/mirrors/electron/
npm config set sass_binary_site https://npm.taobao.org/mirrors/node-sass/
npm config set phantomjs_cdnurl https://npm.taobao.org/mirrors/phantomjs/

yarn config set registry https://registry.npm.taobao.org -g
yarn config set disturl https://npm.taobao.org/dist -g
yarn config set electron_mirror https://npm.taobao.org/mirrors/electron/ -g
yarn config set sass_binary_site https://npm.taobao.org/mirrors/node-sass/ -g
yarn config set phantomjs_cdnurl https://npm.taobao.org/mirrors/phantomjs/ -g
yarn config set chromedriver_cdnurl https://cdn.npm.taobao.org/dist/chromedriver -g
yarn config set operadriver_cdnurl https://cdn.npm.taobao.org/dist/operadriver -g
yarn config set fse_binary_host_mirror https://npm.taobao.org/mirrors/fsevents -g
```

java -jar worktrans-mes-gateway-1.0.0-RELEASE-dev.jar --eureka.client.serviceUrl.defaultZone=http://192.168.20.80:8888/eureka/

nohup java -Xms512m -Xmx512m -jar "\${item}" >/dev/null 2>&1 &

nohup java -jar "\${item}" >/dev/null 2>&1 &

nohup java -jar --eureka.client.serviceUrl.defaultZone=http://192.168.20.80:8888/eureka/ worktrans-mes-gateway-1.0.0-RELEASE-dev.jar >/dev/null 2>&1 &
