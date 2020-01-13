---
author: liudi
createTime: 2020-01-13
updateTime: 2020-01-13
---

#### CentOS 下 MySQL5.7 忘记密码

```
[root@localhost ~]# vi /etc/my.cnf
# For advice on how to change settings please see # http://dev.mysql.com/doc/refman/5.7/en/server-configuration-defaults.html [mysqld] # # Remove leading # and set to the amount of RAM for the most important data # cache in MySQL. Start at 70% of total RAM for dedicated server, else 10%. # innodb_buffer_pool_size = 128M # # Remove leading # to turn on a very important data integrity option: logging # changes to the binary log between backups. # log_bin # # Remove leading # to set options mainly useful for reporting servers. # The server defaults are faster for transactions and fast SELECTs. # Adjust sizes as needed, experiment to find the optimal values. # join_buffer_size = 128M # sort_buffer_size = 2M # read_rnd_buffer_size = 2M datadir=/var/lib/mysql socket=/var/lib/mysql/mysql.sock skip-grant-tables  # Disabling symbolic-links is recommended to prevent assorted security risks  
[root@localhost ~]# systemctl restart mysqld.service [root@localhost ~]# mysql
mysql>update mysql.user set authentication_string=password('新密码') where user='root' ; mysql>flush privileges ; mysql>quit
[root@localhost ~]# systemctl restart mysqld.service
```

#### MySQL中文乱码

```
vim /etc/my.ini
[mysqld]
character-set-server=utf8  collation-server=utf8_general_ci 
```

