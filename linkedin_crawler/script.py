from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
import parameters
from parsel import Selector
import csv


def clean_and_validate_field(field):
    if field:
        return field.strip()
    else:
        return ''


writer = csv.writer(open(parameters.file_name, 'w+'))
writer.writerow(['Name', 'Job Title', 'Location', 'School', 'URL'])

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

for linkedin_url in linkedin_urls:
    driver.get(linkedin_url)
    sleep(5)

    sel = Selector(text=driver.page_source)

    name = sel.xpath('//h1/text()').extract_first()
    job_title = sel.xpath('//h2/text()').extract_first()
    school = sel.xpath(
        '//*[@href="#education-section"]/span/text()').extract_first()
    location = sel.xpath(
        '//h3[starts-with(@class, "pv-top-card-section__location")]/text()').extract_first()

    name = clean_and_validate_field(name)
    job_title = clean_and_validate_field(job_title)
    school = clean_and_validate_field(school)
    location = clean_and_validate_field(location)
    linkedin_url = clean_and_validate_field(linkedin_url)

    scraped_data = {
        'Name': name,
        'Job Title': job_title,
        'School': school,
        'Location': location,
        'URL': linkedin_url
    }

    for k, v in scraped_data.items():
        print(k + ': ' + v)

    # writer.writerow([
    #     name,
    #     job_title,
    #     school,
    #     location,
    #     linkedin_url
    # ])
    writer.writerow([
        name.encode('utf-8'),
        job_title.encode('utf-8'),
        school.encode('utf-8'),
        location.encode('utf-8'),
        linkedin_url.encode('utf-8')
    ])

    # try:
    #     driver.find_element_by_xpath('//span[text()="Connect"]').click()
    #     sleep(3)
    #     driver.find_element_by_xpath(
    #         '//*[@class="button-primary-large ml3"]').click()
    #     sleep(3)
    # except:
    #     pass

driver.quit()
