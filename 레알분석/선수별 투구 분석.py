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
        arrFirst=[] # 투구
        arrSecond=[] # 볼넷
        arrThird=[] # 삼진

        # 선수 명단 가지고 오기
        df = pd.read_csv('../dataSet/' + year + '선수정보_단계변경/' + name + '.csv', encoding='UTF-8')

        countFirst = len(df[df['단계'] == 1])
        countSecond = len(df[df['단계'] == 2])
        countThird = len(df[df['단계'] == 3])

        arrFirst.append(df[df['단계'] == 1]['투구'].sum()  /df[df['단계'] == 1]['타수'].sum())
        arrFirst.append(df[df['단계'] == 2]['투구'].sum() /df[df['단계'] == 1]['타수'].sum())
        arrFirst.append(df[df['단계'] == 3]['투구'].sum() /df[df['단계'] == 1]['타수'].sum())

        arrSecond.append(df[df['단계'] == 1]['볼넷'].sum() / countFirst)
        arrSecond.append(df[df['단계'] == 2]['볼넷'].sum() / countSecond)
        arrSecond.append(df[df['단계'] == 3]['볼넷'].sum() / countThird)

        arrThird.append(df[df['단계'] == 1]['삼진'].sum() / countFirst)
        arrThird.append(df[df['단계'] == 2]['삼진'].sum() / countSecond)
        arrThird.append(df[df['단계'] == 3]['삼진'].sum() / countThird)

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
        '''
        legens=['삼진','볼넷']
        plt.rc('font', family='Malgun Gothic')

        fig, ax1 = plt.subplots()

        plt.title(year + '년 ' + name + ' 선수의 기록')

        ax1.bar(x, arrThird, width=0.3,color='indianred')
        ax1.bar(x, arrSecond, width=0.3, color='steelblue')

        ax2 = ax1.twinx()
        ax2.plot(x, arrFirst, color='dimgray', linestyle='--', label='투구', marker='o')

        plt.show()
        '''
        print(arrFirst)
        plt.rc('font', family='Malgun Gothic')
        fig, ax1 = plt.subplots()
        plt.title(year + '년 ' + name + ' 선수의 타격 기록')

        width = 0.3

        left_x_position = []
        for position in x:
            left_x_position.append(position - width / 2)

        right_x_position = []
        for position in x:
                right_x_position.append(position + width / 2)

        ax1.bar(left_x_position, arrSecond, width=width, alpha=0.7,color='darkorange',label='볼넷')
        ax1.bar(right_x_position, arrThird, width=width,alpha=0.7, color='steelblue',label='삼진')
        ax1.legend(loc=1)

        ax2 = ax1.twinx()
        ax2.plot(x, arrFirst, color='dimgray', linestyle='--', label='투구 수', marker='o')
        plt.legend(loc=2)
        plt.savefig('C:/Users/gkfka/Documents/college/3_1/4_스타트업/최종결과./4_' + year + '년 '+name+' 타격 기록 .png')
        plt.show()