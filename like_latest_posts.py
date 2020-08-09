from getpass import getpass
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from common_methods import Wait

username = input('enter your username : ')
password = getpass('enter your password : ')
username_to_be_liked = input(
    'enter username to be liked : ')


# Setup webdriver
driver = webdriver.Chrome()
wait = Wait(driver, time=40)

# Open Instagram
driver.get('https://instagram.com')

# Login current user
wait.get_by_xpath('//input[@name="username"]').send_keys(username)
driver.find_element_by_xpath("//input[@name='password']").send_keys(password)
driver.find_element_by_xpath('//form[@id="loginForm"]').submit()


wait.get_by_xpath(
    '//*[@id="react-root"]/section/nav/div[2]/div/div/div[1]/a')

# Search
wait.get_by_xpath(
    '//div[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input[@placeholder="Search"]'
).send_keys(username_to_be_liked)

# Select from search results
wait.get_by_xpath(
    '//div[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[3]/div[2]/div/a[1]').click()

# Find posts area
post_area = wait.get_multiple_by_xpath(
    '//*[@id="react-root"]/section/main/div/div')[-1]

# Select first pic
post_area.find_element_by_xpath('article/div[1]/div/div[1]/div[1]/a').click()

# like picture if it isn't already liked
like_button = wait.get_by_xpath(
    '/html/body/div[4]/div[2]/div/article/div[3]/section[1]/span[1]/button')
like_icon = like_button.find_element_by_tag_name('svg')
if(like_icon.get_attribute('aria-label') == 'Like'):
    like_button.click()