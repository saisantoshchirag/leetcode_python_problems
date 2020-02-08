from bs4 import BeautifulSoup as soup
import requests
import  re
from selenium import webdriver



driver = webdriver.PhantomJS(executable_path=r"C:\Software_shortcuts\phantomjs-2.1.1-windows\phantomjs-2.1.1-windows\bin\phantomjs.exe")
url1 = 'http://netdna.bootstrapcdn.com/bootstrap/3.0.3/css/bootstrap.min.css'
driver.get(url1)

soup1 = soup(driver.page_source,'lxml')
print(soup1)
txt = soup1.find_all('form-control')
print(txt)
print(txt.text)
