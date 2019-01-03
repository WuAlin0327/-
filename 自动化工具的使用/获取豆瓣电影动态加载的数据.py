from selenium import webdriver

import time
from lxml import etree
bro = webdriver.Chrome('./chromedriver')
url = 'https://movie.douban.com/typerank?type_name=%E5%96%9C%E5%89%A7&type=24&interval_id=100:90&action='


bro.get(url)

# 等待五秒页面加载完毕
time.sleep(5)
# 重复20次使用页面滚轮
for i in range(20):
    time.sleep(2)
    bro.execute_script('window.scrollTo(0,document.body.scrollHeight)')

# 获取页面源代码，可以使用三种解析方式进行解析，这里使用xpath解析数据
text = bro.page_source
tree = etree.HTML(text)
div_list = tree.xpath('//div[@class="movie-info"]')
f = open('豆瓣喜剧电影排行榜.txt','w',encoding='utf-8')
count = 0
for div in div_list:
    # 获取电影具体数据，并进行持久化存储
    try:
        name = div.xpath('./div[@class="movie-name"]/span/a/text()')[0]
        link = div.xpath('./div[@class="movie-name"]/span/a/@href')[0]
        man = div.xpath('./div[@class="movie-crew"]/text()')[0]
        country = div.xpath('./div[@class="movie-misc"]/text()')[0]
        num = div.xpath('./div[@class="movie-rating"]/span[2]/text()')[0]
    except IndexError:
        continue

    f.write('电影名：'+name+'\n链接'+link+'\n'+'导演：'+man+'\n国家：'+country+'\n评分：'+num+'\n-----------------------------\n\n\n')
    print('写入成功:',name)
    count += 1
print('爬取完毕,共抓取%s跳数据'%count)
f.close()
time.sleep(5)
bro.quit()