# rsync server 搭建

## 配置文件

```bash
cat /etc/xinetd.d/rsync
# default: off
# description: The rsync server is a good addition to an ftp server, as it \
# allows crc checksumming etc.
service rsync
{
  disable = yes
  flags   = IPv6
  socket_type     = stream
  wait            = no
  user            = root
  server          = /usr/bin/rsync
  server_args     = --daemon
  log_on_failure  += USERID
}


cat /etc/rsyncd.conf
pid file = /var/run/rsyncd.pid
lock file = /var/run/rsync.lock
log file = /var/log/rsync.log
uid = nobody
gid = nobody
port = 873
max connections = 4

[public]
path = /data/public_rsync
comment = RSYNC FILES
read only = no
timeout = 300
list = yes
uid = xiaoqiang
gid = xiaoqiang
```

## systemctl 配置
```bash

# 执行生成rsyncd.service文件
systemctl enable rsyncd.service

# systemctl启动配置
cat /usr/lib/systemd/system/rsyncd.service
[Unit]
Description=fast remote file copy program daemon
ConditionPathExists=/etc/rsyncd.conf

[Service]
EnvironmentFile=/etc/sysconfig/rsyncd
ExecStart=/usr/bin/rsync --daemon --no-detach "$OPTIONS"

[Install]
WantedBy=multi-user.target

# 命令执行
systemctl status rsyncd.service
systemctl start rsyncd.service
systemctl stop rsyncd.service
systemctl list-units --type=service
journalctl -f或者 journalctl -xe # 查看日志
```

## 启动

```bash
sudo rsync --daemon
/etc/init.d/xinetd restart
```

## 测试
```bash
rsync -rdt rsync://IPADDR:RsyncPort/
rsync -rdt rsync://IPADDR:RsyncPort/DirectoryName/File /DestinationDirectory/
```

## Adding Usernames and Passwords to the Rsync Daemon
```bash
cat /etc/rsyncd.conf
[files]
path = /home/public_rsync
comment = RSYNC FILES
read only = true
timeout = 300
auth users = rsync1,rsync2
secrets file = /etc/rsyncd.secrets


cat /etc/rsyncd.secrets
rsync1:9$AZv2%5D29S
rsync2:Xyb#vbfUQR0o
rsync3:VU&A1We5DEa8

chmod 600 /etc/rsyncd.secrets

rsync -rdt rsync://rsync1@IPADDR:RsyncPort/DirectoryName/File /DestinationDirectory/

# Just remember that authorized users must appear in both the /etc/rsyncd.conf and the /etc/rsyncd.secrets files.

```

## 带密码的测试

```bash
# 第一种方式

echo '123!@#' > zgq.pwd
chmod 600 zgq.pwd
rsync -vzrtpogl  --password-file=/home/zgq/zgq.pwd --exclude=.*  /home/zgq/test.sql  zgq@hxs1::public/tmp/

# 将server（ip）上的文件rah_20170223同步到本地的/data/tmp/data/目录
rsync -vrtl --progress  --password-file=/home/hadoop/.rsync/my.pwd rsync1@ip::files/collect/rah_20170223.d /data/tmp/data/


# 第二种方式
export RSYNC_PASSWORD='123!@#'
rsync -vzrtpogl --exclude=.*  /home/zgq/test.sql  zgq@hxs1::public/tmp/

```

## 参考网址

> https://www.atlantic.net/community/howto/setup-rsync-daemon/

# rsync 2种登录认证协议

## ssh认证协议

> rsync server 端不用启动rsync的daemon进程，只要获取remote host的用户名和密码就可以直接 rsync 同步文件

> rsync server 端因为不用启动daemon进程，所以也不用配置文件 /etc/rsyncd.conf

> ssh 认证协议跟scp 的原理是一样的，如果在同步过程中不需要收入密码就 用 ssh-keygen -t rsa 打通通道

```bash
这种方式默认是省略了 -e ssh 的，与下面等价：  
rsync -avz /SRC -e ssh root@ip:/DEST # -a 文件宿主变化，时间戳不变 -z：压缩数据传输  

当遇到要修改端口的时候，我们可以：  
rsync -avz /SRC -e "ssh -p36000" root@ip:/DEST  #修改了ssh 协议的端口，默认是22
```

## rsync 认证协议

> rsync 认证协议，需要在rsync server端启动daemon进程，并设置对应的配置文件: /etc/rsyncd.conf
> rysnc 认证协议，如果不需要输入密码需要设置下面的配置： 如上

```bash
# rsync 2种协议用法：  
rsync -av /SRC rsync://root@ip:port/modual/DestPath  

# 注意：这条语句显示的指明了使用rsync认证协议，port后的modual是rsync服务端配置文件rsyncd.conf  
# 里面配置的模块名，模块里面会包含一些用户名、密码、路径等认证信息。  

rsync -av /SRC --port=36000 root@ip::modual/DestPath  

# 注意：这种写法不需显示指定 rsync 协议，而是根据 :: 来识别的，端口自己用 --port 指定。  
# 而且这里 modual 前面没有 / 的。

```

# 常用命令

```bash
# 同步指定文件
# --bwlimit 限制带宽
rsync -vzrtpogl --include=*.log --exclude=* --delete --delete-after --bwlimit=2049 -e ssh xxx@port:/data/logs/  dest_path


echo "RSYNC BEGIN : "$(date)
while read readline;do
  ip_info=`echo $readline | awk '/^[1-9]/ {print $1}' | awk -F \: '{print $1}'`
  port_info=`echo $readline | awk '/^[1-9]/ {print $1}' | awk -F \: '{print $2}'`
  if [ "" != "$ip_info" ] ;then
    echo -ne "\n${ip_info}:${port_info}----:\n"
    rsync -vzrtpogl --exclude=.* --exclude=.svn --delete --delete-after -e "ssh -p${port_info}" /data/webroot/ root@${ip_info}:/data/webroot/
    echo "----"
  fi 
done < ./ip_list.info
echo "RSYNC END : "$(date)

```