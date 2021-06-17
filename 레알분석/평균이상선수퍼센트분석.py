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
# 첫번째는 불쾌1, 두번재는 불쾌2, 세번째는 부로캐3
arrFirst = []  # 안타
arrSecond = []  # 2루타
arrThird = []  # 3루타
arrFourth = []  # 홈런

# 선수 명단 가지고 오기

countFirst = len(df_result[df_result['단계'] == 1])
countSecond = len(df_result[df_result['단계'] == 2])
countThird = len(df_result[df_result['단계'] == 3])

arrFirst.append(df_result[df_result['단계'] == 1]['타율'].sum() / countFirst)
arrFirst.append(df_result[df_result['단계'] == 2]['타율'].sum() / countSecond)
arrFirst.append(df_result[df_result['단계'] == 3]['타율'].sum() / countThird)

arrSecond.append(df_result[df_result['단계'] == 1]['출루'].sum() / countFirst)
arrSecond.append(df_result[df_result['단계'] == 2]['출루'].sum() / countSecond)
arrSecond.append(df_result[df_result['단계'] == 3]['출루'].sum() / countThird)

arrThird.append(df_result[df_result['단계'] == 1]['장타'].sum() / countFirst)
arrThird.append(df_result[df_result['단계'] == 2]['장타'].sum() / countSecond)
arrThird.append(df_result[df_result['단계'] == 3]['장타'].sum() / countThird)

arrFourth.append(df_result[df_result['단계'] == 1]['OPS'].sum() / countFirst)
arrFourth.append(df_result[df_result['단계'] == 2]['OPS'].sum() / countSecond)
arrFourth.append(df_result[df_result['단계'] == 3]['OPS'].sum() / countThird)

plt.rc('font', family='Malgun Gothic')

fig, ax1 = plt.subplots()

plt.title('한화 이글스 타자 기록')

ax1.bar(x, arrFourth, width=0.3, alpha=0.6, color='slategrey',label='OPS')
ax1.legend(loc=9)

ax2 = ax1.twinx()
ax2.plot(x, arrFirst, color='indianred', linestyle='--', label='안타', marker='o')
ax2.plot(x, arrSecond, color='olive', linestyle='--', label='출루', marker='o')
ax2.plot(x, arrThird, color='steelblue', linestyle='--', label='장타', marker='o')

plt.legend(loc=1)
plt.savefig('C:/Users/gkfka/Documents/college/3_1/4_스타트업/최종결과./8_한화 이글스 기록.png')
plt.show()
