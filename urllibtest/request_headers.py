from urllib import request,parse

# headers使用
# url = 'https://www.lagou.com/jobs/list_django?city=%E8%A5%BF%E5%AE%89&cl=false&fromSearch=true&labelWords=&suginput='
# headers = {
#     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
#             }
# rq = request.Request(url,headers=headers)
# resp = request.urlopen(rq)
# print(resp.read().decode())

#发现字段通过ajax取得的
url = 'https://www.lagou.com/jobs/positionAjax.json?city=%E8%A5%BF%E5%AE%89&needAddtionalResult=false'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
     'Referer':'https://www.lagou.com/jobs/list_django?city=%E8%A5%BF%E5%AE%89&cl=false&fromSearch=true&labelWords=&suginput='
            }
data = {'first':'true',
        'pn':1,
        'kd':'django'
        }

rq = request.Request(url,headers=headers,data=parse.urlencode(data).encode('utf-8'),method='POST')
resp = request.urlopen(rq)
print(resp.read().decode('utf-8'))