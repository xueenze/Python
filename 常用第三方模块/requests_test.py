import requests

r = requests.get('https://www.douban.com/') # 豆瓣首页

print(r.status_code)