from urllib import request,parse

# url = 'https://ip.cn/'
url='http://www.httpbin.org/ip'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}

url = request.Request(url,headers=headers)
# resp = request.urlopen(url)
# print(resp.read().decode('utf-8'))
# # value="221.234.156.168"

# handler = request.ProxyHandler({'HTTPS':'221.228.17.172:8181'})
handler = request.ProxyHandler({"HTTP":"121.232.148.253:9000"})
opener = request.build_opener(handler)
resp = opener.open(url)
print(resp.read().decode('utf-8'))