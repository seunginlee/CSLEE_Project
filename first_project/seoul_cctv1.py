import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

import platform

from matplotlib import font_manager, rc
plt.rcParams['axes.unicode_minus'] = False
if platform.system() == 'Darwin':
    rc('font', family='AppleGothic')
elif platform.system() == 'Windows':
    path = "c:/Windows/Fonts/malgun.ttf"
    font_name = font_manager.FontProperties(fname=path).get_name()
    rc('font', family=font_name)
else:
    print('Unknown system... sorry~~~~')

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

# 상관지수 0이하 무시 0~0.3 : 약학상관, 0.3~0.7:중간상관,0.7 이상 강한상관
#고령자비율과 CCTV 상관관계지수 뽑기  -0.26783452
print(np.corrcoef(data_result['고령자비율'],data_result['소계']))
#외국인비율과 CCTV 상관관계지수 뽑기  -0.04656978
print(np.corrcoef(data_result['외국인비율'],data_result['소계']))
#인구수과 CCTV 상관관계지수 뽑기 0.23037183
print(np.corrcoef(data_result['인구수'],data_result['소계']))