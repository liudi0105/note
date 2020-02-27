# Jenkins 安装

## 拉取 Jenkins 的 Docker 镜像

```bash
docker pull jenkinsci/blueocean
```

## 运行 Jenkins

```bash
docker run \
  --name jenkins \
  --privileged=true \
  -d \
  -p 8008:8080 \
  -p 50000:50000 \
  -v /var/lib/docker/volumes/jenkins:/var/jenkins_home \
  -v /var/run/docker.sock:/var/run/docker.sock \
  jenkinsci/blueocean
```

## 出现 `Wrong volume permissions` 问题

```bash
sudo chown -R 1000 /var/lib/docker/volumes/jenkins

chmod 777 /var/run/docker.sock

docker run -d --name sonarqube -p 9000:9000 sonarqube
```
