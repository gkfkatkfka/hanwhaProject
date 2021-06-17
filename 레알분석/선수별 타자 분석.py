# 안타(1루타), 2루(2루타), 3루(3루타), 홈런
import csv
import matplotlib.pyplot as plt
from matplotlib import pyplot as plt
import numpy as np
# 년도
import pandas as pd

x=[1,2,3,4]
y=[0,0.5,1,1.5]


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
        # 첫번째는 불쾌1, 두번재는 불쾌2, 세번째는 부로캐3
        arrFirst=[] # 안타
        arrSecond=[] # 2루타
        arrThird=[]# 3루타
        arrFourth=[] #홈런

        # 선수 명단 가지고 오기
        df = pd.read_csv('../dataSet/' + year + '선수정보_단계변경/' + name + '.csv', encoding='UTF-8')
        countFirst = len(df[df['단계'] == 1])
        countSecond = len(df[df['단계'] == 2])
        countThird = len(df[df['단계'] == 3])

        arrFirst.append(df[df['단계'] == 1]['안타'].sum()/countFirst)
        arrFirst.append(df[df['단계'] == 2]['안타'].sum() / countSecond)
        arrFirst.append(df[df['단계'] == 3]['안타'].sum() / countThird)

        arrSecond.append(df[df['단계'] == 1]['2타'].sum() / countFirst)
        arrSecond.append(df[df['단계'] == 2]['2타'].sum() / countSecond)
        arrSecond.append(df[df['단계'] == 3]['2타'].sum() / countThird)

        arrThird.append(df[df['단계'] == 1]['3타'].sum() / countFirst)
        arrThird.append(df[df['단계'] == 2]['3타'].sum() / countSecond)
        arrThird.append(df[df['단계'] == 3]['3타'].sum() / countThird)

        arrFourth.append(df[df['단계'] == 1]['홈런'].sum() / countFirst)
        arrFourth.append(df[df['단계'] == 2]['홈런'].sum() / countSecond)
        arrFourth.append(df[df['단계'] == 3]['홈런'].sum() / countThird)

        color = ['lightcoral', 'orange', 'yellowgreen', 'skyblue']

        plt.rc('font', family='Malgun Gothic')
        legends=['안타','2루타','3루타','홈런']
        topics = ['중간', '높음', '매우 높음']

        c_bottom = np.add(arrFirst, arrSecond)
        d_bottom = np.add(c_bottom, arrThird)
        f_bottom = np.add(d_bottom, arrFourth)
        x = range(len(topics))
        plt.bar(x, arrFirst, width=0.4)
        plt.bar(x, arrSecond, bottom=arrFirst, width=0.4)
        plt.bar(x, arrThird, bottom=c_bottom, width=0.4)
        plt.bar(x, arrFourth, bottom=d_bottom, width=0.4)

        ax = plt.subplot()
        ax.set_xticks(x)
        ax.set_yticks(y)
        ax.set_xticklabels(topics)
        plt.title(year+'년 '+name+' 선수의 안타')
        plt.xlabel('불쾌지수 단계')
        plt.ylabel('개(평균)')
        plt.legend(legends,loc=1)
        plt.savefig('C:/Users/gkfka/Documents/college/3_1/4_스타트업/최종결과./3_' + year + '년 '+name+'의 안타.png')
        plt.show()






