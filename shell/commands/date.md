

```bash
## 将日期转换为Unix时间戳
# 将当前时间以Unix时间戳表示, seconds since 1970-01-01 00:00:00 UTC
date +%s
# 转换指定日期为Unix时间戳：
date -d '2017-04-11 10:00:00' +%s

## 将Unix时间戳转换为日期时间
# 不指定日期时间的格式
date -d @1491876000
# 指定日期格式的转换
date -d @1491876000 +"%Y-%m-%d %H:%M:%S"
# 三天之前（mac上不能执行）
date +%Y%m%d --date '3 days ago'


now=`date +%Y%m%d`
seconds=`date -d "$now" +%s`

# delete 7 days ago
seven_day_seconds=$[3600*24*7]
seven_day_ago_seconds=$[seconds-$seven_day_seconds]
seven_day_ago=`date -d @$seven_day_ago_seconds "+%Y/%m/%d"`

echo "now=$now, seven_day_ago=$seven_day_ago"


# date -d next monday'（下周一的日期）
# date -d next-day +%Y%m%d（明天的日期）
# date -d tomorrow +%Y%m%d
# date -d last-day +%Y%m%d（昨天的日期） 
# date -d yesterday +%Y%m%d
# date -d last-month +%Y%m（上个月是几月）
# date -d next-month +%Y%m（下个月是几月）

# date -d ’dec 14 -2 weeks’ （相对：dec 14这个日期的两周前的日期）
# date -d ’-100 days’ （100天以前的日期）
# date -d ’50 days’（50天后的日期）

```