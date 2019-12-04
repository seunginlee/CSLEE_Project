import pandas as pd
import matplotlib as mlp
import matplotlib.pylab as plt
import numpy as np
import statsmodels.api as sm
from matplotlib.pylab import rc
from matplotlib import font_manager, rc
pd.options.mode.chained_assignment = None

rc('font',family='NanumGothic')
class Wilson_Analysis_System:
   def __init__(self, filename, encoding_value):
       self.origin = pd.read_csv(str(filename) + '.csv',  encoding=str(encoding_value))

   def sort(self, set_default, set_column_year_value, set_year_range, set_column_etc):
       self.origin_sort = pd.DataFrame(self.origin, columns=[str(set_default)])
       start = int(set_column_year_value)
       end = int(set_column_year_value)+int(set_year_range)
       for i in range(start, end):
           self.origin_sort[str(i) + str(set_column_etc)] = \
               self.origin[str(i) + str(set_column_etc)]
       return self.origin_sort

   def per_sort(self, set_default, set_default_name , set_column_year_value, set_year_range, set_column_etc):
       self.origin_per_sort = pd.DataFrame(self.origin, columns=[str(set_default)])
       start = int(set_column_year_value)
       end = int(set_column_year_value) + int(set_year_range)
       for i in range(start, end):
          self.origin_per_sort[str(i) + str(set_default_name)] = (self.origin[str(i) + str(set_column_etc)] / self.origin[
               str(i-1) + str(set_column_etc)]) - 1

       return self.origin_per_sort


WASX = Wilson_Analysis_System('C:/Users/user/Desktop/python/sodc', 'CP949')
WASY = Wilson_Analysis_System('C:/Users/user/Desktop/python/choolsan', 'CP949')
# WASX.sort('시도별',2007,11,' 1인당 개인소득 (천원)')
print(WASY.sort('시도별',2007,11,' 합계출산율')['2017 합계출산율'])
# print(WASX.per_sort('시도별', ' 소득증감률', 2008, 10, ' 1인당 개인소득 (천원)'))
# print(WASY.per_sort('시도별', ' 출산증감률', 2008, 10, ' 합계출산율'))

# color=['red','blue','green','gray','brown','yellow','purple','navy','green','green','green','green','green','green','green','green','green','green']
plt.barh(WASX.sort('시도별',2007,11,' 1인당 개인소득 (천원)')['시도별'],WASX.sort('시도별',2007,11,' 1인당 개인소득 (천원)')['2017 1인당 개인소득 (천원)'])
plt.grid()
plt.title('2017년 지역별 소득분포')
plt.xlabel('소득')
plt.ylabel('시도')
# pre_sale_2017

# plt.barh(pre_sale_2017['행정구역(시도)별'],pre_sale_2017['증가율'])
# plt.barh(WASX.sort('시도별',2007,11,' 합계출산율')['시도별'],WASY.sort('시도별',2007,11,' 합계출산율')['2017 합계출산율'])
plt.barh(WASY.sort('시도별',2007,11,' 합계출산율')['시도별'],WASY.sort('시도별',2007,11,' 합계출산율')['2017 합계출산율'])
# plt.title('2017년 지역별 출산율분포')
# plt.xlabel('출산율')
# plt.ylabel('시도')
# pre_sale_2017

def wilson(x,y):
   x = list(x)
   y = list(y)
#     plt.scatter(x,y)
   fit=np.polyfit(x,y,1) #회귀선 출력을 위한 코드
   fit_fn = np.poly1d(fit)
   ### 통계량 불러오는 코드
   z = pd.DataFrame({'x':x,'y':y})
   reg = sm.OLS.from_formula('x~y',z).fit()
   color = ['red','blue','green','black','orange','purple','yellow','navy','brown','slateblue','hotpink','red','red','red','red','red','red']
   for n in range(17):
       plt.text(x[n]*1.02,y[n]*0.98,WASY.sort('시도별',2007,11,' 합계출산율')['시도별'][n],fontsize=12)

   return plt.plot(x,y,'o',x,fit_fn(x),'r',color='r'),plt.grid(),plt.xlabel('1인당 개인소득 증가율'),plt.ylabel('출산율 증가율'), np.corrcoef(x,y), reg.summary(), plt.title('1인당 개인소득증가율과 출산율증가율의 상관관계')

x = WASX.sort('시도별',2007,11,' 1인당 개인소득 (천원)')['2017 1인당 개인소득 (천원)']
y = WASY.sort('시도별',2007,11,' 합계출산율')['2017 합계출산율']
wilson(x,y)
# wilson(income['2017.2'],birth['2017'])