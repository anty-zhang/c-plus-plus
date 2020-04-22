

```bash
# -t 指定分隔符
# -k 按第几个字段进行排序
sort -t':' -k 3 -n -r /etc/passwd  | head

# a.text b.text 交集
# -d 的作用是输出次数大于1 的内容，即可得到交集
sort a.text b.text | uniq -d

# a.text b.text 并集
sort a.text b.text | uniq

# a.text - b.text 差集
# -u 输出文件中只出现一次的内容
sort a.text b.text b.text | uniq -u

```

