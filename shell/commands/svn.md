# 基本使用
```bash
svn revert -R project
svn up project

```

# 忽略某个目录

## 一、忽略单个目录

```bash
1、忽略文件夹

假如目录oa.youxi.com是从svn checkout出来的，在服务器本地目录添加了material，但是不希望把material加入版本控制，因此我们需要忽略掉这个目录
首先使用svn status命令查看当前状态
[root@localhost oa.youxi.com]# svn status
? htdocs/admin/adv/material

添加需要忽略的目录，貌似必须得进入该目录之下
[root@localhost oa.youxi.com]# cd htdocs/admin/adv/
[root@localhost adv]# svn propset svn:ignore 'material' ./
property 'svn:ignore' set on '.'

[root@localhost adv]# svn ci -m 'ignore a directory called "material".'
Sending adv
Committed revision 2.

再次查看状态
[root@localhost adv]# svn status
[root@localhost adv]#

此后无论material目录如何修改，都不会提交到仓库去

2、提交文件夹，忽略文件夹内内容

[root@localhost adv]# svn propset svn:ignore '*' material
[root@localhost adv]# svn ci -m 'adding "material" and ignore its contents.'

3、若已经创建了文件夹，并加入了版本控制，现在想忽略这个文件夹，但要保持文件夹的内容：

[root@localhost adv]# svn export material material-tmp
[root@localhost adv]# svn rm material
[root@localhost adv]# svn ci -m 'Removing inadvertently added directory "material".'
[root@localhost adv]# mv material-tmp material
[root@localhost adv]# svn propset svn:ignore 'material' ./
[root@localhost adv]# svn ci -m 'Ignoring a directory called "material".'

对于没有加入版本控制的，可以直接设定成ignore，但不能对加入版本控制的文件和目录这么做。解决办法是，先删除再ignore， 上面的命令其实也是这个方式，只不过有导出再mv的过程。

```

## 二、忽略多个目录

```bash
如果有多个目录需要删除，逐个目录按照上面步骤操作，那么操作完成后，前面操作的目录执行svn st又会显示成 ? 状态，而最后执行的那个目录才不会显示出来，所以说这样前面的目录都白弄了
如果有多个目录需要同时忽略，需要这样弄

[root@localhost adv]# svn st
? ad
? material
? logs
? images
[root@localhost adv]# svn delete url -m="delete ad"　　　　#删除版本库相应目录
[root@localhost adv]# mv ad material logs images /tmp 　　#先备份
[root@localhost adv]# svn propset svn:ignore ".svnignore
> ad
> material
> logs
> images
> " ./
property 'svn:ignore' set on '.'
[root@localhost adv]# svn propget svn:ignore .
.svnignore
ad
material
images
logs

[root@localhost adv]# svn ci -m "ignore some directory"
Sending adv

Committed revision 6.
[root@localhost adv]# svn st
[root@localhost adv]#mv /tmp/{ad,images,logs,material} ./　　#恢复备份

到这里就大功告成了，无论怎么修改上面的几个目录里面文件svn st都不会列出来，无论怎么svn up当前目录，上面几个目录都不会受到影响。

```