# crontab 使用
## 格式

```bash
cat /etc/crontab 
SHELL=/bin/bash
PATH=/sbin:/bin:/usr/sbin:/usr/bin
MAILTO=root
HOME=/

# For details see man 4 crontabs

# Example of job definition:
# .---------------- minute (0 - 59)
# | .------------- hour (0 - 23)
# | | .---------- day of month (1 - 31)
# | | | .------- month (1 - 12) OR jan,feb,mar,apr ...
# | | | | .---- day of week (0 - 6) (Sunday=0 or 7) OR sun,mon,tue,wed,thu,fri,sat
# | | | | |
# * * * * * user-name command to be executed
该 文件下的前四行内容为crontab的环境变量，SHELL变量的值指定系统使用的SHELL环境（该样例为bash shell），PATH变量定义了执行命令的路径。Cron的输出以电子邮件的形式发给MAILTO变量定义的用户名。如果MAILTO变量定义为空字符 串（MAILTO=""），电子邮件不会被发送。执行命令或脚本时HOME变量可用来设置基目录。
注：以上系统会默认可以不用修改任何！

```

## 参数说明

```bash
除了数字还有几个个特殊的符号就是"*"、"/"和"-"、","，

*代表所有的取值范围内的数字

"/"代表每的意思

"*/5"表示每5个单位

"-"代表从某个数字到某个数字

","分开几个离散的数字。

以下举几个例子说明问题

# 比较容易犯的错误是通常会把每小时的第一分钟按做每分钟执行一次，这点要注意两者的区别：
1 * * * * /home/postgres/pgsql.sh    # 表示的是每小时的第一分钟执行该脚本
*/1 * * * * /home/postgres/pgsql.sh  # 表示的是每一分钟执行该脚本


1 * * * * /home/postgres/pgsql.sh    # 表示的是每小时的第一分钟执行该脚本
2 3 * * * /home/postgres/pgsql.sh   # 表示每天的3点零2分执行该脚本
1 1 * * 0 / home/postgres/pgsql.sh  # 表示的是每周日的1点1分进行脚本的执行
1 1 1 * * / home/postgres/pgsql.sh  # 表示的是每月的1点1分进行脚本的执行

0 10 * * 1-3 /home/postgres/pgsql.sh # 表示的是每个周一到周三的早上10点执行该脚本
0 10 * * 1,3,5 /home/postgres/pgsql.sh # 表示的是每周的周一、周三、周五的早上10点执行该脚本

```

## 配置说明

```bash
# 日志时间配置
15 10 * * * /bin/sh train.sh >> ./log/order-probability-$(date +"\%Y-\%m-\%d").log 2>&1
```