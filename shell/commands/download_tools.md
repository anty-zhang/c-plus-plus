# wget
# curl

```bash
参数信息
-i 显示头部信息
-I 只显示头部信息，不显示正文
-X 指定请求方法，比如GET、POST等
-d 发送数据
--form模拟表单，利用这个参数可以上传文件、模拟点击按钮等
-A 指定用户代理，比如Mozilla/4.0,有些坑爹网址必须使用IE访问怎么办
-b 设置cookie
-c 指定cookie文件
-e 指定referer，有些网址必须从某个页面跳转过去
--header 设置请求的头部信息
--user 有些页面需要HTTP认证， 传递name:password认证
```

# axel

```bash
axel是一个多线程下载工具（A light download accelerator for Linux），通过建立多连接，能够大幅度提高下载速度，所以我经常使用这个命令开挂下载大文件，比wget快多了，并且默认就支持断点下载:

# 开启20个线程下载文件
axel -n 20 URL

```