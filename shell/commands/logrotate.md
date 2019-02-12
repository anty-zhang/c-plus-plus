# logrotate 使用

参数说明

monthly: 日志文件将按月轮循。其它可用值为‘daily’，‘weekly’或者‘yearly’。

rotate 5: 一次将存储5个归档日志。对于第六个归档，时间最久的归档将被删除。

compress: 在轮循任务完成后，已轮循的归档将使用gzip进行压缩。

delaycompress: 总是与compress选项一起用，delaycompress选项指示logrotate不要将最近的归档压缩，压缩将在下一次轮循周期进行。这在你或任何软件仍然需要读取最新归档时很有用。

missingok: 在日志轮循期间，任何错误将被忽略，例如“文件无法找到”之类的错误。

notifempty: 如果日志文件为空，轮循不会进行。

create 644 root root: 以指定的权限创建全新的日志文件，同时logrotate也会重命名原始日志文件。

postrotate/endscript: 在所有其它指令完成后，postrotate和endscript里面指定的命令将被执行。在这种情况下，rsyslogd 进程将立即再次读取其配置并继续运行。

上面的模板是通用的，而配置参数则根据你的需求进行调整，不是所有的参数都是必要的。

```bash
实例
# 执行任务在 /etc/cron.daily/logrotate*

cd /etc/logrotate.d
cat recommend_data_collect.log
/data/logs/recommend_data_collect.log {
    daily
    missingok
    rotate 7
    notifempty
    dateext
    create 664 root root
    sharedscripts
    postrotate
        /usr/bin/killall -HUP rsyslogd
    endscript
}

```