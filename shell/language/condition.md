# if then 条件

```bash
if cmd; then
    elif cmd; then

    elif cmd; then

    else
        cmds
    fi
```

# 两种方式test命令

```bash
# 格式
if test condition then

fi

if [ condition ] then

fi

# 可判断条件

　数值比较　（浮点数不能比较）

    -eq
    -gt
    -ge
    -lt
    -le
    -ne
字符串比较　

    ==
    !=
    <>
    -n str   检查str长度是否非0
    -z str   检查str长度是否为0
文件比较　

```

# 符合条件测试

```bash
[ condition1 ] && [ condition2 ]

[ condition1 ] || [ condition2 ]

```

# if-then高级特性

```bash

# (( expression )):　高级数学表达式

  支持
  val ++
  val --
  ++ val
  -- val
  !
  ~
  **
  <<
  >>
  &
  |
  &&
  ||

# [[ expression ]]: 高级字符串处理

# expression 采用test命令中标准字符串比较,特性--模式匹配

# case 命令
case variable in
pattern1 | pattern2) commands1;;
pattern2) commands2;;
*) default commands;;

esac

```

# 字符串比较

```bash
# > and < 比较,必须使用转义,否则视为重定向
# -n -z 判断字符串中是否含有数据

testuser=rich
myuser=rich

if [ $testuser = $myuser ]; then
    echo "testuser = myuser"
fi

if [ $testuser != $myuser ]
then
    echo "testuser != myuser"
else
    echo "testuser = myuser else"
fi


val1=baseball
val2=hockey

if [ $val1 \> $val2 ]; then
    echo "$val1 > $val2"
else
    echo "$val1 <= $val2"
fi


val1=Test
val2=test

if [ $val1 \> $val2 ]; then
    echo "$val1 > $val2"
else
    echo "$val1 <= $val2"
fi

echo "========================="
val1=testing
val2=''

if [ -n $val1 ]; then
    echo "The string '$val1' is not empty"
else
    echo "The string '$val1' is empty"
fi

if [ -z $val2 ]; then
    echo "The string '$val2' is empty"
else
    echo "The string '$val2' is not empty"
fi
testuser = myuser
testuser = myuser else
baseball <= hockey
Test <= test
=========================
The string 'testing' is not empty
The string '' is empty

```

# 文件比较

test命令的文件比较功能

-d file 检查file是否存在并且是一个目录

-f file 检查file是否存在并且是一个文件

-e file 检查file是否存在

-r file 检查file是否存在并且可读

-w file

-x file

-s file 检查file是否存在并且非空

-O file 检查file是否存在并且属于当前用户所有

-G file 检查file是否存在并且默认组与当前用户相同

file1 -nt file2 检查file1是否比file2新

file1 -ot file2 检查file1是否比file2旧

```bash
if [ -d $HOME ]; then
    echo "Your home directory exists"
else
    echo "There is a problem with your HOME directory"
fi
Your home directory exists

```

```bash
# 高级数学表达式处理
val1=10
if (( $val1 ** 2 > 90 ))
then
    (( val2 = $val1 ** 2 ))
    echo "the square of $val1 is $val2"
fi
the square of 10 is 100

# 高级字符串比较
val1=test
if [[ $val1 == t* ]]; then
    echo "hello $val1"
else
    echo "sorry, i do not known you"
fi
hello test


# case命令实例

# user=rich
user=testing

case $user in
rich | barbara)
    echo "Welcome, $user"
    echo "Please enjoy your visit";;
testing)
    echo "testing user";;
*)
    echo "sorry, you are not allown here";;
esac
testing user

```