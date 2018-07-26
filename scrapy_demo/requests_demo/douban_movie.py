import requests
from lxml import etree

url = "https://movie.douban.com/cinema/nowplaying/wuhan/"
headers = {
    "Use-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
}
# 获取网站的content
response = requests.get(url,headers=headers)
content = response.content

# parser = etree.HTMLParser(encoding='utf-8')
# html = etree.parse(content,parser=parser)
html = etree.HTML(content)

lis = html.xpath("//div[@id='nowplaying']//div/ul/li")
for li in lis:
    title = li.xpath("./@data-title")[0]
    score = li.xpath("./@data-score")[0]
    duration = li.xpath("./@data-duration")[0]
    href = li.xpath(".//a/@href")[0]
    release = li.xpath("./@data-release")[0]
    director = li.xpath("./@data-director")[0]
    actors = li.xpath("./@data-actors")[0]
    dict = {
        "电影":title,
        "导演":director,
        "主演":actors,
        "时长":duration,
        "评分":score,
        "详情链接":href,
        "上映时间":release
    }
    print(dict)
print("========================================================")

lis = html.xpath("//div[@id='upcoming']//div/ul/li")
for li in lis:
    title = li.xpath("./@data-title")[0]
    wish = li.xpath("./@data-wish")[0]
    duration = li.xpath("./@data-duration")[0]
    href = li.xpath(".//a/@href")[0]
    release = li.xpath(".//li[@class='release-date']/text()")[0].strip()[:6]
    director = li.xpath("./@data-director")[0]
    actors = li.xpath("./@data-actors")[0]
    dict = {
        "电影":title,
        "导演":director,
        "主演":actors,
        "时长":duration,
        "想看人数":wish,
        "详情链接":href,
        "上映时间":release
    }
    print(dict)