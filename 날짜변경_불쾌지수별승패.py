# yyyy불쾌지스_승패.csv m-dd 로 되어 있는것 yyyy-mm-dd로 바꾸는 코드

import pandas as pd
import numpy as np

list_year=['2018','2019','2020']

for year in list_year:
    # 선수 명단 가지고 오기
    df = pd.read_csv('./dataSet/' + year + '불쾌지수_승패.csv')
    '''
    df = df.astype({'날짜': 'object'})
    df["날짜"] = year+"-0" + df["날짜"]
    '''
    df['날짜'] = pd.to_datetime(df['날짜'])

    df.to_csv('./dataSet/' + year + '불쾌지수_승패.csv', mode='w', index=False)

    print(df)
    print(df.info())

