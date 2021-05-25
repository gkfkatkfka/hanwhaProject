from bs4 import BeautifulSoup
from selenium import webdriver
import csv
import pandas as pd


# 드라이버 가져오기
driver = webdriver.Chrome('C://Users//gkfka//Downloads//chromedriver_win32//chromedriver.exe')

# 연도 리스트
list_year = ['2018', '2019', '2020']

for year in list_year:



    # 선수 이름 파일 선택
    f = open('./dataSet/' + year + '한화선수명단.csv', 'r', encoding='UTF-8')

    # csv 파일 하나를 읽어옴
    information = csv.reader(f)

    # 헤더 데이터 패스!
    header = next(information)

    for info in information:
        name = info[1]

        # 선수들 이름 담을 리스트
        searchList = []

        if len(info)==3:
            # 사이트 열기
            url = driver.get('http://www.statiz.co.kr/player.php?opt=3&sopt=0&name='+name+'&re=0&se=&da=&year='+year+'&cv=')
        else:
            url = driver.get('http://www.statiz.co.kr/player.php?opt=3&sopt=0&name=' + name + '&re=0&birth='+info[3]+'&se=&da=&year=' + year + '&cv=')


        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        tblSchedule = soup.find('table', {'style': 'font-size:;'})
        tbody = tblSchedule.find('tbody')
        trs = tbody.find_all('tr')


        for idx, tr in enumerate(trs):
            if idx>0:
                tds = tr.find_all('td')
                if len(tds) == 31:
                    if int(tds[0].text.strip()[0:2])>=6 and int(tds[0].text.strip()[0:2])<=9:
                        temp = [year+"-"+tds[0].text.strip(),tds[6].text.strip(), tds[7].text.strip(), tds[8].text.strip(),
                            tds[9].text.strip(), tds[10].text.strip(), tds[11].text.strip(), tds[12].text.strip(),
                            tds[13].text.strip(), tds[14].text.strip(), tds[15].text.strip(), tds[16].text.strip(),
                            tds[17].text.strip(),tds[18].text.strip(), tds[19].text.strip(), tds[20].text.strip(),
                            tds[21].text.strip(),tds[22].text.strip(), tds[23].text.strip(), tds[24].text.strip(),
                            tds[25].text.strip(),tds[26].text.strip(), tds[27].text.strip(), tds[28].text.strip(),
                            tds[29].text.strip(), tds[30].text.strip()]
                        print(temp)
                        searchList.append(temp)

        # csv 만들기
        data = pd.DataFrame(searchList)
        data.columns = ['날짜', '타수', '득점', '안타',
                        '2타','3타', '홈런', '루타',
                        '타점','도루', '도실','볼넷',
                        '사구', '고4','삼진', '병살',
                        '희타', '희비', '타율', '출루',
                        '장타', 'OPS', '투구', 'avLI',
                        'RE24', 'WPA']
        data.head()
        data.to_csv('./dataSet/'+year+'선수정보수집/' + name + '선수정보.csv', encoding='UTF-8',index=False)