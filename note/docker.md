#### 常用命令

```bash
sudo groupadd docker
sudo gpasswd -a ${USER} docker
sudo service docker restart
docker run --name bct-postgresql -e POSTGRES_USER=bct -e POSTGRES_PASSWORD=kEaLJ9ZERLLN -e POSTGRES_DB=bct -p 5432:5432 -d postgres:9-alpine -c max_connections=300
docker run --name bct-redis -p 6379:6379 -d redis:alpine
docker run -di --name=tensquare_rabbitmq -p 5671:5671 -p 5672:5672 -p 4369:4369 -p 15671:15671  -p 15672:15672 -p 25672:25672
docker run --name swagger-ui -p 5005:8080 -d swaggerapi/swagger-ui -e SWAGGER_JSON=/foo/swagger.json
```

