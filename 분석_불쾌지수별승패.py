import pandas as pd

year_list=['2018','2019','2020']

for year in year_list:
    df = pd.read_csv('.\\dataSet\\'+year+'불쾌지수_승패.csv', encoding='UTF-8')

    # 단계와 승패여부와의 상관관계 분석
    corr1 = df['단계'].corr(df['승패여부'])


    print(year+'년 불쾌지수와 승패여부 상관계수 : {:.2f}'.format(corr1))