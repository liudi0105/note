---
author: liudi
createTime: 2020-01-13
updateTime: 2020-01-13
---

#### Redis firewall setting

```bash
firewall-cmd --zone=public --add-port=6379/tcp --permanent
firewall-cmd --reload
/etc/init.d/redisd stop
redis-server /etc/redis/6379.conf &
```

