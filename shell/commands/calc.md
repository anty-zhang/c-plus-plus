# shell数学运算
```bash
expr 1 + 2
3
```

# 部分运算符需要转义
```bash
# 需要进行转义
expr 2 \* 3
6

var1=10
var2=20
res=`expr $var2 / $var1`
echo The result is $res
The result is 2
```

# 使用[] 计算
```bash
# $符和[]将某个结果赋值给某个变量
var1=$[1 + 2]
echo $var1

var2=$[$var1 * 2]
echo $var2
3
6

```

# bash 中浮点运算

```bash
# bash中只支持浮点运算
var1=100
var2=45
res=$[$var1 / $var2]
echo "the result is $res"
the result is 2


# bc解决浮点数
# scale 控制小数位,默认为0
# 格式: res=`echo "options: expression" | bc`

res=`echo "scale=4; 3.44 / 5" | bc`
echo "res: $res"
res: .6880
In [20]:
%%bash
if false; then
    variable=`bc << EOF
        options
        statements
        expressions
        EOF
    `
fi

var1=10.46
var2=43.67
var3=33.2
var4=71

var5=`bc << EOF
scale=4
a1=($var1 * $var2)
a2=($var3 * $var4)
a1 + a2
EOF
`

echo "var5: $var5"
var5: 2813.9882

```