

[TOC]

# 安装

## mac
```bash
brew cask install docker

# 配置国内源
https://registry.docker-cn.com
http://141e5461.m.daocloud.io

```

# 镜像

## 基本操作

```bash
docker pull --help
docker pull [选项] [Docker Registry地址]<仓库名>:<标签>

Docker Registry地址:地址的格式一般是 <域名/IP>[:端口号] 。默认地址是 Docker Hub。
仓库名:如之前所说，这里的仓库名是两段式名称，既 。 对于 Docker Hub，如果不给出用户名，则默认为library，也就是官方镜像。

docker run -it --rm ubuntu:14.04 bash
docker images

# 悬空镜像
docker images -f dangling=true
# 删除悬空镜像
### docker rmi $(docker images -q -f dangling=true)

# 中间层镜像
docker images -a

# 查看mongo:3.2之后的镜像
docker images -f since=mongo:3.2
# 查看mongo:3.2之前的镜像
docker images -f before=mongo:3.2
# 镜像format输出
docker images --format "{{.ID}}: {{.Repository}}"
docker images --format "table {{.ID}}\t{{.Repository}}\t{{.Tag}}"

## docker commit---将容器的存储层保存下来成为镜像
docker run --rm --name webserver -d -p 80:80 nginx
docker exec -it webserver bash
echo '<h1>Hello, Docker!</h1>' > /usr/share/nginx/html/index.html
exit
curl http://localhost

docker diff webserver
docker commit --author "guoqiang@xxx.com"  -m 'echo hello' webserver nginx:v2

# 查看镜像历史
docker history nginx:v2
docker history nginx:latest
docker run --rm --name web2 -d -p 81:80 nginx:v2

```

## 使用dockerFile定制镜像

```bash
# dockerfile---修改，配置，安装，构建，操作命令脚本

```

## Dockerfile命令

```bash
每个指令都会建立一层

# FROM
scratch是虚拟镜像。静态编译类型可以使镜像体积变小

# RUN
shell 格式：RUN <命令> 
exec 格式：RUN <"可执行文件", "参数1", "参数2">

# COPY

# ADD
尽量用COPY

# CMD 只可以出现一次，如果写了多个， 只有最后一个生效。

# ENTRYPOINT 只可以出现一次，如果写了多个， 只有最后一个生效。
# ENV
# ARG
# VOLUME
# EXPOSE
# WORKDIR
# USER
# HEALTHCHECK 只可以出现一次，如果写了多个， 只有最后一个生效
# ONBUILD
# 

docker inspect --format '{{json .State.Health}}' web | python -m json.tool

docker build -t nginx:v3 .
"点" 是指定上下文路径
构建方式：
1）普通方式
2）git方式
3）tar方式
4）从标准输入中读取Dockerfile文件进行构建： docker build - < Docerfile 或者 cat Dockerfile build -
docker build - < xx.tar.gz

```

# 容器

## 基本操作

```bash
docker start docker stop docker restart docker attach docker nsenter

# 启动服务参数
# --mount:    表示要进行挂载
# source:     指定要运行部署的模型地址
# target:     这个是要挂载的目标位置
# -t:         指定的是挂载到哪个容器
# -d:         后台运行
# -p:         指定主机到docker容器的端口映射
# -e:         环境变量
# -v:         docker数据卷
# --name:     指定容器name，后续使用比用container_id更方便

# 启动容器
docker run -dit ubuntu

# 进入容器
docker attach containerid	# 如果从这个 stdin 中 exit，会导致容器的停止
docker exec -it 69d1 bash

# 查看运行容器
docker container ls
docker ps

# 查看全部容器
docker ps -a
docker save <repo_id:tag> > ubuntu.tar
docker save -o ubuntu.tar <repo_id:tag>
docker load < ubuntu.tar
docker load -i ubuntu.tar

```
