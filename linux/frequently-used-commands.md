# Linux 下常用命令

```bash
# 初始显示 100 行，跟踪文件变化
tail -n 100 -f

# 显示当前已登录的所有实例
who

# 查看当前登录的实例用户信息
who -m

# 查看当前登录的用户名
whoami

# 查看系统硬盘空间使用情况
df -h

# 查看 pattern 相关进程的信息
ps aux | grep $pattern

# 查看 pattern 相关的进程信息
pgrep $pattern -a

# 查看 端口占用
netstat -tunlp
ss -lntp
```
