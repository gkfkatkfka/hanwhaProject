# 1단계랑 2단계 통합해서 => 1
# 3단계 => 2단계
# 4단계 => 3

import csv
import pandas as pd

# 연도 리스트
list_year = ['2018', '2019', '2020']

for year in list_year:
    '''선수들 이름 가져오기'''
    # 선수 이름 파일 선택
    f = open('./dataSet/' + year + '한화선수명단.csv', 'r', encoding='UTF-8')

    # csv 파일 하나를 읽어옴
    information = csv.reader(f)

    # 헤더 데이터 패스!
    header = next(information)

    for info in information:
        name = info[1]

        # 선수 명단 가지고 오기
        df = pd.read_csv('./dataSet/'+year+'선수정보_불쾌지수/'+name+'.csv',encoding='UTF-8')
        df.loc[df.단계==2,'단계']=1
        df.loc[df.단계 == 3, '단계'] = 2
        df.loc[df.단계 == 4, '단계'] = 3
        df.to_csv('./dataSet/' + year + '선수정보_단계변경/' + name + '.csv', mode='w', index=False)
        print(df)

        df2 = pd.read_csv('./dataSet/' + year + '불쾌지수_승패.csv', encoding='UTF-8')
        df2.loc[df2.단계 == 2, '단계'] = 1
        df2.loc[df2.단계 == 3, '단계'] = 2
        df2.loc[df2.단계 == 4, '단계'] = 3
        df2.to_csv('./dataSet/' + year + '불쾌지수_승패_단계변경.csv', mode='w', index=False)
        print(df2)


