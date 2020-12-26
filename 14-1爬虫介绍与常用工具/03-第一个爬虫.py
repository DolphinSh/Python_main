from urllib.request import urlopen

# 1 要访问的地址
url = "http://www.baidu.com"

# 2 发送请求
response = urlopen(url)

# 3 读取内容
info = response.read()

# 4 打印内容
print(info)