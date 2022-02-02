from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
import urllib.request

if not os.path.exists('google_img/testdir'):
    os.mkdir('google_img/testdir')

url = "https://www.google.com/search?q=%EA%B3%A0%EC%96%91%EC%9D%B4&rlz=1C5CHFA_enKR980KR980&sxsrf=APq-WBuhFJzvGdnID-vp7mF_OQVQSKtWcQ:1643541356512&source=lnms&tbm=isch&sa=X&ved=2ahUKEwiZxOnVrNn1AhXJ4mEKHaxDAgMQ_AUoAXoECAIQAw&biw=1102&bih=638&dpr=2"
browser = webdriver.Chrome("")
browser.implicitly_wait(10)
browser.maximize_window()
browser.get(url)

# 무한 스크롤 처리
# 스크롤 전 높이
before_h = browser.execute_script("return window.scrollY")

# 무한 스크롤
while True:
    # 맨 아래로 스크롤을 내린다.
    browser.find_element_by_css_selector("body").send_keys(Keys.END)

    # 스크롤 사이 페이지 로딩 시간
    time.sleep(1)

    # 스크롤 후 높이
    after_h = browser.execute_script("return window.scrollY")

    if after_h == before_h:
        break
    before_h = after_h

# 썸네일 이미지 태그 추출
imgs = browser.find_element_by_css_selector("._image._listImage")

for i,img in enumerate(imgs, 1):
    # 이미지를 클릭해서 큰 사이즈를 찾아요
    img.click()
    time.sleep(1)

    # 큰 이미지 주소 추출
    target = browser.find_element_by_css_selector("img.n3VNCb")
    img_src = target.get_attribute('src')

    # 이미지 다운로드
    # 크롤링 하다보면 HTTP Error 403: Forbidden 에러가 납니다.
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-Agent', 'Mozila/5.0')]
    urllib.request.install_opener(opener)
    urllib.request.urlretrieve(img_src, f'google_img/고양이/{1}.jpg')