
# netstat

```bash
# 查看本地路由表
netstat -nr

# 查看当前建立的网络连接
netstat -lnpt

```

# lsof

# ss

> ss命令可以用来获取socket统计信息，它可以显示和netstat类似的内容。但ss的优势在于它能够显示更多更详细的有关TCP和连接状态的信息，而且比netstat更快速更高效。当服务器的socket连接数量变得非常大时，无论是使用netstat命令还是直接cat /proc/net/tcp，执行速度都会很慢。可能你不会有切身的感受，但请相信我，当服务器维持的连接达到上万个的时候，使用netstat等于浪费 生命，而用ss才是节省时间。 天下武功唯快不破。ss快的秘诀在于，它利用到了TCP协议栈中tcp_diag。tcp_diag是一个用于分析统计的模块，可以获得Linux 内核中第一手的信息，这就确保了ss的快捷高效。当然，如果你的系统中没有tcp_diag，ss也可以正常运行，只是效率会变得稍慢。

## 常用参数

```bash
-l 查看处于LISTEN状态的连接
-t 查看tcp连接
-4 查看ipv4连接
-n 不进行域名解析

# 实例
# ss命令查看本地监听的所有端口和netstat命令功能类似
ss  -t -l -n -4

```

# telnet

```bash
# 实例
# 查看本地端口22是否开放
telnet localhost 22

```

# nc

> nc(netcat)被称为网络工具的瑞士军刀，其非常轻巧但功能强大！常常作为网络应用的Debug分析器，可以根据需要创建各种不同类型的网络连接

```bash
实例
# 我要扫描ip主机1~100端口
nc -zv ip 1-100 |& grep 'succeeded!'

```