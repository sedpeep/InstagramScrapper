import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.edge.options import Options
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC

# Login Credentials for Instagram
username = 'skiesarchivez'
password = 'PinkSkies.11.'

# The term you would like to search on Instagram
search_query = 'leomessi'

options = Options()
options.add_experimental_option("detach", True)
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

driver = webdriver.Edge(options=options)
driver.get("https://www.instagram.com/")


username_box = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[name="username"]')))
username_box.send_keys(username)

password_box = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[name="password"]')))
password_box.send_keys(password)

login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[type="submit"]')))
login_button.click()
time.sleep(6)

#redirect to the account
driver.get("https://www.instagram.com/skiesarchivez/")
time.sleep(3)
total_posts_elements=driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[1]/span/span")
total_posts=int(total_posts_elements.text)
print(total_posts)
posts_to_scrap =...
#Retrieve posts

posts = {}
posts = driver.find_elements(By.XPATH, "//div[starts-with(@class,'_aagw')]")

#cross_buttom = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div")
base_xpath = "/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/div[3]/article/div/div/div[{div1}]/div[{div2}]/a/div[1]/div[2]"
num = 0
div1 = 1
div2 = 1
likes = []
date_post = []
captions = []
caption = ''
while True:
    if num < total_posts:
        xpath = base_xpath.format(div1=div1, div2=div2)
        post_path = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        print(xpath)
        post_path.click()

        # Extracting likes
        likes.append(driver.find_element(By.XPATH,
                                     "/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[3]/div/div[2]/span/a/span/span").text)
        date_post.append(driver.find_element(By.XPATH,
                                         "/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/div[2]/div/div/a/span/time").text)
        # checking if caption is there
        element_xpath = "/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/div[1]/ul/div/li/div/div/div[2]/div[1]/h1"
        element = driver.find_element(By.XPATH, element_xpath)
        text_content = driver.execute_script("return arguments[0].innerText;", element)

        if caption == text_content:
            captions.append(text_content)

        print(likes)
        print(captions)
        print(date_post)
    # close the post
        webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()

    # Increment the counters according to the desired pattern
        num += 1
        div2 += 1
        if div2 > 3:
            div2 = 1
            div1 += 1

    # Scroll down after visiting 6 posts
        if num % 6 == 0:
            actions = ActionChains(driver)
            actions.send_keys(Keys.END).perform()
            for _ in range(10):  # You may need to adjust the range based on the page's length
                actions.send_keys(Keys.PAGE_DOWN).perform()
                time.sleep(2)  # You may need to adjust the sleep time based on the page's loading behavior
    else:
        break

driver.quit()

