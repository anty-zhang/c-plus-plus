# awk

```
数据字段和数据行变量
FIELDWIDTHS    由空格分割开的定义了每个数据字段确切宽度的一系列数字
    FS             输入分隔符
    OFS            输出分隔符
    RS             输入数据行分隔符,默认换行符
    ORS            输出数据行分隔符,默认换行符


    ARGC           当前命令行参数个数
    ARGV           命令行参数数组
    ARGIND         当前文件在ARGV中的位置

    CONVFMT        数字转换格式
    ENVIRON        当前shell环境变量及其组成的关联数组
    NF
    NR
    FNR
```

# examples

```bash
# printf 格式化
# echo 和awk 修改分隔符为\0001

echo "test" | awk -v OFS='\001' '{print $1,$2,$3}'

cat ./data2.d
data11.data12.data13
data21.data22.data23
data31.data32.data33

awk 'BEGIN {FS="."} {print $1,$2,$3}' ./data2.d
data11 data12 data13
data21 data22 data23
data31 data32 data33

awk 'BEGIN {FS="."; OFS="-"} {print $1,$2,$3}' ./data2.d
data11-data12-data13
data21-data22-data23
data31-data32-data33


cat ./data3.d
1005.3247596.37
115-2.349194.00
05810.1298100.1
In [16]:
%%bash

# 再以后gawk才支持

awk 'BEGIN {FIELDWIDTHS="3 5 2 5"} {print $1,$2,$3,$4}' ./data3.d
1005.3247596.37   
115-2.349194.00   
05810.1298100.1

awk 'BEGIN {print ARGC,ARGV[1]}' ./data3.d

awk 'BEGIN {print ENVIRON["HOME"]; print ENVIRON["PATH"]}'
2 ./data3.d

# 正则表达式匹配

awk 'BEGIN {FS="."} /11/{print $1}' ./data2.d
data11

# ~ 匹配操作符

# 按着.分割后,取第二个字段以data2开头,并打印
awk 'BEGIN {FS="."} $2 ~ /^data2/{print $0}' ./data2.d
data21.data22.data23

# 用! 符号来排除正则表达式匹配
awk -F. '$2 !~ /^data2/{print $0}' ./data2.d
data11.data12.data13
data31.data32.data33

# 使用表达式
awk -F. '$1 == "data11" {print $0}' ./data2.d
data11.data12.data13


cat ./data4.d
10
5
13
50
34

# if 条件
awk '{if ($1 > 20) print $1}' ./data4.d
50
34

awk '{if ($1 > 20) {x=$1 * 2; print x} else {x=$1 / 2; print x} }' ./data4.d
5
2.5
6.5
100
68

awk '{if ($1 > 20) print $1 * 2; else print $1 / 2 }' ./data4.d
5
2.5
6.5
100
68

cat ./data5.d
130 120 135
160 113 140
145 170 215

# for 

awk '{total=0; i=1; while (i < 4) {total += $i; i++} ; avg = total / 3; print "Average:",avg}' ./data5.d
Average: 128.333
Average: 137.667
Average: 176.667

```