import requests
from lxml import etree

url = 'https://ishuo.cn/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}
page_text = requests.get(url=url,headers=headers).text

tree = etree.HTML(page_text)
li_list = tree.xpath('//div[@id="list"]/ul/li')
f = open('段子.text','w',encoding='utf-8')
for li in li_list:
    content = li.xpath('./div[@class="content"]/text()')[0]
    title = li.xpath('./div[@class="info"]/a/text()')[0]
    f.write("#####################\n"+title+":\n"+content+"\n\n")
print('写入数据成功')