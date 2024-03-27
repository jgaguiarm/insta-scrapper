from instascrape import Post
from selenium import webdriver
from time import sleep
from datetime import datetime

navegator = webdriver.Chrome()
navegator.get("https://www.instagram.com/p/C20bda3O4yP/")
sleep(20)

post = Post("https://www.instagram.com/p/C20bda3O4yP/")
post.scrape()
comments = post.get_recent_comments()

for comment in comments:
    print(f"{comment.username} => {comment.text}")

    more_comments = driver.find_element(By.XPATH, '//div[@class="_abm0"')