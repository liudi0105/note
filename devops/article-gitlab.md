# Gitlab 安装

## 拉取 Gitlab Docker 镜像

```bash
docker pull gitlab/gitlab-ce
```

## 运行 Gitlab 镜像

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
