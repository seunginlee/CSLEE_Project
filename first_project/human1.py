import pandas as pd

# pop_Seoul = pd.read_excel('Report.xls',  encoding='utf-8')
pop_Seoul = pd.read_excel('Report.xls',
                          header = 2,   # 두줄 건너띄어 읽기
                          usecols = 'B, D, G, J, N',
                          encoding='utf-8')
# 컴럼명 지정
pop_Seoul.rename(columns={pop_Seoul.columns[0] : '구별',
                          pop_Seoul.columns[1] : '인구수',
                          pop_Seoul.columns[2] : '한국인',
                          pop_Seoul.columns[3] : '외국인',
                          pop_Seoul.columns[4] : '고령자'}, inplace=True)
pop_Seoul.drop([0], inplace=True)   # 첫번째 합계 통계에서 배제
print(pop_Seoul[pop_Seoul['구별'].isnull()]) #None 걸럼 검색
# 외국인비율과 고령자비율 컬럼 추가
pop_Seoul['외국인비율'] = pop_Seoul['외국인'] / pop_Seoul['인구수'] * 100
pop_Seoul['고령자비율'] = pop_Seoul['고령자'] / pop_Seoul['인구수'] * 100

#인구수 분포별 많은 사람순으로
print(pop_Seoul.sort_values(by='인구수', ascending=False).head(5))

#외국인 분포별 많은 사람순으로
print(pop_Seoul.sort_values(by='외국인', ascending=False).head(5))

#외국인 분포별 많은 사람순으로
print(pop_Seoul.sort_values(by='외국인비율', ascending=False).head(5))

#외국인비율 분포별 많은 사람순으로
print(pop_Seoul.sort_values(by='외국인비율', ascending=False).head(5))

#고령자 분포별 많은 사람순으로
print(pop_Seoul.sort_values(by='고령자', ascending=False).head(5))

#고령자비율별 많은 사람순으로
print(pop_Seoul.sort_values(by='고령자비율', ascending=False).head(5))
# print(pop_Seoul.head())