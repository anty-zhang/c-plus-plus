# for 循环

```bash
# 格式
for var in list
    do
        cmds
    done

# list 以空格分割

# 分隔符
IFS环境变量定义了bash shell中的分隔符,默认值是: 空格, 制表符, 换行符

指定换行符IFS=$'\n'(忽略空格和制表符), IFS=:, IFS=$'\n:;'"
```

# example

```bash
# 在程序中某一部分需要修改分割符

IFS.OLD=$IFS
IFS=$'\n'
# TODO new use the new IFS value in the code

IFS=$IFS.OLD
bash: line 4: IFS.OLD=: command not found
In [8]:
%%bash

# 指定分隔符实例
for v in `cat /etc/passwd| head -1`
do
    echo "value: $v"
done

echo "-------------------------------------------------"

IFS=:
for v in `cat /etc/passwd| head -1`
do
    echo "value: $v"
done
value: root:x:0:0:root:/root:/bin/bash
-------------------------------------------------
value: root
value: x
value: 0
value: 0
value: root
value: /root
value: /bin/bash
In [9]:
%%bash
# C语言风格for循环

for ((i=1, j=10; i < j; i++, j--)); do
    echo "i=$i, j=$j"
done
i=1, j=10
i=2, j=9
i=3, j=8
i=4, j=7
i=5, j=6
In [4]:
%%bash

# 循环实例

# c语言风格
echo "===========c语言风格=============="
for ((i=1; i<=5; i++))
do
    echo $i
done




# in 和 {} 使用
echo "===========in 和 {} 使用=============="
for i in {1..5}
do
    echo $i
done

# seq 使用
echo "===========c语言风格=============="
===========c语言风格==============
1
2
3
4
5
1
2
3
4
5

```