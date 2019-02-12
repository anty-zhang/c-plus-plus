
# bash 信号处理

## linux信号
```bash
1  SIGHUP   挂起进程
   2  SIGINT   终止进程
   3  SIGQUIT  停止进程
   9  SIGKILL  无条件终止进程
   15 SIGTERM  可能的话终止进程
   17 SIGSTOP  无条件停止进程,但不终止
   18 SIGTSTP  停止或者暂停,但不终止
   19 SIGCONT  继续运行停止的进程

```

## 格式
```bash
trap cmds signals

例如:
    trap "echo ByeBye" EXIT     # 捕捉推出信号
    trap - EXIT                 # 移除信号捕捉


#!/bin/bash

# testing trapping signal

trap "echo 'Sorry! I have trapped Ctrl-C'" SIGINT SIGTERM
echo "This is test program"

count=1
while [ $count -lt 10 ]
do
    echo "Loop #$count"
    sleep 3
    count=$[ $count + 1 ]
done

echo "This is the end of test program"
This is test program
Loop #1
Loop #2
Loop #3
Loop #4
Loop #5
Loop #6
Loop #7
Loop #8
Loop #9
This is the end of test program

```

