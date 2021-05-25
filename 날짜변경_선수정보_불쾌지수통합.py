# 연도, 날짜가 분리되어 있는 것 연결
# 연결해준뒤 연도 컬럼 삭제
# 최종연결된 날짜컬럼의 자료형을 object -> datetime 변경
# 승패랑 불쾌지수까지 통합
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

    # 선수들 이름 담을 리스트
    searchList = []

    # 년도별 불쾌지수 정보
    df_year = pd.read_csv('./dataSet/' + year + '불쾌지수_승패.csv', encoding='UTF-8')

    for info in information:
        name = info[1]

        # 선수 명단 가지고 오기
        df_player = pd.read_csv('./dataSet/'+year+'선수정보수집/'+name+'선수정보.csv',encoding='UTF-8')

        # 날짜를 object형으로 변환
        # 근데 한번 실행후 하려니까 object를 object로 바꿀려고 하니 오류가 뜸
        # 그래서 주석 처리
        # df = df.astype({'연도': 'object'})

        # 연도, 날짜 이렇게 분리되어 있었는데 연결 해주고 연도를 삭제해서 두 번째 하려했을 때 오류나서 이 상태로 바꾸저ㅜㅁ
        # df["날짜"] = df["연도"].map(str) + "-" + df["날짜"]
        # df = df.drop(['연도','Unnamed: 0'], axis=1)

        # object -> datetime
        #df_player['날짜']=pd.to_datetime(df_player['날짜'])

        #자료 통합
        df_merge = pd.merge(left=df_year,
                            right=df_player,
                            how='inner')

        #자료 저장
        df_merge.to_csv('./dataSet/' + year + '선수정보_불쾌지수/' + name + '.csv', mode='w', index=False)

        #print(df.info())