# 종속변수 : 여러가지 타자 스탯들
# 독립변수 : 불쾌지수
# 각 단순 스탯들과 불쾌지수 간의 인과관계 파악을 위해 작성
import csv
import pandas as pd
import seaborn as sns

# 한글 폰트 사용을 위해서 세팅
from matplotlib import font_manager, rc
font_path = "C:/Windows/Fonts/NANUMGOTHIC.TTF"
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)

# 연도 리스트
from matplotlib import pyplot as plt

list_year = ['2018', '2019', '2020']

for year in list_year:
    # 선수 이름 파일 선택
    f = open('../dataSet/' + year + '한화선수명단.csv', 'r', encoding='UTF-8')

    # csv 파일 하나를 읽어옴
    information = csv.reader(f)

    # 헤더 데이터 패스!
    header = next(information)

    # 선수들 이름 담을 리스트
    searchList = []

    for info in information:
        name = info[1]

        # 선수 명단 가지고 오기
        df = pd.read_csv('../dataSet/' + year + '선수정보_불쾌지수/' + name + '.csv', encoding='UTF-8')


        pivot = df.pivot_table(values='타수',
                               index='단계',
                               aggfunc='mean')

        print(pivot)

        pivot.plot.bar()
        plt.title(name+'불쾌지수 단계와 타수')
        plt.xlabel('불쾌지수')
        plt.ylabel('타수(평균/개)')
        plt.show()


