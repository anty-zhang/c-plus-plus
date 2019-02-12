# ssh 代理

```bash
#######################################################################
ssh 代理详细解释

SSH: Port Forwarding
1.正向隧道-隧道监听本地port,为普通活动提供安全连接
ssh -qTfnN -L port:host:hostport -l user remote_ip
ssh myserver -L 8888:localhost:8888


2.反向隧道----隧道监听远程port，突破防火墙提供服务
ssh -qTfnN -R port:host:hostport -l user remote_ip
3.socks代理
SSH -qTfnN -D port remotehost（用证书验证就直接主机名，没用的还要加上用户名密码）
-q Quiet mode. 安静模式，忽略一切对话和错误提示。
-T Disable pseudo-tty allocation. 不占用 shell 了。
-f Requests ssh to go to background just before command execution. 后台运行，并推荐加上 -n 参数。
-n Redirects stdin from /dev/null (actually, prevents reading from stdin). -f 推荐的，不加这条参数应该也行。
-N Do not execute a remote command. 不执行远程命令，专为端口转发度身打造。

#######################################################################
ssh实现转发, 只要用到以下两条命令: 
# ssh -CfNg -L 6300:127.0.0.1:1521 oracle@172.16.1.164
# ssh -CfNg -R 1521:127.0.0.1:6300 oracle@172.16.1.164
不论是做跳板, 还是加密隧道, 还是加密其他的网络连接也都是这两条命令. 视具体情况而定, 有时只要用到其中一条, 有时两条都要用到. 
-L 解释： 本机(运行这条命令的主机)打开6300端口, 通过加密隧道映射到远程主机172.16.1.164的1521端口(使用远程主机oracle用户). 在本机上用netstat -an|grep 6300可看到. 简单说,本机的6300端口就是远程主机172.16.1.164的1521端口. 
-R 解释：作用同上, 只是在远程主机172.16.1.164上打开1521端口, 来映射本机的6300端口. 

命令解释: 

1) -CfNg
C表示压缩数据传输
f表示后台用户验证,这个选项很有用,没有shell的不可登陆账号也能使用.
N表示不执行脚本或命令
g表示允许远程主机连接转发端口


实用例子

有A,B,C 3台服务器, A,C有公网IP, B是某IDC的服务器无公网IP. A通过B连接C的80端口(A<=>B<=>C), 那么在B上执行如下命令即可: 
$ ssh -CfNg -L 6300:127.0.0.1:80 userc@C
$ ssh -CfNg -R 80:127.0.0.1:6300 usera@A
服务器A和服务器C之间, 利用跳板服务器B建立了加密隧道. 在A上连接127.0.0.1:80, 就等同C上的80端口. 需要注意的是, 服务器B上的6300端口的数据没有加密, 可被监听, 例: 

# tcpdump -s 0-i lo port 6300
```