# 안타(1루타), 2루(2루타), 3루(3루타), 홈런
import csv
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

years=['2018', '2019', '2020']
count=0
df_result= pd.read_csv('../dataSet/2018선수정보_단계변경/최재훈.csv', encoding='UTF-8')

x=[1,2,3]
y=[0,0.5,1]

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

arrFirst.append(df_result[df_result['단계'] == 1]['안타'].sum() / countFirst)
arrFirst.append(df_result[df_result['단계'] == 2]['안타'].sum() / countSecond)
arrFirst.append(df_result[df_result['단계'] == 3]['안타'].sum() / countThird)

arrSecond.append(df_result[df_result['단계'] == 1]['2타'].sum() / countFirst)
arrSecond.append(df_result[df_result['단계'] == 2]['2타'].sum() / countSecond)
arrSecond.append(df_result[df_result['단계'] == 3]['2타'].sum() / countThird)

arrThird.append(df_result[df_result['단계'] == 1]['3타'].sum() / countFirst)
arrThird.append(df_result[df_result['단계'] == 2]['3타'].sum() / countSecond)
arrThird.append(df_result[df_result['단계'] == 3]['3타'].sum() / countThird)

arrFourth.append(df_result[df_result['단계'] == 1]['홈런'].sum() / countFirst)
arrFourth.append(df_result[df_result['단계'] == 2]['홈런'].sum() / countSecond)
arrFourth.append(df_result[df_result['단계'] == 3]['홈런'].sum() / countThird)

color = ['lightcoral', 'orange', 'yellowgreen', 'skyblue']

plt.rc('font', family='Malgun Gothic')
legends = ['안타', '2루타', '3루타', '홈런']
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
plt.title('한화 이글스 선수 안타 기록')
plt.xlabel('불쾌지수 단계')
plt.ylabel('개(평균)')
plt.legend(legends, loc=9,ncol=2)
plt.savefig('C:/Users/gkfka/Documents/college/3_1/4_스타트업/최종결과./6_한화 이글스 안타 .png')
plt.show()

