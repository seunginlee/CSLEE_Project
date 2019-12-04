from bs4 import BeautifulSoup
from selenium import webdriver
import re

def youtube_crawler(search_key, n_limit=1):

    search_key = '토익'
    driver = webdriver.Chrome(executable_path = r'C:\Users\user\Downloads\chromedriver_win32\chromedriver.exe')
    # driver = _get_chrome_driver(driver_path)
    driver.implicitly_wait(1) # 암묵적으로 웹 자원 로드를 위해 3초까지 기다려 준다.

    driver.get('https://www.youtube.com/results?search_query=%s' % (search_key))
    video_list_html = driver.page_source
    video_list_html = BeautifulSoup(video_list_html, 'html.parser')

    tags = video_list_html.select('ytd-video-renderer')
    #ytd-video-renderer 태그를 모두 복사해온다.
    data_list = []
    for i, tag in enumerate(tags):

        y_url_tag = tag.find('a', attrs={'id': 'thumbnail'})
        y_url = y_url_tag['href']
        #url의 thumbnail부분만 가져옴
        #print(y_url)

        driver.get('https://www.youtube.com' + (y_url))
        video_list_html = driver.page_source
        video_list_html = BeautifulSoup(video_list_html, 'html.parser')
        tag = video_list_html.select('ytd-video-primary-info-renderer')
        print(tag)
        #문장 정규표현식으로 검색해보기 ... 내일을 위해서 잔다... 잠은 안오지만....
        #
        # regex = re.compile('좋아요')
        # like_count = regex.search(video_list_html)
        # print(like_count)

        # for i, tag in enumerate(tag):
        #     like_count_tag = tag.find('yt-formatted-string', attrs={'id': 'text'})
        #     like_count = like_count_tag.text.strip()
        #     print(like_count)
            # tag.find('yt-formatted-string',attrs={'aria-label': '싫어요' })
            # print(like_count_tag)
            # like_count = like_count_tag.text.strip()
            # 하나 건너띄기


            # hate_count_tag = tag.find('yt-formatted-string', attrs={'id': 'text'})
            # hate_count = hate_count_tag.text.strip()

        data_list.append({
            'y_url': y_url,
            # 'likeCount': like_count,
            #'hateCount': hate_count
            })

        if len(data_list) == n_limit:
            break

        #driver.quit()
    return data_list
#함수 안으로 빼줘야함
if __name__ == "__main__":
    search_key = '영어'
    data_list = youtube_crawler(search_key, n_limit=1)
    for data in data_list:
        print(data)
    # youtube_crawler()