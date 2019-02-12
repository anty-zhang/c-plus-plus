# sed 使用

```bash
格式
sed options script file

    -e script: 在处理输入时,将script中指定的命令加到运行的命令中
    -f file: 在处理输入时, 将file中的命令添加到运行的命令中
    -n: 不要为每个命令生成输出, 等待print命令来输出
    -p: 会输出替换修改过的行
    -n -p: 二者配合只会输出替换修改过的行
```


## s命令实例

```bash
格式　
s/pattern/replacement/flags

    flags:
        1) 数字:　每行文本第几处模式匹配的地方将被替换
        2) g: 替换所有匹配
        3) p: 原来行的内容要打印出来
        4) w file: 替换的结果写入到文件中

$ echo "the quick brown fox jumps over the lazy dog" | sed -e 's/brown/gree/; s/dog/cat/'
$ the quick gree fox jumps over the lazy cat

# 使用地址: 行的数字范围
sed '2,3s/dog/cat/' ./data.d

# 使用地址: 文本过滤器
sed '/fox1/s/dog/cat/' ./data.d
sed '2s/fox/elephant/; 2s/dog/cat/' ./data.d

```

## d命令实例

```bash
sed '2d' ./data.d
echo "-------------------------------"
sed '2,3d' ./data.d
echo "-------------------------------"
sed '/fox1/d' ./data.d
echo "-------------------------------"
sed '/fox1 jumps/,/fox1 jumps/d' ./data.d

#  删除空行
sed '/^$/d' ./file

```

## i/a 插入命令
```bash
i: 会在指定行前面增加一个新行 a: 会在指定行的后面追加一个新行

格式
sed '[address]cmds new line'


echo "Test line2" | sed 'i\Test line1'
echo "-------------------------------"
echo "Test line2" | sed 'a\Test line1'
echo "-------------------------------"
echo "Test line2" | sed '3i\Test line1'

```

## c 修改行

```bash
cat ./data.d
The quick brown fox jumps over the lazy dog
The quick brown fox jumps over the lazy dog
The quick brown fox1 jumps over the lazy dog
The quick brown fox1 jumps over the lazy dog

sed '3c\this is a changed line of text.' ./data.d
echo "---------------------------------------"
sed '/fox1/c\This is a changed line of text' ./data.d
echo "---------------------------------------"
sed '2,3c\This is a changed line of text' ./data.d

# output
The quick brown fox jumps over the lazy dog
The quick brown fox jumps over the lazy dog
this is a changed line of text.
The quick brown fox1 jumps over the lazy dog
---------------------------------------
The quick brown fox jumps over the lazy dog
The quick brown fox jumps over the lazy dog
This is a changed line of text
This is a changed line of text
---------------------------------------
The quick brown fox jumps over the lazy dog
This is a changed line of text
The quick brown fox1 jumps over the lazy dog

```

## y 转换命令

```bash
格式
[address]/y/inchars/outchars/

$ echo "1 2 3 4 5" | sed 'y/123/899/'
$ 8 9 9 4 5

```


## 回顾打印
```bash
小写p打印文本行
    =号命令打印行号
    l命令列出行

# -n 可禁止其他行, 只打印包含匹文本配模式的行
$ echo "This is a test" | sed -n '/This/p'
$ This is a test

$ cat ./data.d
$ echo "-------------------"

# sed -n '/3/{p ; /dog/cat/p}' ./data.d


$ echo "-------------------"

$ sed '=' ./data.d
$ echo "-------------------"

$ sed -n 'l' ./data.d

# output
The quick brown fox jumps over the lazy dog
The quick brown fox jumps over the lazy dog
The quick brown fox1 jumps over the lazy dog
The quick brown fox1 jumps over the lazy dog
-------------------
-------------------
1
The quick brown fox jumps over the lazy dog
2
The quick brown fox jumps over the lazy dog
3
The quick brown fox1 jumps over the lazy dog
4
The quick brown fox1 jumps over the lazy dog
-------------------
The quick brown fox jumps over the lazy dog$
The quick brown fox jumps over the lazy dog$
The quick brown fox1 jumps over the lazy dog$
The quick brown fox1 jumps over the lazy dog$

```


## sed 高级
```bash
1. next 命令
    sed '/fox/{n ; d}' ./data.d     # 找到fox相匹配的行,并移动到下一行,并且删除下一行

    sed 'G' file      # 向文本文件中插入空白行
    sed '$!G' file    # 文本最后一行不插入空行
    sed '=' file | sed 'N; s/\n/ /'      # 给文件中的行编号

    sed -n '$p' file    # 打印末尾行


$ cat ./data1.d
This is the header line
This is the first data line
This is the second data line
This is the last line


# 找到first行, 连同其下一行一起进行处理
$ sed '/first/{ N; s/\n/ / }' ./data1.d
This is the header line
This is the first data line This is the second data line
This is the last line

# 排除命令
sed -n '/header/!p' ./data1.d
This is the first data line
This is the second data line
This is the last line

# 实例

# 将多行转成一行
cat test.txt
001
002
003
004
005
006
# 方法1：xargs 方法
xargs < test.txt

# 方法2: cat，echo
a=`cat test.txt` ; echo $a

# 方法3: tr将换行转为空格
tr -s "\n" " " < test.txt ;echo

# 方法4: sed把整个文件读入保持空间，处理最后一行的时候，替换所有换行为空格并打印
sed -n '1h;1!H;${g;s/\n/ /g;p;}'
1h 为将第一行copy 到 Hold space,1!H 为将非第一行的append到hold space, ${...} 为如果是最后一行这进行替换

# 方法5: paste命令格式化打印，-d分隔符，-s合并为一行
paste -d" " -s - < test.txt

# 方法6: pr格式化打印，-s指定分隔符，-50指定每行打印多少域，-t指定取消页眉页尾
pr -50t -s" " test.txt

# 方法7: awk，读入一行打印一行，但是不是打印换行符，最后一行多打印一个换行符
awk '{printf("%s ", $0);} END {print }' test.txt

```
