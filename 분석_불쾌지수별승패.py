import pandas as pd

year_list=['2018','2019','2020']

for year in year_list:
    df = pd.read_csv('.\\dataSet\\'+year+'불쾌지수_승패.csv', encoding='UTF-8')

    df_subset = df[['단계', '승패여부']]

    corr1 = df_subset['단계'].corr(df_subset['승패여부'])

    print(year+'년 불쾌지수와 승패여부 상관계수 : {:.2f}'.format(corr1))