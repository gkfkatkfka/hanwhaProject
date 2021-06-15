# 안타(1루타), 2루(2루타), 3루(3루타), 홈런
import csv
import matplotlib.pyplot as plt
from matplotlib import pyplot as plt
import numpy as np
# 년도
import pandas as pd

x=[1,2,3,4]
y=[1,2,3,4]


years=['2018','2019','2020']

for year in years:
    # 선수 이름 파일 선택
    f = open('../dataSet/' + year + '한화선수명단.csv', 'r', encoding='UTF-8')

    # csv 파일 하나를 읽어옴
    information = csv.reader(f)

    # 헤더 데이터 패스!
    header = next(information)

    for info in information:
        name = info[1]


        # 불쾌지수별 정보를 담을 배열
        # 안타(1루타),2타(2루타),3타(3루타), 홈런 순으로 들어감
        arrFirst=[]
        arrSecond=[]
        arrThird=[]
        arrFourth=[]

        # 선수 명단 가지고 오기
        df = pd.read_csv('../dataSet/' + year + '선수정보_불쾌지수_단계변경/' + name + '.csv', encoding='UTF-8')
        countFirst = len(df[df['단계'] == 1])
        countSecond = len(df[df['단계'] == 2])
        countThird = len(df[df['단계'] == 3])
        countFourth = len(df[df['단계'] == 4])

        sumFirst=0
        sumSecond=0
        sumThird=0
        sumFourth=0

        if countFirst==0:
            arrFirst.append(0)
            arrFirst.append(0)
            arrFirst.append(0)
            arrFirst.append(0)
        else:
            arrFirst.append(df[df['단계']==1]['안타'].sum()/countFirst)
            arrFirst.append(df[df['단계'] == 1]['2타'].sum() / countFirst)
            arrFirst.append(df[df['단계'] == 1]['3타'].sum() / countFirst)
            arrFirst.append(df[df['단계'] == 1]['홈런'].sum() / countFirst)

        arrSecond.append(df[df['단계'] == 2]['안타'].sum() / countSecond)
        arrSecond.append(df[df['단계'] == 2]['2타'].sum() / countSecond)
        arrSecond.append(df[df['단계'] == 2]['3타'].sum() / countSecond)
        arrSecond.append(df[df['단계'] == 2]['홈런'].sum() / countSecond)

        arrThird.append(df[df['단계'] == 3]['안타'].sum() / countThird)
        arrThird.append(df[df['단계'] == 3]['2타'].sum() / countThird)
        arrThird.append(df[df['단계'] == 3]['3타'].sum() / countThird)
        arrThird.append(df[df['단계'] == 3]['홈런'].sum() / countThird)

        arrFourth.append(df[df['단계'] == 4]['안타'].sum() / countFourth)
        arrFourth.append(df[df['단계'] == 4]['2타'].sum() / countFourth)
        arrFourth.append(df[df['단계'] == 4]['3타'].sum() / countFourth)
        arrFourth.append(df[df['단계'] == 4]['홈런'].sum() / countFourth)

        '''
        print(name,year)
        print(arrFirst)
        print(arrSecond)
        print(arrThird)
        print(arrFourth)
        '''

        topics = ['one', 'two', 'three', 'four']
        As = [0, 0, 0, 0] #arrFirst
        Bs = [0.4642857142857143, 0.0, 0.0, 0.0] #arrSecond
        Cs = [0.4, 0.0, 0.0, 0.03333333333333333] #arrThird
        Ds = [0.42857142857142855, 0.14285714285714285, 0.0, 0.0] #arrFourth

        c_bottom = np.add(As, Bs)
        d_bottom = np.add(c_bottom, Cs)

        x = range(len(topics))
        plt.bar(x, As)
        plt.bar(x, Bs, bottom=As)
        plt.bar(x, Cs, bottom=c_bottom)
        plt.bar(x, Ds, bottom=d_bottom)

        ax = plt.subplot()
        ax.set_xticks(x)
        ax.set_xticklabels(topics)
        plt.title('TITLE')
        plt.xlabel('X LABEL')
        plt.ylabel('Y LABEL')
        plt.show()

        '''
        legends=['1루타','2루타','3루타','홈런']
        topics = ['낮음', '중간', '높음', '매우 높음']

        c_bottom = np.add(arrFirst, arrSecond)
        d_bottom = np.add(c_bottom, arrThird)
        x = range(len(topics))

        plt.rc('font', family='Malgun Gothic')

        plt.bar(x, arrFirst)
        plt.bar(x, arrSecond, bottom=arrFirst)
        plt.bar(x, arrThird, bottom=c_bottom)
        plt.bar(x, arrFourth, bottom=d_bottom)

        ax = plt.subplot()
        ax.set_xticks(x)
        ax.set_xticklabels(topics)


        plt.title(year+'년 '+name+'의 안타 지수')
        plt.xlabel('불쾌지수 단계')
        plt.ylabel('개(평균)')
        plt.legend(legends)
        plt.show()
        '''





