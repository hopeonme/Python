import requests
import re
import time
local = time.strftime("%Y.%m.%d")       # 当前日期
url = 'http://cn.bing.com/'             # 指定URL
con = requests.get(url)     # Get URL
content = con.text
# print(content)
reg = r"(az/hprichbg/rb/.*?.jpg)"
a = re.findall(reg, content, re.S)[0]
print(a)
picUrl = url + a
read = requests.get(picUrl)
f = open('%s.jpg' % local, 'wb')
f.write(read.content)
f.close()
