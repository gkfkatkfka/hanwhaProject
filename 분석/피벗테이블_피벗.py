# 년도별 승패 비율 피에차트
# 불쾌지수 단계와 승패 피벗테이블
# 불쾌지수 단계와 승패 피벗테이블 피에차트

import pandas as pd
import matplotlib.pyplot as plt

# 한글 폰트 사용을 위해서 세팅
from matplotlib import font_manager, rc
font_path = "C:/Windows/Fonts/NANUMGOTHIC.TTF"
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)

year_list=['2018','2019','2020']

for year in year_list:
    '''피벗테이블 시각화'''
    # 파일 불러오기
    df = pd.read_csv('..\\dataSet\\'+year+'불쾌지수_승패.csv', encoding='UTF-8')

    '''년도별 승패 비율 피에 차트'''
    df["승패여부"].value_counts().plot.pie(explode=[0, 0.1], autopct='%1.1f%%', shadow=True)
    plt.title(year + '년 승패')
    plt.show()

    pivot = df.pivot_table(index='단계',
                       columns='승패여부',
                       aggfunc='count')

    print(pivot)

    pivot.plot.bar()
    plt.title('불쾌지수 단계와 승패')
    plt.xlabel('불쾌지수 단계')
    plt.ylabel('승패(개수)')
    plt.show()


    '''단계별 불쾌지수 파이차트'''
    #각 영역 이름 설정
    labels = 'win', 'lose'


    sizes_1 = [len(df.loc[(df["단계"] == 1) & (df["승패여부"] == 1)]),
               len(df.loc[(df["단계"] == 1) & (df["승패여부"] == 0)])]

    sizes_2 = [len(df.loc[(df["단계"] == 2) & (df["승패여부"] == 1)]),
               len(df.loc[(df["단계"] == 2) & (df["승패여부"] == 0)])]

    sizes_3 = [len(df.loc[(df["단계"] == 3) & (df["승패여부"] == 1)]),
               len(df.loc[(df["단계"] == 3) & (df["승패여부"] == 0)])]

    sizes_4 = [len(df.loc[(df["단계"] == 4) & (df["승패여부"] == 1)]),
               len(df.loc[(df["단계"] == 4) & (df["승패여부"] == 0)])]

    explode = (0, 0.1)

    fig = plt.figure()
    fig.set_size_inches(15, 5)
    ax1 = fig.add_subplot(1, 4, 1)
    ax2 = fig.add_subplot(1, 4, 2)
    ax3 = fig.add_subplot(1, 4, 3)
    ax4 = fig.add_subplot(1, 4, 4)

    ax1.pie(sizes_1, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
    ax1.set_title('낮음')  # Equal aspect ratio ensures that pie is drawn as a circle.

    ax2.pie(sizes_2, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
    ax2.set_title('보통')  # Equal aspect ratio ensures that pie is drawn as a circle.

    ax3.pie(sizes_3, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
    ax3.set_title('높음')  # Equal aspect ratio ensures that pie is drawn as a circle.

    ax4.pie(sizes_4, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
    ax4.set_title('매우 높음')  # Equal aspect ratio ensures that pie is drawn as a circle.

    plt.show()