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

# iframe 안으로 들어가기
browser.switch_to.frame("searchIframe")

# browser.switch_to_default_content() iframe 밖으로 나오기

# iframe 안쪽을 한번 클릭하기
browser.find_element_by_css_selector("#_pcmap_list_scroll_container").click()

# 로딩된 데이터 개수 확인
lis = browser.find_element_by_css_selector("li._3t81n")
before_len = len(lis)

while True:
    # 맨 아래로 스크롤 내린다.
    browser.find_element_by_css_selector("body").send_keys(Keys.END)

    # 스크롤 사이 페이지 로딩 시간
    time.sleep(1.5)

    # 스크롤 후 로딩된 데이터 개수 확인
    lis = browser.find_element_by_css_selector("li._3t81n")
    after_len = len(lis)

    print("스크롤 전", before_len, "스크롤 후", after_len)

    # 로딩된 데이터 개수가 같다면 반복 멈춤
    if before_len == after_len:
        break
    before_len = after_len