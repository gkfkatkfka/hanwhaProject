# 년도별 분석
# 2018~2020년 승패 분석

# 알고리즘
# 년도별로 리스트 생성
# 동시에 3년간의 데이터를 담는 리스트 만들기

import csv
import matplotlib.pyplot as plt

# 전체 년도 기록을 담을 리스트
total_record=[]

# 3년의 불쾌지수 별 승 더할 변수 초기화하기
tFirst = 0
tSecond = 0
tThird = 0

# 년도
years=['2018','2019','2020']

for year in years:
    # 년도별 기록을 담을 리스트 초기화
    year_record = []

    # 불쾌지수별 승 더할 변수 초기화하기
    first = 0
    second = 0
    third = 0

    f= open('../dataSet/' + year + '불쾌지수_승패_단계변경.csv',encoding='UTF8')
    data=csv.reader(f)


    # 데이터 줄별로 읽기
    for row in data:
        # 이긴 경우 보기
        if '1' in row[2]:
            if '1' in row[1]:
                first += 1
                tFirst += 1
            elif '2' in row[1]:
                second += 1
                tSecond += 1
            elif '3' in row[1]:
                third += 1
                tThird += 1


    # 년도별 리스트에 불쾌지수 단계별 승 추가하기
    year_record.append(first)
    year_record.append(second)
    year_record.append(third)



    plt.rc('font', family='Malgun Gothic')
    color=['lightcoral', 'orange', 'yellowgreen', 'skyblue']
    plt.axis('equal')

    plt.pie(year_record,labels=['중간', '높음', '매우높음'],autopct='%.f%%',colors=color,startangle=90)
    plt.legend(loc=3)
    plt.title(year+' 불쾌지수 별 승리')
    plt.savefig('C:/Users/gkfka/Documents/college/3_1/4_스타트업/최종결과./1_' + year + '불쾌지수 별 승리.png')
    plt.show()



total_record.append(tFirst)
total_record.append(tSecond)
total_record.append(tThird)

plt.rc('font', family='Malgun Gothic')
color=['lightcoral', 'orange', 'yellowgreen', 'skyblue']
plt.axis('equal')

plt.pie(total_record,labels=['중간', '높음', '매우 높음'],autopct='%.f%%',colors=color,startangle=90)
plt.legend(loc=3)
plt.title('2018년 - 2020년 불쾌지수 별 승리')
plt.savefig('C:/Users/gkfka/Documents/college/3_1/4_스타트업/최종결과./1_2018-2020년 불쾌지수 별 승리.png')
plt.show()