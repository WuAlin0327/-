import requests
from bs4 import BeautifulSoup

url = 'http://www.shicimingju.com/book/sanguoyanyi.html'
headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
    }
page_text = requests.get(url=url,headers=headers).text

def get_content(url,fileobj):
    '''
    爬取页面内容
    :param url:
    :param fileobj:
    :return:
    '''
    content_page = requests.get(url=url, headers=headers).text
    content_soup = BeautifulSoup(content_page, 'lxml')
    p_list = content_soup.select('.chapter_content > p')
    for p in p_list:
        fileobj.write('\n' + p.text + '\n\n')

soup = BeautifulSoup(page_text,'lxml')
a_list = soup.select('.book-mulu > ul > li > a')
f = open('三国演义.txt','w',encoding='utf-8')
for a in a_list:
    f.write('\n'+a.text)
    content_url = 'http://www.shicimingju.com'+a['href']
    get_content(content_url,f)
    print('爬取成功',a.text)