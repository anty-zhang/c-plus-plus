# urllib,urllib2,httplib

```bash
# httplib实现了http和https协议
# 在python中urllib,urllib2对httplib进行了更上层的封装
# python中发送post请求到get时，会报405 httpErrorCode

```

# example

## urllib,urlllib2 get reqeust

```python
import urllib
import urllib2

url = "http://host:port?name=zhangsan&age=10"
req = urllib2.Request(url)

data = req.urllib2.urlopen(req)
res = data.read()

print res


# httplib get request

import httplib

url = "http://host:port?name=zhangsan&age=10"
conn = httplib.HTTPConnection(host)
conn.request(method="GET", url=url)
response = conn.getresponse()
res = response.read()

```

## urllib,urlllib2 get reqeust

```python
import urllib
import urllib2

url = "http://host:port"
body_data = {
    "name": "zhangsan",
    "age": 20
}
body_data_urlencode = urllib.urlencode(body_data)

req = urllib2.Request(url, data=body_data_urlencode)

data = req.urllib2.urlopen(req)
res = data.read()

print res


# httplib get request

import httplib

url = "http://host:port"
body_data = {
    "name": "zhangsan",
    "age": 29
}
headerdata = {"Host":"192.168.81.16"}

body_data_urlencode = urllib.urlencode(body_data)
conn = httplib.HTTPConnection('host')

conn.request(method="POST", url=url, body=body_data_urlencode, headers=headerdata)
response = conn.getresponse()
res = response.read()
```