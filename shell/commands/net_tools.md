# mtr简单应用

- mtr在某些方面比traceroute更好用，它可以实时显示经过的每一跳路由的信息，并不断进行探测。

- traceroute默认使用UDP数据包探测，而mtr默认使用ICMP报文探测，ICMP在某些路由节点的优先级要比其他数据包低，所以测试得到的数据可能低于实际情况。

```bash
sudo mtr -rw baidu.com
Start: Tue Apr 11 16:22:08 2017
HOST: localhost                          Loss%   Snt   Last   Avg  Best  Wrst StDev
  1.|-- ???                                100.0    10    0.0   0.0   0.0   0.0   0.0
  2.|-- aca86401.ipt.aol.com               90.0%    10   30.6  30.6  30.6  30.6   0.0
  3.|-- 241.48.110.36.static.bjtelecom.net  0.0%    10   38.4  25.0   2.5  73.1  22.9
  4.|-- ???                                100.0    10    0.0   0.0   0.0   0.0   0.0
  5.|-- 220.181.0.234                      90.0%    10  214.9 214.9 214.9 214.9   0.0
  6.|-- 218.30.112.146                     60.0%    10    5.3  81.7   5.3 298.3 144.5
  7.|-- 180.149.128.154                    40.0%    10  691.7 281.1  23.0 691.7 284.7
  8.|-- 180.149.129.174                     0.0%    10   77.7  50.6   3.6 168.7  47.8
  9.|-- ???                                100.0    10    0.0   0.0   0.0   0.0   0.0
 10.|-- 10.36.9.134                         0.0%    10   18.1  89.9   6.6 499.3 148.4
 11.|-- 180.149.132.47                      0.0%    10   68.0  53.9  11.0 176.7  49.1
xxxdeMacBook-Pro:groovy xxx$ ping baidu.com
PING baidu.com (180.149.132.47): 56 data bytes
64 bytes from 180.149.132.47: icmp_seq=0 ttl=55 time=13.863 ms
64 bytes from 180.149.132.47: icmp_seq=1 ttl=55 time=356.845 ms


第一列：显示的是IP地址和本机域名
第二列 Loss%：是显示的每个对应IP的丢包率。
第三列 snt：发送数据包的数量。
第四列 Last：显示的最近一次的返回延时。
第五列 Avg：平均值，发送数据包的平均延时。
第六列 Best：延时最短的数据包。
第七列 Wrst：延时最长的数据包。
第八列 StDev：标准偏差，标准偏差越高说明延迟波动越大，例如，如果最低延迟在25MS，最高在350MS，发送一定的包之后，平均延迟看上去平稳，但实际波动大，数据包会受到影响，如果标准偏差较大，确认延时最短数据包和延迟最长数据包。
# 当没有额外的路由信息时，将会显示问号（???）
# 有时候，一个错误配置的路由器，将会在一个环路中不断发送数据包
# 因为可能仅仅是第9跳设备限制了 ICMP 传输速率的原因。所以我们一般要用最后一跳的实际延迟为准。

```

# route

```bash
实例
# 查看路由表
route -n


# 增加/删除路由分别为add/del子命令,比如删除默认路由：
sudo route del default

# 增加默认路由，网关为192.168.1.1，网卡为1f：
sudo route add default gw 192.168.1.1 dev 1f
```

# ifconfig

```bash
实例
# 查看网卡ip地址
ifconfig eth0

# 为网卡eth0增加一个新的地址（虚拟网卡）：
sudo ifconfig eth0:0 10.103.240.2/24

# 关闭网卡以及开启网卡
sudo ifconfig eth0 down
sudo ifconfig eth0 up
```

# traceroute
```bash
实例
# 可以看到，从主机到test.com共经过n跳，并统计了每一跳间的响应时间。
sudo traceroute  -I -n test.com

```

# nslookup

```bash
nslookup用于交互式域名解析(query Internet name servers interactively)，当然也可以直接传入域名作为Ad-Hoc命令使用

实例
# 查看baidu.com的ip地址
nslookup baidu.com
Server:        172.168.200.110
Address:    172.168.200.110#53

Non-authoritative answer:
Name:    baidu.com
Address: 220.181.57.217
Name:    baidu.com
Address: 123.125.114.144
Name:    baidu.com
Address: 180.149.132.47
Name:    baidu.com
Address: 111.13.101.208

# 查看使用的DNS服务器地址
nslookup
> server
Default server: 172.168.200.110
Address: 172.168.200.110#53
Default server: 172.168.200.120
Address: 172.168.200.120#53

```

# dig

```bash
实例
dig baidu.com

```

# whois

```bash
实例
# whois用于查看域名所有者的信息(client for the whois directory service)，比如注册邮箱、手机号码、域名服务商等
whois baidu.com
```

# tcpdump

```bash
tcpdump(dump traffic on a network)是一个强大的命令行抓包工具，千万不要被它的名称误导以为只能抓取tcp包，它能抓任何协议的包。它能够实现Wireshark一样的功能，并且更加灵活自由

实例
# 需要抓取目标主机是192.168.56.1，通过端口22的传输数据包
sudo tcpdump -n -i eth1 'dst host 192.168.56.1 && port 22'

```