
import requests
from bs4 import BeautifulSoup
r=requests.get("http://mianzhuan.wddsnxn.org/")
print(r.text)