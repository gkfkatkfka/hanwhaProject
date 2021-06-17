# 안타(1루타), 2루(2루타), 3루(3루타), 홈런
import csv
from matplotlib import pyplot as plt
import pandas as pd

x=[1,2,3]

years=['2018', '2019', '2020']

for year in years:
    # 선수 이름 파일 선택
    f = open('../dataSet/' + year + '한화선수명단.csv', 'r', encoding='UTF-8')

    # csv 파일 하나를 읽어옴
    information = csv.reader(f)

    # 헤더 데이터 패스!
    header = next(information)

    for info in information:
        name = info[1]

        # 선수 명단 가지고 오기
        df = pd.read_csv('../dataSet/' + year + '선수정보_단계변경/' + name + '.csv', encoding='UTF-8')

        # 불쾌지수별 정보를 담을 배열
        # 첫번째는 불쾌1, 두번재는 불쾌2, 세번째는 불쾌3
        arrFirst=[] # 안타
        arrSecond=[] # 2루타
        arrThird=[]# 3루타
        arrFourth=[] #홈런

        # 선수 명단 가지고 오기
        df = pd.read_csv('../dataSet/' + year + '선수정보_단계변경/' + name + '.csv', encoding='UTF-8')

        countFirst = len(df[df['단계'] == 1])
        countSecond = len(df[df['단계'] == 2])
        countThird = len(df[df['단계'] == 3])

        arrFirst.append(df[df['단계'] == 1]['타율'].sum()/countFirst)
        arrFirst.append(df[df['단계'] == 2]['타율'].sum() / countSecond)
        arrFirst.append(df[df['단계'] == 3]['타율'].sum() / countThird)

        arrSecond.append(df[df['단계'] == 1]['출루'].sum() / countFirst)
        arrSecond.append(df[df['단계'] == 2]['출루'].sum() / countSecond)
        arrSecond.append(df[df['단계'] == 3]['출루'].sum() / countThird)

        arrThird.append(df[df['단계'] == 1]['장타'].sum() / countFirst)
        arrThird.append(df[df['단계'] == 2]['장타'].sum() / countSecond)
        arrThird.append(df[df['단계'] == 3]['장타'].sum() / countThird)

        arrFourth.append(df[df['단계'] == 1]['OPS'].sum() / countFirst)
        arrFourth.append(df[df['단계'] == 2]['OPS'].sum() / countSecond)
        arrFourth.append(df[df['단계'] == 3]['OPS'].sum() / countThird)

        '''
        print(year,name)
        print(arrFirst)
        print(arrSecond)
        print(arrThird)
        print(arrFourth)
        
        plt.rc('font', family='Malgun Gothic')
        plt.title(year+'년 '+name+' 선수의 퍼센트')

        plt.plot(x,arrFirst,color='r',linestyle='--',label='안타',marker='o')
        plt.plot(x,arrSecond, color='g', linestyle='--', label='출루',marker='o')
        plt.plot(x,arrThird, color='b', linestyle='--', label='장타',marker='o')

        plt.bar(x,arrFourth,width=0.2)

        plt.xticks(x)
        plt.legend(loc=1)
        plt.show()
        '''

        plt.rc('font', family='Malgun Gothic')

        fig, ax1 = plt.subplots()

        plt.title(year+'년 '+name+' 기록')

        ax1.bar(x, arrFourth,width=0.3,alpha=0.6,color='slategrey',label='OPS')
        ax1.legend(loc=2)

        ax2 = ax1.twinx()
        ax2.plot(x,arrFirst,color='indianred',linestyle='--',label='안타',marker='o')
        ax2.plot(x,arrSecond, color='olive', linestyle='--', label='출루',marker='o')
        ax2.plot(x,arrThird, color='steelblue', linestyle='--', label='장타',marker='o')

        ax2.legend(loc=1)
        plt.savefig('C:/Users/gkfka/Documents/college/3_1/4_스타트업/최종결과./5_' + year + '년 ' + name + '기록 .png')
        plt.show()