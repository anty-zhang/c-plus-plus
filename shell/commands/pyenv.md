
[TOC]

# pyenv install
```bash
# install pyenv
git clone https://github.com/yyuu/pyenv.git ~/.pyenv
# install virtualenv
git clone https://github.com/yyuu/pyenv-virtualenv.git ~/.pyenv/plugins/pyenv-virtualenv
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bash_profile
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bash_profile
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"

# 查询所有可以安装的版本
pyenv install --list

# 安装指定版本
pyenv install -v 3.6.3

# 卸载特定的Python版本
pyenv uninstall

# 显示当前活动的Python版本
pyenv version

# Python的全局设置，整个系统生效
pyenv global 3.6.3


```


# pyenv virtualenv

```bash
pyenv virtualenv env # 从默认版本创建虚拟环境
pyenv virtualenv 3.6.4 env-3.6.4 # 创建3.6.4版本的虚拟环境
pyenv activate env-3.6.4 # 激活 env-3.6.4 这个虚拟环境
pyenv deactivate # 停用当前的虚拟环境

# 自动激活
# 使用pyenv local 虚拟环境名
# 会把`虚拟环境名`写入当前目录的.python-version文件中
# 关闭自动激活 -> pyenv deactivate
# 启动自动激活 -> pyenv activate env-3.6.4
pyenv local env-3.6.4

pyenv uninstall env-3.6.4 # 删除 env-3.6.4 这个虚拟环境

# 删除对应的环境
rm -rf ~/.pyenv/versions/env-3.6.4
```
