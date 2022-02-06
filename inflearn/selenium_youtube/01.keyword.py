from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup

url = ""

browser = webdriver.Chrome("")
browser.implicitly_wait(10)
browser.maximize_window()
browser.get(url)

# 7번 스크롤하기
scroll_count = 7

i = 1
while True:
    # 맨 아래로 스크롤을 내린다.
    browser.find_element_by_css_selector("body").send_keys(Keys.END)

    # 스크롤 사이에 페이지 로딩 시간
    time.sleep(2)

    if i == scroll_count:
        break
    i += 1

# selenium - Beautifulsoup 연동방법
html = browser.page_source
soup = BeautifulSoup(html, 'html.parser')
infos = soup.select("div.text-wrapper")

for info in infos:
    # 원하는 정보 가져오기
    # 제목
    title = info.select_one("a#video-title").text

    try:
        # 조회수
        views = info.select_one("div#metadata-line > span:nth-child(1)").text
        # 날짜
        date = info.select_one("div#metadata-line > span:nth-child(2)").text
    except:
        views = "조회수 0회"
        date = "날짜 없음"

print(title, views, date)