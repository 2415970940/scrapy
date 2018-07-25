import requests

url = "http://www.httpbin.org/ip"
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
    }
proxies = {"http":"27.206.176.120:9000"}

response = requests.get(url,headers=headers,proxies=proxies)
print(response.text)