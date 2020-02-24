---
# Redis 常见问题

## Redis firewall setting

```bash
firewall-cmd --zone=public --add-port=6379/tcp --permanent
firewall-cmd --reload
/etc/init.d/redisd stop
redis-server /etc/redis/6379.conf &
```
