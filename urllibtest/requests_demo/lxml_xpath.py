from lxml import etree
import json

parser = etree.HTMLParser(encoding='utf-8')
html = etree.parse('test.html',parser=parser)

# # 显示所有tr
# trs = html.xpath('//tr')
# for tr in trs:
#     print(etree.tostring(tr,encoding='utf-8').decode('utf-8'))

# 获取第2个tr标签
# tr = html.xpath('//tr[2]')[0]
# print(etree.tostring(tr,encoding='utf-8').decode('utf-8'))

#所有class是even
# trs = html.xpath("//tr[@class='even']")
# for tr in trs:
#     print(etree.tostring(tr,encoding='utf-8').decode('utf-8'))

# 获取所有a标签的href属性值
# trs = html.xpath("//a/@href")
# for tr in trs:
#     print(tr)
#     print(type(tr))

# 获取所有职位的纯文本
trlist = []
trs = html.xpath("//tr[position()>1]")
for tr in trs:
    text = tr.xpath('.//a/text()')[0]
    href = tr.xpath('.//a/@href')[0]
    url = "https://hr.tencent.com/" + href
    category = tr.xpath('./td[2]/text()')[0]
    nums = tr.xpath('./td[3]/text()')[0]
    address = tr.xpath('./td[4]/text()')[0]
    tdict = {
        "职位":text,
        "详情":url,
        "类型":category,
        "需要人数":nums,
        "地点":address
    }
    trlist.append(tdict)
print(trlist)

with open('a.json','w',encoding='utf-8') as fp:
    json.dump(trlist,fp)

with open('a.json','r',encoding='utf-8') as fp:
    json.load(fp)