[TOC]

# Mac python matplotlib 中文字体配置

- step 0: 查看已有字体

```bash
from matplotlib.font_manager import FontManager
fm = FontManager()
mat_fonts = set(f.name for f in fm.ttflist)

# 如果不安装新字体，可以尝试使用如下语句解决中文乱码
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']

```

- step 1: SimHei字体下载

```bash
// 下载地址: https://www.fontpalace.com/font-download/simhei/
下载位置: /anaconda3/lib/python3.6/site-packages/matplotlib/mpl-data/fonts/ttf
```

- step 2: 修改配置文件

```bash
在 /anaconda3/lib/python3.6/site-packages/matplotlib/mpl-data/matplotlibrc

增加如下三行配置
font.family          : sans-serif
font.sans-serif      : SimHei
axes.unicode_minus   : False
```

- step 3: 删除缓存

```bash
import matplotlib
print(matplotlib.matplotlib_fname())

rm -f ~/.matplotlib/fontList.json
```

- step 4: 重启Jupyter和python客户端重新加载

- step 5: 验证代码

```python
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
 
x = np.linspace(-10,10,200)
y = x
plt.plot(x,y)
plt.xlabel("横轴/单位",fontproperties="SimHei")
plt.ylabel("纵轴/单位",fontproperties="SimHei")
plt.title("标题",fontproperties="SimHei")
plt.show()
```


# reference

[Python 学习园](http://liao.cpython.org/pandas40/)
