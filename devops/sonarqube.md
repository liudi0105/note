# Docker 安装 Sonarqube

## 拉取 Sonarqube 镜像

```bash
docker pull sonarqube
```

## 运行 Sonarqube

```bash
docker run -d --name sonarqube \
  -p 9000:9000 \
  -e sonar.jdbc.username=USERNAME \
  -e sonar.jdbc.password=PASSWORD \
  -e sonar.jdbc.url=URL \
  -v /var/lib/docker/volumes/sonarqube/logs:/opt/sonarqube/logs \
  -v /var/lib/docker/volumes/sonarqube/data:/opt/sonarqube/data \
  -v /var/lib/docker/volumes/sonarqube/conf:/opt/sonarqube/conf \
  -v /var/lib/docker/volumes/sonarqube/extensions:/opt/sonarqube/extensions \
  sonarqube
```
