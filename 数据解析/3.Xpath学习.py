from lxml import etree
html = """
<html >
<head>
<meta charset="UTF-8">
<title>this is a title</title>
</head>
<body>
<p class="news"><a >123456</a>
<a >78910</a></p>
<p class="contents" id="i1">456</p>
<a href="http://www.baidu.com" rel="external nofollow" rel="external nofollow" rel="external nofollow" rel="external nofollow" rel="external nofollow" >advertisements</a>
</body>
</html>
"""
etree = etree.HTML(html)
#拿到数据
print(etree)
a = etree.xpath('//title/text()')
a = etree.xpath('//p/text()')
a = etree.xpath('//p/a/text()')
print(a)
s = etree.xpath('//p[@class="news"]/text()')
print(s)
