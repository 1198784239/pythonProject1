import re
str =''' <link  href="https://g.csdnimg.cn/static/logo/favicon32.ico"  rel="shortcut icon" type="image/x-icon" />
    <title>re模块最全常用正则表达式大全_re正则表达式-CSDN博客</title>
    <script>
      (function(){ 
        var el = document.createElement("script"); 
        el.src = "https://s3a.pstatp.com/toutiao/push.js?1abfa13dfe74d72d41d83c86d240de427e7cac50c51ead53b2e79d40c7952a23ed7716d05b4a0f683a653eab3e214672511de2457e74e99286eb2c33f4428830"; 
        el.id = "ttzz"; 
        var s = document.getElementsByTagName("script")[0]; 
        s.parentNode.insertBefore(el, s);+
      })(window)
    </script>
        <meta name="keywords" content="re正则表达式">
        <meta name="csdn-baidu-search"  content='{"autorun":true,"install":true,"keyword":"re正则表达式"}'>'''
m=re.compile('[一-龟]+|[A-Z]{4}[一-龟]+',re.S)
src=re.compile('.src.*"(.*?)"')
print(re.search(m,str).group())
S = re.findall(src,str)
print(S)
# a=re.sub(r'\W+','',str)
# print(a)
# print(m)