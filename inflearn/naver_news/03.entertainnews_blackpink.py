import requests
from bs4 import BeautifulSoup

response = requests.get("https://search.naver.com/search.naver?where=news&sm=tab_jum&query=%EB%B8%94%EB%9E%99%ED%95%91%ED%81%AC")
html = response.text
soup = BeautifulSoup(html, 'html.parser')
articles = soup.select("div.info_group") # 뉴스 기사 div 10개 추출

for article in articles:
    links = article.select("a.info") # 리스트
    if len(links) >= 2: # 링크가 2개 이상이면
        url = links[1].attrs['href'] # 두번째 링크의 href를 추출
        response = requests.get(url, headers={'User-agent':'Mozila/5.0'})
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        # 만약 연예 뉴스라면
        if "entertain" in response.url:
            title = soup.select_one(".end_tit")
            content = soup.select_one("#articeBody")
        else:
            title = soup.select_one("#articleTitle")
            content = soup.select_one("#articleBodyContents")

        print("==========링크==========\n", url)
        print("==========제목==========\n", title.text.strip())
        print("==========본문==========\n", content.text.strip())
