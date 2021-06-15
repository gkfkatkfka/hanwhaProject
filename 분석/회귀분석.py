# 종속변수 : 여러가지 타자 스탯들
# 독립변수 : 불쾌지수
# 각 단순 스탯들과 불쾌지수 간의 인과관계 파악을 위해 작성

import csv
import pandas as pd

# 한글 폰트 사용을 위해서 세팅
from matplotlib import font_manager, rc

# 연도 리스트
from matplotlib import pyplot as plt

font_path = "C:/Windows/Fonts/NANUMGOTHIC.TTF"
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)

statList=['타수', '득점', '안타',
            '2타','3타', '홈런', '루타',
            '타점','도루', '도실','볼넷',
            '사구', '고4','삼진', '병살',
            '희타', '희비', '타율', '출루',
            '장타', 'OPS', '투구', 'avLI',
            'RE24', 'WPA']



list_year = ['2018', '2019', '2020']

for year in list_year:
    # 선수 이름 파일 선택
    f = open('../dataSet/' + year + '한화선수명단.csv', 'r', encoding='UTF-8')

    # csv 파일 하나를 읽어옴
    information = csv.reader(f)

    # 헤더 데이터 패스!
    header = next(information)

    # 선수들 이름 담을 리스트
    searchList = []
    
    for info in information:
        name = info[1]

        # 선수 명단 가지고 오기
        df = pd.read_csv('../dataSet/' + year + '선수정보_불쾌지수/' + name + '.csv', encoding='UTF-8')

        for stat in statList:
            pivot = pd.pivot_table(df,
                               index = ['단계'],
                               values = stat)

            print(year)
            print(pivot)

            plt.rc('font', family=font)
            pivot.plot.bar()
            plt.title(year+'년 '+name+' 불쾌지수 단계와 '+stat)
            plt.xlabel('불쾌지수')
            plt.ylabel(stat+'평균')
            plt.show()