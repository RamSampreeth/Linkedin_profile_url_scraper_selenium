from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import csv
import pandas
driver = webdriver.Firefox(executable_path="C:\Ram Sampreeth\Work\chromedriver_win32\geckodriver.exe")
driver.implicitly_wait(0.5)

dataset = pandas.read_csv('C:\Ram Sampreeth\Work\Scrapy\Linkedin_scraper\input.csv',encoding='latin-1')
search_queries = dataset.values
results = []

#linkedin signin

driver.get("https://www.linkedin.com/login?fromSignIn=true&session_redirect=https%3A%2F%2Fwww.linkedin.com%2Fjobs&trk=guest_homepage-jobseeker_nav-header-signin")
#linkedin_username
linkedin_username = 'ethan.williams@goodera.com'
username = driver.find_element_by_css_selector('#username')
username.send_keys(linkedin_username)
time.sleep(1)
#linkedin_password
linkedin_password = 'Goodera@123'
password = driver.find_element_by_css_selector("#password")
password.send_keys(linkedin_password)
time.sleep(0.5)
#signin
sign_in_button = driver.find_element_by_xpath('//*[@type="submit"]')
sign_in_button.click()
time.sleep(0.5)

#Profile_search
for query in search_queries:
    try:
        driver.get("https://www.linkedin.com")

        m = driver.find_element_by_css_selector("#global-nav-typeahead > input")
        m.send_keys(str(query[0]) + " " + str(query[1]))
        time.sleep(1)
        m.send_keys(Keys.ENTER)
        time.sleep(2)

        people_filter = driver.find_element_by_css_selector('li.search-reusables__primary-filter:nth-child(1)')
        people_filter.click()
        time.sleep(1)

        linkedin_url = driver.find_element_by_xpath('//div[@class="entity-result__item"][1]')
        linkedin_url.click()
        time.sleep(3)

        result = [str(query[0]),str(query[1]),str(driver.current_url)]
        results.append(result)
        time.sleep(2)
    except Exception:
        result = [str(query[0]),str(query[1]),"Not Found"]
        results.append(result)
        time.sleep(2)

  
driver.quit()

writer = csv.writer(open('results.csv','w',encoding='UTF8', newline=''))
writer.writerows(results)