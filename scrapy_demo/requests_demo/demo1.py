import requests

url = "https://www.baidu.com"
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
    }
kw = {"wd":"python"}

response = requests.get(url,headers=headers,params=kw)
# print(response.content.decode('utf-8'))
# print(response.text)
print(response.url)
print(response.encoding)
print(response.status_code)