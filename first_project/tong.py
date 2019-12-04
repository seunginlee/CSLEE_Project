import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import platform

from matplotlib import font_manager, rc
pd.options.mode.chained_assignment = None
Sodc = pd.read_csv('sodc.csv',  encoding='CP949') # 읽어오고
Choolsan = pd.read_csv('choolsan.csv',  encoding='CP949') # 읽어오고 2007 합계출산율
# print(Choolsan)
pre_sale_2017 = Sodc[['시도별' , '2016 1인당 개인소득 (천원)' , '2017 1인당 개인소득 (천원)']] # 열 축소
Choolsan_2017 = Choolsan[['시도별' , '2016 합계출산율' , '2017 합계출산율']] # 열 축소
pre_sale_2017['증가율'] = (pre_sale_2017['2017 1인당 개인소득 (천원)'] / pre_sale_2017['2016 1인당 개인소득 (천원)'])-1
Choolsan_2017['증가율'] = (Choolsan_2017['2017 합계출산율'] / Choolsan_2017['2016 합계출산율'])-1
# print(Choolsan_2017)
# print(pre_sale_2017) # 증가율 출력