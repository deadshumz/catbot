import urllib3
from bs4 import BeautifulSoup

url = 'https://www.google.com/search?q=apple&prmd=nvmi&sxsrf=APq-WBuFy280z7KyG55SrB99VmukhtXjxw:1648237723601&source=lnms&tbm=isch&sa=X&ved=2ahUKEwib2pSAhOL2AhWjlIsKHSHlABsQ_AUoBHoECAIQBA&biw=2652&bih=1614&dpr=2'

http = urllib3.PoolManager()

page = http.request('GET', url)

bs = BeautifulSoup

soup = bs(page.data, 'html.parser')

images = soup.find_all('a')

for i in images:
    print(i)