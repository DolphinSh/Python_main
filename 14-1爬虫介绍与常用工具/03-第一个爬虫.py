from urllib.request import urlopen

# 1 要访问的地址
url = "http://www.baidu.com"

# 2 发送请求
response = urlopen(url)

# 3 读取内容
info = response.read()

# 4 打印内容
#print(info)
print(info.decode())

# 返回HTTP的响应码
print(response.getcode())

# 返回实际访问的url
print(response.geturl())

# 返回HTTP响应头
print("返回HTTP响应头")
print(response.info())