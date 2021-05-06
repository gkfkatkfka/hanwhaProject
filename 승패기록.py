import re
import csv
import pandas as pd

# 한글, 영어만 추출하는 정규식 => 팀명 추출할 때 사용
string = re.compile('[^ 가-힣 a-z A-Z]+')

# 년도 리스트
year_list=['2018','2019','2020']


for year in year_list:

    searchList = []

    #파일 선택
    f = open('./dataSet/'+year+'모든경기정보.csv', 'r', encoding='UTF-8')

    # csv 파일 하나를 읽어옴
    information = csv.reader(f)
    
    # 헤더 데이터 안 읽어오기
    header=next(information)

    # 정보 한 줄씩 불러오기
    for info in information:
        strData=info[4]
        
        # vs로 일차적으로 문자열 분할
        strList=strData.split('vs')

        # 숫자만 추출
        firstScore=int(re.findall('\d+', strList[0])[0])
        secondScore=int(re.findall('\d+', strList[1])[0])

        # 팀만 추출
        firstTeam=string.sub('', strList[0])
        secondTeam=string.sub('', strList[1])

        # 0:패배 , 1: 승리
        if firstScore>secondScore and firstTeam=="한화":
            temp=[info[2][0:5],firstTeam,firstScore,secondTeam,secondScore,1]
        elif firstScore<secondScore and secondTeam=="한화":
            temp=[info[2][0:5],firstTeam,firstScore,secondTeam,secondScore,1]
        else:
            temp=[info[2][0:5],firstTeam,firstScore,secondTeam,secondScore,0]

        searchList.append(temp)

        # csv 만들기
        data = pd.DataFrame(searchList)
        data.columns = ['날짜', '팀1', '팀1 점수','팀2', '팀2 점수', '승패여부']
        data.head()
        data.to_csv(year + '승패기록.csv', encoding='UTF-8')

