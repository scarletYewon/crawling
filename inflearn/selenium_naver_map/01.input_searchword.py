from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome("c:/chromedriver.exe")
browser.get("http://map.naver.com/v5/")
browser.implicitly_wait(10)
browser.maximize_window()

# 검색창 입력
search = browser.find_element_by_css_selector("input.input_search")
search.click()
time.sleep(1)
search.send_keys("강남역 맛집")
time.sleep(1)
search.send_keys(Keys.ENTER)
time.sleep(2)