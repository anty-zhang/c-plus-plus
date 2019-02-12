# while 循环

```bash
# 格式
while test cmd
    do
        cmds
    done
# test名令和if-then命令是一致的, 只有返回码为0时, while循环条件才会成立

val1=10
while [ $val1 -ge 0 ]
do
    echo "This is inside of the loop"
    val1=$[ $val1 - 1 ]
done

```