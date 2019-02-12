# 安装

```bash
wget wget https://pypi.python.org/packages/60/9a/8035af3a7d3d1617ae2c7c174efa4f154e5bf9c24b36b623413b38be8e4a/pssh-2.3.1.tar.gz

tar -zxvf pssh-2.3.1.tar.gz
cd pssh-2.3.1
python setup.py install
```

# pssh参数

pssh在多个主机上并行地运行命令

    -h 执行命令的远程主机列表,文件内容格式[user@]host[:port]
        如 test@172.16.10.10:229
    -H 执行命令主机，主机格式 user@ip:port
    -l 远程机器的用户名
    -p 一次最大允许多少连接
    -P 执行时输出执行信息
    -o 输出内容重定向到一个文件
    -e 执行错误重定向到一个文件
    -t 设置命令执行超时时间
    -A 提示输入密码并且把密码传递给ssh(如果私钥也有密码也用这个参数)
    -O 设置ssh一些选项
    -x 设置ssh额外的一些参数，可以多个，不同参数间空格分开
    -X 同-x,但是只能设置一个参数
    -i 显示标准输出和标准错误在每台host执行完毕后

# 附加工具

```bash
pscp 传输文件到多个hosts，类似scp
    pscp -h hosts.txt -l irb2 foo.txt /home/irb2/foo.txt
pslurp 从多台远程机器拷贝文件到本地
pnuke 并行在远程主机杀进程
    pnuke -h hosts.txt -l irb2 java
prsync 使用rsync协议从本地计算机同步到远程主机
    prsync -r -h hosts.txt -l irb2 foo /home/irb2/foo

```

# example

```bash
pssh -i -h ~/.pssh/all -P --par 1 date
pssh -x '-t -t -o StrictHostKeyChecking=no' -i -h host.txt date
pssh -x '-t -t -o StrictHostKeyChecking=no' -i -H 192.168.230.128 -H wul@10.0.0.8 date

# 标示将本地的/etc/sysconfig目录递归同步到目标服务器的 /tmp/etc目录下,并保持原来的时间戳,使用用户 dongwm
prsync -h test.txt -l dongwm -a -r /etc/sysconfig /tmp/etc 

# 标示将目标服务器的/tmp/network文件复制到本地的/tmp/test目录下,并更名为test
pslurp -h test.txt   -L /tmp/test -l root /tmp/network test

# 杀死目标服务器的syslog进程,只要ps进程中出现相关词语 都能杀死
pnuke -h test.txt   syslog
```