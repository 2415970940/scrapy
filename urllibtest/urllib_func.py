from urllib import request

# resp = request.urlopen("http://www.baidu.com")
# # print(resp.read())
# print(resp.readlines())

# 页面下载到本地urlretrieve
# request.urlretrieve("http://www.baidu.com","baidu.html")

# urlencode编码
from urllib import parse
# params = {'name':'张三','age':14,'memo':'student'}
# result = parse.urlencode(params)
# print(result)

# # urlopen  urlencode
# url = "http://www.baidu.com/s"
# param = {'wd':'刘德华'}
# param_encode = parse.urlencode(param)
# urls = url + '?'+ param_encode
# result = request.urlopen(urls)
# print(result.read())

# 解码parse_qs
# params = {'name':'张三','age':14,'memo':'student'}
# cd = parse.urlencode(params)
# print(type(cd))
# result = parse.parse_qs(cd)
# print(result)

# urlparse  urlsplit(无params字段)
result = parse.urlparse('https://www.baidu.com/s?wd=parse&rsv_spt=1&rsv_iqid=0xd87e20f1000080fc&issp=1&f=8&rsv_bp=1&rsv_idx=2&ie=utf-8&rqlang=cn&tn=baiduhome_pg&rsv_enter=1&oq=%25E5%258F%2582%25E6%2595%25B0%2520%25E8%258B%25B1%25E6%2596%2587&rsv_t=b68cofwr9QOT6kspYlIy3ILiuvEUw0cQMC11f1hAiv4F%2Bfj%2Bf55pirn%2B8YPjWNhzeRn0&rsv_pq=f036175300015a05&rsv_sug3=10&rsv_sug1=6&rsv_sug7=100&bs=%E5%8F%82%E6%95%B0%20%E8%8B%B1%E6%96%87')
print(result)