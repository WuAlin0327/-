import requests
import re
import os
from concurrent.futures import ThreadPoolExecutor
if not os.path.exists('image'):
    os.mkdir('image')
def get_page(number):
    '''
    页数
    :param number:
    :return:
    '''
    if number == 1:
        url = 'https://www.qiushibaike.com/pic/'
    else:
        url='https://www.qiushibaike.com/pic/'+'page/'+str(number)
    print(url)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
    }
    page_text = requests.get(url=url,headers=headers).text

    img_list = re.findall('<div class="thumb">.*?<img src="(.*?)".*?>.*?</div>',page_text,re.S)
    for _url in img_list:
        img_url = 'https:'+_url
        response = requests.get(url=img_url,headers=headers)
        filename = img_url.split('/')[-1]
        file_path = 'image/%s'%filename
        with open(file_path,'wb') as f:
            f.write(response.content)
            print('爬取第%s页数据中：%s'%(number,filename))

if __name__ == '__main__':
    pool = ThreadPoolExecutor(5)
    for i in range(1,36):
        pool.submit(get_page,i)

    pool.shutdown()
    print('爬取完毕')