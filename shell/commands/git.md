

[TOC]

# git 基本使用
## git config使用

### git config 文件存放的位置
``` bash

git config -e   # .git/config
git config -e --global   # ~/.gitconfig
git config -e --system   # /etc/gitconfig

# 优先级
git config > git config --global > git config --system

```

### 基本配置和使用

```bash
# 查看配置
git config --list
git config --global --list
git config --system --list

# 基本配置
core.symlinks=false
core.autocrlf=true
core.fscache=true
color.diff=auto
color.status=auto
color.branch=auto
color.interactive=true
help.format=html

# 用户名和密码
# 如果是不同的项目使用不同的名称和email，则不需要加global
git config --global user.name "xxx"
git config --global user.email "xxx@163.com"
# 删除global 中的user.name
git config --global --unset user.name

# 配置比较工具
git config --global core.editor vim

# 配置别名
git config --global alias.lg "log --color --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit"

git config --global alias.co checkout
git config --global alias.st status
git config --global alias.df diff
git config --global alias.ss status -s
git config --global alias.cm commit -m
git config --global alias.br branch
git config --global alias.bm branch -m
git config --global alias.bd branch -D
git config --global alias.cb checkout -b
git config --global alias.ll "log --graph --pretty=format:'%Cred%h%Creset %C(bold blue)%s%Creset %Cgreen(%cr) <%an>%Creset' --abbrev-commit --date=relative"
git config --global alias.lg "log --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %C(bold blue)%s%Creset %Cgreen(%cr) <%an>%Creset' --abbrev-commit --date=relative"
git config --global alias.alg "log --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %C(bold blue)%s%Creset %Cgreen(%cr) <%an>%Creset' --abbrev-commit --date=relative --all"
git config --global alias.ls log --stat
git config --global alias.plo pull origin
git config --global alias.pho push origin


# error: RPC failed; curl 18 transfer closed with outstanding read data remaining
# fatal: The remote end hung up unexpectedly
# fatal: early EOF
# fatal: index-pack failed
git config --global http.postBuffer 524288000
git clone http://xxx.git --depth 1

# 提交本地代码到新分支
# branchA分支拉了一份代码，做了一些修改，但是不想提交到branchA分支，想新建一个分支branchB保存代码
git add .
git commit -m ''
git push origin branchA:branchB
git checkout -b branchB origin/branchB

# help
git help <verb>
git <verb> help
man git

# git ssh
ssh-keygen -t rsa -C "your_email@youremail.com"
ssh -T git@github.com

# 
git init
git remote add https://xxx.git
git add .
git commit -m ''
git push origin master

# .gitignore 不起作用
git rm -r --cached .


```

## tag basic

https://dev.to/emmawedekind/using-git-tags-to-version-coding-tutorials-39cc

https://en.wikibooks.org/wiki/Git/Advanced
