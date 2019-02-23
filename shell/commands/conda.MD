# 基本使用

```bash
# conda 配置源

cat ~/.condarc
channels:
    - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
    - defaults
show_channel_urls: true


# 创建环境
conda create -n tf python=3.6
conda activate tf
conda deactivate

```