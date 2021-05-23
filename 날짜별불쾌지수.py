import csv
import pandas as pd

# 년도 리스트
year_list = ['2018', '2019', '2020']

for year in year_list:

    searchList = []

    # 파일 선택
    f = open('./dataSet/' + year + '날짜별불쾌지수.csv', 'r', encoding='UTF-8')

    # csv 파일 하나를 읽어옴
    information = csv.reader(f)

    # 헤더 데이터 안 읽어오기
    header = next(information)

    # 정보 한 줄씩 불러오기
    for info in information:
        date=info[1]
        dateIndex=int(info[3])

        # 0 : 낮음, 1: 보통, 2: 높음, 3: 매우높음
        if dateIndex>=80:
            temp=[date,dateIndex,4]
        elif dateIndex >=75:
            temp = [date, dateIndex, 3]
        elif dateIndex >= 68:
            temp = [date, dateIndex, 2]
        else:
            temp = [date, dateIndex, 1]

        searchList.append(temp)

        # csv 만들기
        data = pd.DataFrame(searchList)
        data.columns = ['날짜','불쾌지수','단계']
        data.head()
        data.to_csv(year + '최종불쾌지수.csv', encoding='UTF-8')
