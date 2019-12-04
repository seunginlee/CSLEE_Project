import json
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
import os
#import time
import urllib.request
import requests
print(webdriver.__version__)
import bs4
print(bs4.__version__)
def _get_chrome_driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")
    chrome_options.add_argument("lang=ko_KR")
    driver = webdriver.Chrome('/usr/bin/chromedriver', options=chrome_options)
    # driver = webdriver.Chrome('./driver/chromedriver.exe')

    return driver

def youtube_crawler(search_key, n_limit=10):
    search_key =  '영어 ' + search_key
    driver = _get_chrome_driver()
    driver.implicitly_wait(1)  # ???{8??% Z??? '? 3??? ???????

    driver.get('https://www.youtube.com/results?search_query=%s' % (search_key))
    video_list_html = driver.page_source
    video_list_html = BeautifulSoup(video_list_html, 'html.parser')

    tags = video_list_html.select('ytd-video-renderer')

    data_list = []
    for i, tag in enumerate(tags):
        y_title_tag = tag.find('a', attrs={'id': 'video-title'})
        y_title = y_title_tag.text.strip()
        y_view_cnt = y_title_tag['aria-label'].split()[-1]

        y_url_tag = tag.find('a', attrs={'id': 'thumbnail'})
        y_url = y_url_tag['href']

        y_thumbnail_tag = tag.find('img', attrs={'class': 'style-scope yt-img-shadow'})
        if 'src' in y_thumbnail_tag.attrs:
            y_thumbnail = y_thumbnail_tag['src']
        else:
            continue

        y_content_tag = tag.find('yt-formatted-string', attrs={'id': 'description-text'})
        y_content = y_content_tag.text.strip()

        y_writer_tag = tag.find('a', attrs={'class': 'yt-simple-endpoint style-scope yt-formatted-string'})
        y_writer = y_writer_tag.text.strip()
        				
        driver.close()			
        driver = _get_chrome_driver()
        driver.implicitly_wait(3) # 암묵적으로 웹 자원 로드를 위해 3초까지 기다려 준다.
        url='https://www.youtube.com' + (y_url) #기존의 drive을 다시 열면 source 원본이 나옵니다.
        response = requests.get(url=url) #requests함수 사용합니다.
        tags2 = BeautifulSoup(response.text, 'html.parser')

        tags_like = tags2.find('span',{'class':'like-button-renderer'})
        like_count = tags_like.find_all('span', {'class': 'yt-uix-button-content'})

        like_count , hate_count = like_count[0].string , like_count[3].string
        
        data_list.append({
            'title': y_title,
            'url': y_url,
            'thumbnail': y_thumbnail,
            'content': y_content,
            'author': y_writer,
            'viewCount': y_view_cnt,
            'likeCount': like_count,
            'hateCount': hate_count
        })

        if len(data_list) == n_limit:
            break
    
    driver.quit()
    return data_list
   