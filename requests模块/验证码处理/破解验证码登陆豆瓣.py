
import discern_code
# 获取验证码图片保存到本地
import requests
from lxml import etree
import re

url = 'https://www.douban.com/accounts/login?source=movie'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}
page_text = requests.get(url=url,headers=headers).text

# 使用xpath解析出验证码图片的url
tree = etree.HTML(page_text)
codeImg_url = tree.xpath('//*[@id="captcha_image"]/@src')[0]

# 获取到图片的二进制数据保存到本地
code_img = requests.get(url=codeImg_url,headers=headers)
with open('code.png','wb') as f:
    f.write(code_img.content)
code = discern_code.getCode('code.png')

# 获取captcha-id的值
'<img id="captcha_image" src="https://www.douban.com/misc/captcha?id=doxNHcIKqXbXczQU9osn65kP:en&amp;size=s" alt="captcha" class="captcha_image">'
c_id = re.findall('<img id="captcha_image" .*?id=(.*?)&amp.*?',page_text)[0]
login_url = 'https://accounts.douban.com/login'
data = {
    'source': 'movie',
    'redir': 'https://movie.douban.com/',
    'form_email': '1032298871@qq.com',
    'form_password': '09212427zlh',
    'captcha-solution': code,
    'captcha-id': c_id,
    'login': '登录',
}
response = requests.post(url=login_url,data=data,headers=headers)
with open('豆瓣.html','w',encoding='utf-8') as f:
    f.write(response.text)
