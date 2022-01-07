from os import error
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import csv
import pandas


driver = webdriver.Chrome(executable_path="C:\Ram Sampreeth\Work\chromedriver_win32\chromedriver.exe")
driver.implicitly_wait(0.5)

dataset = pandas.read_csv('C:\Ram Sampreeth\Work\Web-scraping requests\Linkedin_scraper\input.csv',encoding='latin-1')
search_queries = dataset.values

writer = csv.writer(open('results.csv','w',encoding='UTF8', newline=''))
for query in search_queries:
    try:
        driver.get("https://www.google.com/")
        time.sleep(3)
        m = driver.find_element_by_name("q")
        m.send_keys(str(query[0])+ ", social enterprise Australia")
        time.sleep(2)

        m.send_keys(Keys.ENTER)
        time.sleep(3)
        url = driver.find_element_by_css_selector("div.yuRUbf > a").get_attribute('href')
        url = url.strip()
        result = [str(query[0]), str(url)]
        time.sleep(3)
        writer.writerow(result)

    except Exception:
        result = [str(query[0]),str(query[1]),"Not Found"]
        print(error)
        time.sleep(3)
        writer.writerow(result)
    
driver.quit()