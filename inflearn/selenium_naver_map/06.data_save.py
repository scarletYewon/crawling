from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pyautogui
import openpyxl

keyword = pyautogui.prompt("검색어를 입력하세요")

wb = openpyxl.Workbook()
ws = wb.create_sheet(keyword)
ws.append(["순위","이름","별점","방문자리뷰","블로그리뷰"])

browser = webdriver.Chrome("c:/chromedriver.exe")
browser.get("http://map.naver.com/v5/")
browser.implicitly_wait(10)
browser.maximize_window()

# 검색창 입력
search = browser.find_element_by_css_selector("input.input_search")
search.click()
time.sleep(1)
search.send_keys(keyword)
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

# 데이터 기다리는 시간을 0으로 만들어 줘요. (데이터가 없더라도 빠르게 넘어감)
browser.implicitly_wait(0)

rank = 1
for li in lis:
    # 광고 상품 아닌 것만
    if len(li.find_element_by_css_selector("svg._2ulu3")) > 0:
        # 별점이 있는 것만
        if len(li.find_element_by_css_selector("span._3Yzhl._1ahw0 > em")) > 0:
            # 가게명
            name = li.find_element_by_css_selector("span._3Yilt").text
            # 별점
            star = li.find_element_by_css_selector("span._3Yzhl._1ahw0 > em").text
            # 영업시간이 있다면
            if len(li.find_element_by_css_selector("span._3Yzhl._1cf4n")) > 0:
                # 방문자 리뷰수
                try:
                    visit_review = li.find_element_by_css_selector("span._3Yzhl:nth-child(3)").text
                except:
                    visit_review = "0"
                # 블로그 리뷰수
                try:
                    blog_review = li.find_element_by_css_selector("span._3Yzhl:nth-child(4)").text
                except:
                    blog_review = "0"
            # 영업시간이 없다면
            else:
                # 방문자 리뷰수
                try:
                    visit_review = li.find_element_by_css_selector("span._3Yzhl:nth-child(2)").text
                except:
                    visit_review = "0"
                # 블로그 리뷰수
                try:
                    blog_review = li.find_element_by_css_selector("span._3Yzhl:nth-child(3)").text
                except:
                    blog_review = "0"

            # 데이터 전처리
            visit_review = visit_review.replace("방문자리뷰 ", "").replace(",", "")
            blog_review = blog_review.replace("블로그리뷰 ", "").replace(",", "")

            print(rank, name, star, visit_review, blog_review)
            ws.append([rank, name, float(star), int(visit_review), int(blog_review)])
            rank += 1

wb.save(f"selenium_naver_map/{keyword}.xlsx")