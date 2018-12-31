from selenium import webdriver

bro = webdriver.PhantomJS(executable_path='/Users/wualin/Desktop/第7模块课件/01-爬虫课件/5. 动态数据加载爬取/phantomjs-2.1.1-macosx/bin/phantomjs')

# 浏览器
bro.get('https://www.baidu.com')

# 截屏
bro.save_screenshot('./1.png')

bro.quit()