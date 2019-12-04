from bs4 import BeautifulSoup
from selenium import webdriver


def youtube_crawler(search_key, n_limit=20):

    """
    :param search_key:
    :param n_limit:
    :return:
    """


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
        y_title_tag = tag.find('a', attrs={'id': 'video-title'})
        y_title = y_title_tag.text.strip()
        #제목 문자열을 저장함

        y_view_cnt = y_title_tag['aria-label'].split()[-1]
        # aria-label : 현재 요소에 레이블을 지정하는 문자열 값을 정의
        #split()[-1]  맨뒤 요소 저장
        #조회수
# -> json 파일에서 그 부분만 가져다 쓰는것

        y_url_tag = tag.find('a', attrs={'id': 'thumbnail'})
        y_url = y_url_tag['href']
        #url의 thumbnail부분만 가져옴

        y_thumbnail_tag = tag.find('img', attrs={'class': 'style-scope yt-img-shadow'})

    #img 태그의 src 부분을 가져옴 아님 넘기고
        if 'src' in y_thumbnail_tag.attrs:
            y_thumbnail = y_thumbnail_tag['src']
        else:
            continue

        y_content_tag = tag.find('yt-formatted-string', attrs={'id': 'description-text'})
        y_content = y_content_tag.text.strip()
#문자열 content 부분 가져옴

        y_writer_tag = tag.find('a', attrs={'class': 'yt-simple-endpoint style-scope yt-formatted-string'})
        y_writer = y_writer_tag.text.strip()
        #유튜브명?
        data_list.append({
            'title': y_title,
            'url': y_url,
            'thumbnail': y_thumbnail,
            'content': y_content,
            'author': y_writer,
            'viewCount': y_view_cnt,
            })

        if len(data_list) == n_limit:
            break

        #driver.quit()
    return data_list
#함수 안으로 빼줘야함
if __name__ == "__main__":
    search_key = '영어'
    data_list = youtube_crawler(search_key, n_limit=10)
    for data in data_list:
        print(data)
    # youtube_crawler()