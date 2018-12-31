from selenium import  webdriver
import time
# 创建一个浏览器对象 executable_path:驱动路径
bro = webdriver.Chrome(executable_path='./chromedriver')

# get方法可以指定一个url，让浏览器进行请求
bro.get('https://www.baidu.com')

# 让浏览器进行指定词条搜索
'''
#使用下面的方法，查找指定的元素进行操作即可
    find_element_by_id            根据id找节点
    find_elements_by_name         根据name找
    find_elements_by_xpath        根据xpath查找
    find_elements_by_tag_name     根据标签名找
    find_elements_by_class_name   根据class名字查找
'''
text = bro.find_element_by_id('kw')
text.send_keys('人民币') # send_keys表示向文本框中录入指定内容

time.sleep(3)
button = bro.find_element_by_id('su')
button.click()# click表示的是点击操作
time.sleep(5)
bro.quit()
