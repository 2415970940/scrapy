from bs4 import BeautifulSoup

text = """<table class="tablelist" cellspacing="0" cellpadding="0">
		    	<tbody><tr class="h">
		    		<td class="l" width="374">职位名称</td>
		    		<td>职位类别</td>
		    		<td>人数</td>
		    		<td>地点</td>
		    		<td>发布时间</td>
		    	</tr>
		    			    	<tr class="even">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=42806&amp;keywords=&amp;tid=87&amp;lid=2175">25924-技术研发组长（上海）</a></td>
					<td>技术类</td>
					<td>1</td>
					<td>上海</td>
					<td>2018-07-25</td>
		    	</tr>
		    			    	<tr class="odd">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=42809&amp;keywords=&amp;tid=87&amp;lid=2175">25927-WeTest高级IOS客户端开发工程师（上海）</a></td>
					<td>技术类</td>
					<td>1</td>
					<td>上海</td>
					<td>2018-07-25</td>
		    	</tr>
		    			    	<tr class="even">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=42794&amp;keywords=&amp;tid=87&amp;lid=2175">25926-NLP工程师（上海）</a><span class="hot">&nbsp;</span></td>
					<td>技术类</td>
					<td>1</td>
					<td>上海</td>
					<td>2018-07-25</td>
		    	</tr>
		    			    	<tr class="odd">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=42622&amp;keywords=&amp;tid=87&amp;lid=2175">24987-手游客户端开发工程师</a></td>
					<td>技术类</td>
					<td>2</td>
					<td>上海</td>
					<td>2018-07-25</td>
		    	</tr>
		    			    	<tr class="even">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=42426&amp;keywords=&amp;tid=87&amp;lid=2175">25927-移动游戏高级测试开发工程师（上海）</a></td>
					<td>技术类</td>
					<td>1</td>
					<td>上海</td>
					<td>2018-07-25</td>
		    	</tr>
		    			    	<tr class="odd">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=42358&amp;keywords=&amp;tid=87&amp;lid=2175">OMG064-系统测试工程师（上海）</a></td>
					<td>技术类</td>
					<td>1</td>
					<td>上海</td>
					<td>2018-07-25</td>
		    	</tr>
		    			    	<tr class="even">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=42229&amp;keywords=&amp;tid=87&amp;lid=2175">OMG064-广告数据平台开发工程师（上海）</a><span class="hot">&nbsp;</span></td>
					<td>技术类</td>
					<td>1</td>
					<td>上海</td>
					<td>2018-07-25</td>
		    	</tr>
		    			    	<tr class="odd">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=42113&amp;keywords=&amp;tid=87&amp;lid=2175">SNG07-看点系统测试工程师（上海）</a></td>
					<td>技术类</td>
					<td>1</td>
					<td>上海</td>
					<td>2018-07-25</td>
		    	</tr>
		    			    	<tr class="even">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=41967&amp;keywords=&amp;tid=87&amp;lid=2175">25928-Web前端开发工程师（上海）</a></td>
					<td>技术类</td>
					<td>1</td>
					<td>上海</td>
					<td>2018-07-25</td>
		    	</tr>
		    			    	<tr class="odd">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=41832&amp;keywords=&amp;tid=87&amp;lid=2175">SNG04-内容平台视觉算法研究员（上海）</a><span class="hot">&nbsp;</span></td>
					<td>技术类</td>
					<td>3</td>
					<td>上海</td>
					<td>2018-07-25</td>
		    	</tr>

		    </tbody>
</table>"""

# soup = BeautifulSoup(text,'lxml')
soup = BeautifulSoup(open('test.html',encoding='utf-8'),'lxml')
# print(soup.prettify())

#获取所有tr标签
# trs = soup.find_all('tr')
# for tr in trs:
#     print(tr)
#     print('========================')

# 获取第2个tr标签
# BeautifulSoup不像xpath，直接tr[2],而需要通过列表方式
# trs = soup.find_all('tr',limit=2)
# print(trs[1])

#所有class是even
# # trs = soup.find_all('tr',class_='even')
# trs = soup.find_all('tr',attrs={'class':'even'})
# for tr in trs:
#     print(tr)

# id=test class=test的a标签
# aitem = soup.find_all('a',attrs={'id':'test','class':'test'})
# aitem = soup.find_all('a',id='test',class_='test')
# for item in aitem:
#     print(item)

# 获取所有a标签的href属性值
# aitem = soup.find_all('a')
# for a in aitem:
#     print(a)
#     #两种方式获得
#     # href = a['href']
#     href = a.attrs['href']
#     print(href)

# 获取所有职位的纯文本
trs = soup.find_all('tr')[1:]
for tr in trs:
    # title = tr.find_all('a')[0]
    # tds = tr.find_all('td')
    # category = tds[1]
    # print(title.string)
    # print(category.string)
    # 第2种方式
    infos = list(tr.stripped_strings)
    print(infos)