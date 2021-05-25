# 도류를 도루로 바꿔주는 코드

import csv
import pandas as pd

# 연도 리스트
list_year = ['2018', '2019', '2020']

for year in list_year:
    # 선수 이름 파일 선택
    f = open('./dataSet/' + year + '한화선수명단.csv', 'r', encoding='UTF-8')

    # csv 파일 하나를 읽어옴
    information = csv.reader(f)

    # 헤더 데이터 패스!
    header = next(information)

    # 선수들 이름 담을 리스트
    searchList = []

    for info in information:
        name = info[1]

        # 선수 명단 가지고 오기
        df = pd.read_csv('./dataSet/'+year+'선수정보수집/'+name+'선수정보.csv')

        df.rename(columns={'도류': '도루'}, inplace=True)
        #print(df.info())
        df.to_csv('./dataSet/' + year + '선수정보수집/' + name + '선수정보.csv', mode='w', index=False)