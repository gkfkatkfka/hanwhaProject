import csv
import matplotlib.pyplot as plt

# 전체 불쾌지수별 담을 리스트 초기화
total_first=[]
total_second=[]
total_third=[]


# 3년의 불쾌지수 별 승 더할 변수 초기화하기
tFirstWin = 0
tFirstLose = 0
tSecondWin = 0
tSecondLose = 0
tThirdWin = 0
tThirdLose = 0


# 년도
years=['2018','2019','2020']

for year in years:
    # 년도별 기록을 담을 리스트 초기화
    year_first = []
    year_second = []
    year_third = []


    # 승패 담을 변수 초기화
    firstWin=0
    firstLose=0
    secondWin = 0
    secondLose = 0
    thirdWin = 0
    thirdLose = 0


    f = open('../dataSet/' + year + '불쾌지수_승패_단계변경.csv', encoding='UTF8')
    data = csv.reader(f)

    # 데이터 줄별로 읽기
    for row in data:
        # 불쾌지수별 승패 모으기
        if '1' in row[1]:
            if '1' in row[2]:
                firstWin +=1
                tFirstWin +=1
            else:
                firstLose +=1
                tFirstLose +=1
        elif '2' in row[1]:
            if '1' in row[2]:
                secondWin +=1
                tSecondWin +=1
            else:
                secondLose +=1
                tSecondLose +=1
        elif '3' in row[1]:
            if '1' in row[2]:
                thirdWin +=1
                tThirdWin +=1
            else:
                thirdLose +=1
                tThirdLose +=1

    year_first.append(firstWin)
    year_first.append(firstLose)
    year_second.append(secondWin)
    year_second.append(secondLose)
    year_third.append(thirdWin)
    year_third.append(thirdLose)


    plt.rc('font', family='Malgun Gothic')

    fig = plt.figure()
    fig.set_size_inches(15, 5)
    ax1 = fig.add_subplot(1, 3, 1)
    ax2 = fig.add_subplot(1, 3, 2)
    ax3 = fig.add_subplot(1, 3, 3)

    color=['lightcoral','powderblue']

    ax1.pie(year_first, labels=['승리','패배'], autopct='%.f%%', colors=color, startangle=90,shadow=True)
    ax1.set_title('보통')

    ax2.pie(year_second, labels=['승리', '패배'], autopct='%.f%%', colors=color, startangle=90,shadow=True)
    ax2.set_title('높음')

    ax3.pie(year_third, labels=['승리', '패배'], autopct='%.f%%', colors=color, startangle=90,shadow=True)
    ax3.set_title('매우 높음')

    plt.show()
