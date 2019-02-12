# install

## mac install
```bash
brew install redis
# 配置文件
/usr/local/etc/redis.conf

# 可在redis.conf 中的requirepass 设置密码

# 启动服务
sudo ./redis-server

# 客户端登录
redis-cli -h 127.0.0.1 -p 6379 -a XXX

```