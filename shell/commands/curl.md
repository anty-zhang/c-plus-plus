
[TOC]

# Get 请求

## Get请求转中文

```bash
# 直接请求会出现异常
curl -i  http://localhost:8444/api/test?msg=ddd我
# get 请求参数msg带中文，需要将其转码后才可以正常请求
curl -G --data-urlencode "msg=ddd我"  http://localhost:8444/api/test
```
