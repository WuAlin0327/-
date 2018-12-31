from lxml import etree
import requests

url = 'https://www.qiushibaike.com/pic/'
page_text = requests.get(url=url).text

tree = etree.HTML(page_text)
url_list = tree.xpath('//div[@class="article block untagged mb15"]/div[2]/a/img/@src')

print(url_list)
