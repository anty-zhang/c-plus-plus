
```bash
安装
sudo esay_install ansible
# 或者
sudo pip install ansible
yum install ansible
配置
ansible 执行顺序
ansible执行的时候会按照以下顺序查找配置项:
* ANSIBLE_CONFIG (环境变量)
* ansible.cfg (当前目录下)
* .ansible.cfg (用户家目录下)
* /etc/ansible/ansible.cfg
hosts配置
cat ~/.hosts
# hosts
[local]
127.0.0.1

ansible -i ~/hosts all -a 'who'
这是一条ad-hoc命令——临时执行命令，ad-hoc是ansible里的一个概念, 在上面命令中就是 -a
ad hoc——临时的，在ansible中是指需要快速执行，并且不需要保存的命令。说白了就是执行简单的命令——一条命令
模块
在ansible中还有一个Module（模块）的概念，这个模块可以理解为一个库，所有的命令都需要通过模块来执行，比如上面的那个命令: ansible-i ~/hosts all -a 'who' ，其实是调用了默认的command模块: ansible -i ~/hosts all -mcommand -a 'who' ,除了command模块还有其他很多模块，比如你就想ping下这个服务器是不是还存在可以通过ping模块: ansible -i ~/hosts all -m ping 。

```