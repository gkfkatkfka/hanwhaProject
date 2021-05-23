import pandas as pd

list_year=['2018','2019','2020']

for year in list_year:
    # 파일 불러오기
    weather = pd.read_csv('./dataSet/'+year+'최종불쾌지수.csv')
    WinLose = pd.read_csv('./dataSet/'+year+'승패기록.csv')
    
    # 날짜로 파일 묶기
    mergeFile = pd.merge(weather, WinLose, on='날짜')

    mergeFile.drop('Unnamed: 0_x', axis=1)
    mergeFile.drop('불쾌지수', axis=1)

    # 새로운 파일 만들기
    mergeFile.to_csv('./dataSet/'+year+'불쾌지수_승패.csv')

