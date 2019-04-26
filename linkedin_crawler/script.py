from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
import parameters

driver = webdriver.Chrome()
driver.get('https://www.linkedin.com')
sleep(.5)
driver.refresh()

user = driver.find_element_by_id('login-email')
user.send_keys(parameters.linkedin_username)
sleep(.5)

pswd = driver.find_element_by_id('login-password')
pswd.send_keys(parameters.linkedin_password)
sleep(.5)

lbtn = driver.find_element_by_id('login-submit')
lbtn.click()
sleep(5)

driver.get('https://www.google.com')
sleep(3)

search_query = driver.find_element_by_name('q')
search_query.send_keys(parameters.search_query)
sleep(.5)

search_query.send_keys(Keys.RETURN)

linkedin_urls = driver.find_elements_by_tag_name('cite')
linkedin_urls = [url.text for url in linkedin_urls
                 if 'linkedin.com' in url.text]
print(linkedin_urls)
sleep(.5)

driver.quit()
