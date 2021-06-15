# 종속변수 : 여러가지 타자 스탯들
# 독립변수 : 불쾌지수
# 각 단순 스탯들과 불쾌지수 간의 인과관계 파악을 위해 작성

import csv
import pandas as pd
from matplotlib import pyplot as plt

# 한글 폰트 사용을 위해서 세팅
from matplotlib import font_manager, rc


font_path = "C:/Windows/Fonts/NANUMGOTHIC.TTF"
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)

hitting_statList=['안타', '2타', '3타', '홈런', '타점']
seeing_statList=['볼넷', '삼진']
percent_statList=['타율', '출루', '장타','OPS']
steal_statList=['도루','도실']
'''statList=['득점', '안타',
            '2타','3타', '홈런', '루타',
            '타점','도루', '도실','볼넷',
            '사구', '고4','삼진', '병살',
            '희타', '희비', '타율', '출루',
            '장타', 'OPS', '투구', 'avLI',
            'RE24', 'WPA']
'''

list_year = ['2018','2019','2020']

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

        '''
        pivot_hitting = df.pivot_table(values=hitting_statList,
                                index ='단계',
                                aggfunc='mean')



        pivot_hitting.plot.bar()
        plt.title(year+'년 '+name+' 불쾌지수 단계와 타격')
        plt.xlabel('불쾌지수')
        plt.ylabel('개(평균)')
        plt.show()

        pivot_seeing = df.pivot_table( values=seeing_statList,
                                index ='단계',
                                aggfunc='mean')

        pivot_seeing.plot.bar()
        plt.title(year+'년 '+name+' 불쾌지수 단계와 선구안')
        plt.xlabel('불쾌지수')
        plt.ylabel('개(평균)')
        plt.show()

        pivot_percent = df.pivot_table( values=percent_statList,
                                index ='단계',
                                aggfunc='mean')

        pivot_percent.plot.bar()
        plt.title(year+'년 '+name+' 불쾌지수 단계와 타격 지표')
        plt.xlabel('불쾌지수')
        plt.ylabel('%(평균)')
        plt.show()
        '''
        pivot_steal = df.pivot_table(values=steal_statList,
                                index ='단계',
                                aggfunc='mean')



        pivot_steal.plot.bar()
        plt.title(year+'년 '+name+' 불쾌지수 단계와 도루')
        plt.xlabel('불쾌지수')
        plt.ylabel('개(평균)')
        plt.show()

