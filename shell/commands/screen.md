# screen 基础

## 使用问题

```bash
Cannot open your terminal '/dev/pts/0' - please check.
解决方法:
# 运行脚本
script -q -c "su $USER -l -c 'screen -m -d -S $NAME $DAEMON start'" /dev/null

# 单独执行
script /dev/null

```


##  自定义.screenrc配置文件

```bash
defscrollback 100000
termcapinfo xterm* ti@:te@

```