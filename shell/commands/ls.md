
# ls 基本使用

```bash
# # 列出当前目录的文件、文件夹完整路径
# -1 列显示
ls -1 |awk '{print i$0}' i=`pwd`'/'

# 列出当前目录及子目录的文件、文件夹完整路径
ls -R | awk '{print i$0}' i=`pwd`'/'

# 列出当前目录及子目录下的文件夹完整路径
# find ./ -name "*" -exec ls {} \;
ls -FR | grep /$ | sed "s:^:`pwd`/:"

# 递归列出当前目录及子目录名称，包括相关属性
ls -lR | grep "^d"

# 只列出当前目录下的子目录
ls -d */

```