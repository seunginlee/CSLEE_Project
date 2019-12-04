import pandas as pd
CCTV_Seoul = pd.read_csv('cctv_in_seoul.csv',  encoding='utf-8')

# 컬럼의 기관명을 구별로 변경
CCTV_Seoul.rename(columns={CCTV_Seoul.columns[0] : '구별'}, inplace=True)
# print(CCTV_Seoul.head())
#CCTV 적은 Top5
# print(CCTV_Seoul.sort_values(by='소계', ascending=True).head(5))
#CCTV 많은 Top5
print('CCTV 많은 Top5')
print(CCTV_Seoul.sort_values(by='소계', ascending=False).head(5))
#최근 설치된 CCTV 많은 Top5
print(CCTV_Seoul.sort_values(by='2016년', ascending=False).head(5))
#최근3년도 안의 최근 증가율이 많은 Top5
# CCTV_Seoul['최근증가율'] = (CCTV_Seoul['2016년'] + CCTV_Seoul['2015년'] +
#                         CCTV_Seoul['2014년']) / CCTV_Seoul['2013년도 이전']  * 100
# print(CCTV_Seoul.sort_values(by='최근증가율', ascending=False).head(5))