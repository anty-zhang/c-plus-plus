

```bash

:<<!
    变量
!

if false; then
    变量
    $$ Shell本身的PID（ProcessID） 
    $! Shell最后运行的后台Process的PID 
    $? 最后运行的命令的结束代码（返回值） 
    $- 使用Set命令设定的Flag一览 
    $* 所有参数列表。如"$*"用「"」括起来的情况、以"$1 $2 … $n"的形式输出所有参数。 
    $@ 所有参数列表。如"$@"用「"」括起来的情况、以"$1" "$2" … "$n" 的形式输出所有参数。 
    $# 添加到Shell的参数个数 
    $0 Shell本身的文件名 
    $1～$n 
    添加到Shell的各参数值。$1是第1参数、$2是第2参数…。 
    超过9个参数时, 在程序中可以通过 ${10} 获取
    
    basename 获取程序名而不包括路径
    ${$#}: 获取最后一个参数变量值, 必须换成 ${!#}, 当输入的参数为0时, ${!#}会返回命令行用到的脚本名
    shift: 移位运算符
    
    getopt
    getopts
    
    read -s -p "Enter your password: " pass   # 隐士读取
    read -t 5 -p "Enter your name: " name     # 超时
    
fi

# Enter posix mode for bash
set -o posix

echo $0

echo $$
echo $!
echo $?
echo $-

echo $#
  File "<ipython-input-5-0802c17d2fd2>", line 3
    :<<!
    ^
SyntaxError: invalid syntax

```


# 路径结算

```bash

fwdir="$(cd "`dirname "$0"`"/..; pwd)"
echo $fwdir
/home/xiaoqiang/Documents

cat file | while read line
do
    # todo other cmds
done
```

# 标准输入输出

```bash
每个过程最多可以有9个文件描述符

exec 3 > test3out   # 创建自己的重定向

exec 3 > &1         # 将自定义描述符3重定向到标准输出


# 创建输入描述符

exec 6 <&0
exec 0 < testfile

# 关闭文件描述符
exec 3 > &-


tee: 输出到控制台,并输出到制定文件中

```
