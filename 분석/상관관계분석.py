# 상관관계 설명 코드
# 결과값 및 시각화까지 담당
# 문득 얘는 상관관계 분석이 아니라 회귀분석을 해야겠다는 생각이 들음
# 그래서 이거는 없는걸로! 짱


import pandas as pd
import matplotlib.pyplot as plt

year_list=['2018','2019','2020']

for year in year_list:
    # 날짜, 단계, 승패여부 가지고 옴
    df = pd.read_csv('..\\dataSet\\'+year+'불쾌지수_승패.csv', encoding='UTF-8')
    corrData = df[['단계','승패여부']]

    # 두 변수간의 상관관계 분석
    corr1 =corrData['단계'].corr(corrData['승패여부'])
    corr2 = df['승패여부'].corr(df['단계'])

    print(corr1)
    print(corr2)