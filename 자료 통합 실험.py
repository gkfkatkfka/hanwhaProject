# 연도, 날짜가 분리되어 있는 것 연결
# 연결해준뒤 연도 컬럼 삭제
# 최종연결된 날짜컬럼의 자료형을 object -> datetime 변경

import csv
import pandas as pd

# 연도 리스트
list_year = ['2018', '2019', '2020']

for year in list_year:
    # 년도별 불쾌지수 정보
    df_year =pd.read_csv('./dataSet/' + year + '불쾌지수_승패.csv',encoding='UTF-8')

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
        df_player = pd.read_csv('./dataSet/'+year+'선수정보수집/'+name+'선수정보.csv',encoding='UTF-8')
        df_merge=pd.merge(left=df_year,
                          right=df_player,
                          how='inner')
        df_merge = df_merge.drop(['Unnamed: 0.1'], axis=1)
        df_merge.to_csv('./dataSet/' + year + '선수정보_불쾌지수/' + name + '.csv', mode='w', index=False)
