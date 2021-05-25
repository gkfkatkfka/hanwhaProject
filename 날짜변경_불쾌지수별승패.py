# yyyy불쾌지스_승패.csv m.dd 로 되어 있는것 yyyy-mm-dd로 바꾸는 코드
import pandas as pd
import numpy as np

list_year=['2018','2019','2020']

for year in list_year:
    # 파일 불러오기
    df = pd.read_csv('./dataSet/'+year+'불쾌지수_승패.csv')

    # 날짜 float64로 되어 있으므로 object로 수정
    df = df.astype({'날짜': 'object'})

    print(df['날짜'].values)
