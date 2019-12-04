import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import platform

from matplotlib import font_manager, rc

CCTV_Seoul = pd.read_csv('cctv_in_seoul.csv',  encoding='utf-8')
#CCTV 컴럼명 변경
CCTV_Seoul.rename(columns={CCTV_Seoul.columns[0] : '구별'}, inplace=True)

pop_Seoul = pd.read_excel('Report.xls',
                          header = 2,   # 두줄 건너띄어 읽기
                          usecols = 'B, D, G, J, N',
                          encoding='utf-8')
#서울인구 컴럼명 변경
pop_Seoul.rename(columns={pop_Seoul.columns[0] : '구별',
                          pop_Seoul.columns[1] : '인구수',
                          pop_Seoul.columns[2] : '한국인',
                          pop_Seoul.columns[3] : '외국인',
                          pop_Seoul.columns[4] : '고령자'}, inplace=True)

# 외국인비율과 고령자비율 컬럼 추가
pop_Seoul['외국인비율'] = pop_Seoul['외국인'] / pop_Seoul['인구수'] * 100
pop_Seoul['고령자비율'] = pop_Seoul['고령자'] / pop_Seoul['인구수'] * 100

# CCTV 테이블과 서울 인구 테이블 구별 기준으로 병합
data_result = pd.merge(CCTV_Seoul, pop_Seoul, on='구별')
# 의미 없는 컬럼 제거
del data_result['2013년도 이전']
del data_result['2014년']
del data_result['2015년']
del data_result['2016년']
print(data_result.head())

#Index값을 일변번호에서 구별로 변경 설정
data_result.set_index('구별', inplace=True)
print(data_result.head())

# # 상관지수 0이하 무시 0~0.3 : 약학상관, 0.3~0.7:중간상관,0.7 이상 강한상관
# #고령자비율과 CCTV 상관관계지수 뽑기  -0.26783452
# print(np.corrcoef(data_result['고령자비율'],data_result['소계']))
# #외국인비율과 CCTV 상관관계지수 뽑기  -0.04656978
# print(np.corrcoef(data_result['외국인비율'],data_result['소계']))
# #인구수과 CCTV 상관관계지수 뽑기 0.23037183
# print(np.corrcoef(data_result['인구수'],data_result['소계']))

#한글폰트 처리하기
plt.rcParams['axes.unicode_minus'] = False
if platform.system() == 'Darwin':
    rc('font', family='AppleGothic')
elif platform.system() == 'Windows':
    path = "c:/Windows/Fonts/malgun.ttf"
    font_name = font_manager.FontProperties(fname=path).get_name()
    rc('font', family=font_name)
else:
    print('Unknown system... sorry~~~~')

# #구별 ,CCTV 소계 차트 출력
# plt.figure()
# # 크기:figsize=(10,10)넓이, 높이 inch 기준
# # data_result['소계'].plot(kind='barh', grid=True, figsize=(10,10))
# data_result['소계'].sort_values().plot(kind='barh',
#                                      grid=True, figsize=(10,10))
# plt.show()

# CCTV비율별 분포도
# plt.figure()
# data_result['CCTV비율'] = data_result['소계'] / data_result['인구수'] * 100
#
# data_result['CCTV비율'].sort_values().plot(kind='barh',
#                                          grid=True, figsize=(10,10))
# plt.show()

# 인구수별 CCTV 분포도(산포도)
# plt.figure(figsize=(6,6))
# plt.scatter(data_result['인구수'], data_result['소계'], s=50)
# plt.xlabel('인구수')
# plt.ylabel('CCTV')
# plt.grid()
# plt.show()

#인구수를 대표하는 라인을 대표하는 직선 구하기
# fp1 = np.polyfit(data_result['인구수'], data_result['소계'], 1)
# #y축값 구하기
# f1 = np.poly1d(fp1)
# #x축값 구하기
# fx = np.linspace(100000, 700000, 100)
# plt.figure(figsize=(10,10))
# plt.scatter(data_result['인구수'], data_result['소계'], s=50)
# # 라인값 설정
# plt.plot(fx, f1(fx), ls='dashed', lw=3, color='g')
# # x축, y축 라벨 설정
# plt.xlabel('인구수')
# plt.ylabel('CCTV')
# plt.grid()
# plt.show()

#통합차트 구성
fp1 = np.polyfit(data_result['인구수'], data_result['소계'], 1)

f1 = np.poly1d(fp1)
fx = np.linspace(100000, 700000, 100)
# 수평직선과의 오차값을 구해서 컬럼 추가
data_result['오차'] = np.abs(data_result['소계'] - f1(data_result['인구수']))

# 오차기준으로 정렬
df_sort = data_result.sort_values(by='오차', ascending=False)

#출력이미지 사이즈 결정
plt.figure(figsize=(14, 6))
plt.scatter(data_result['인구수'], data_result['소계'],
            c=data_result['오차'], s=50)
plt.plot(fx, f1(fx), ls='dashed', lw=3, color='g')
# 오차 정보 출력하며, 문자열 함께 출력
for n in range(10):
    plt.text(df_sort['인구수'][n] * 1.02, df_sort['소계'][n] * 0.98,
             df_sort.index[n], fontsize=12)
#라벨 지정
plt.xlabel('인구수')
plt.ylabel('인구당비율')
#오른쪽 칼라바 출력
plt.colorbar()
plt.grid()
plt.show()