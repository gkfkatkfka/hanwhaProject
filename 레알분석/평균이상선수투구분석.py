# 안타(1루타), 2루(2루타), 3루(3루타), 홈런
import csv
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

years=['2018', '2019', '2020']
count=0
df_result= pd.read_csv('../dataSet/2018선수정보_단계변경/최재훈.csv', encoding='UTF-8')

x=[1,2,3]

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
        if count==0:
            df_result= pd.read_csv('../dataSet/' + year + '선수정보_단계변경/' + name + '.csv', encoding='UTF-8')
            count+=1
            continue

        df_in = pd.read_csv('../dataSet/' + year + '선수정보_단계변경/' + name + '.csv', encoding='UTF-8')
        df_result=df_result.append(df_in)

'''뭔지 모르지만 일단 분석'''
# 불쾌지수별 정보를 담을 배열
# 첫번째는 불쾌1, 두번재는 불쾌2, 세번째는 불쾌3
arrFirst = []  # 투구
arrSecond = []  # 볼넷
arrThird = []  # 삼진

countFirst = len(df_result[df_result['단계'] == 1])
countSecond = len(df_result[df_result['단계'] == 2])
countThird = len(df_result[df_result['단계'] == 3])

arrFirst.append(df_result[df_result['단계'] == 1]['투구'].sum() / df_result[df_result['단계'] == 1]['타수'].sum() )
arrFirst.append(df_result[df_result['단계'] == 2]['투구'].sum() / df_result[df_result['단계'] == 1]['타수'].sum())
arrFirst.append(df_result[df_result['단계'] == 3]['투구'].sum() / df_result[df_result['단계'] == 1]['타수'].sum())

arrSecond.append(df_result[df_result['단계'] == 1]['볼넷'].sum() / countFirst)
arrSecond.append(df_result[df_result['단계'] == 2]['볼넷'].sum() / countSecond)
arrSecond.append(df_result[df_result['단계'] == 3]['볼넷'].sum() / countThird)

arrThird.append(df_result[df_result['단계'] == 1]['삼진'].sum() / countFirst)
arrThird.append(df_result[df_result['단계'] == 2]['삼진'].sum() / countSecond)
arrThird.append(df_result[df_result['단계'] == 3]['삼진'].sum() / countThird)
color = ['lightcoral', 'orange', 'yellowgreen', 'skyblue']

plt.rc('font', family='Malgun Gothic')
fig, ax1 = plt.subplots()
plt.title('한화 이글스 타자 타격 기록')

width = 0.3

left_x_position = []
for position in x:
    left_x_position.append(position - width / 2)

right_x_position = []
for position in x:
    right_x_position.append(position + width / 2)

ax1.bar(left_x_position, arrSecond, width=width, alpha=0.7, color='darkorange',label='볼넷')
ax1.bar(right_x_position, arrThird, width=width, alpha=0.7, color='steelblue',label='삼진')
ax1.legend(ncol=2,loc=9)

ax2 = ax1.twinx()
ax2.plot(x, arrFirst, color='dimgray', linestyle='--', label='투구', marker='o')
plt.savefig('C:/Users/gkfka/Documents/college/3_1/4_스타트업/최종결과./7_한화 이글스 타격 .png')
plt.legend()

plt.show()

