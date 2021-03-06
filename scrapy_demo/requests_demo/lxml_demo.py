# -*- coding: utf-8 -*-

from lxml import etree
text = """
<table class="tablelist" cellspacing="0" cellpadding="0">
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
</table>
"""

def parse_text():
    html = etree.HTML(text)
    # print(etree.tostring(html))
    print(etree.tostring(html,encoding='utf-8').decode('utf-8'))

def parse_file():
    # 创建HTML解析
    parser = etree.HTMLParser(encoding='utf-8')
    html = etree.parse("test.html",parser=parser)
    print(etree.tostring(html,encoding='utf-8').decode('utf-8'))
    print(type(html))

if __name__ == '__main__':
    parse_file()