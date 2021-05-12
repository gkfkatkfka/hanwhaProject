from bs4 import BeautifulSoup
from selenium import webdriver
import time
import pandas as pd

# 드라이버 가져오기
driver = webdriver.Chrome('C://Users//gkfka//Downloads//chromedriver_win32//chromedriver.exe')

# 연도 리스트
list_year=['2018', '2019', '2020']
list_average=[127,142,138]


for year in list_year:
    
    # 리스트 초기화
    searchList = []
    
    # 사이트 열기
    url = driver.get('http://www.kbreport.com/leader/main?rows=20&order=oWAR&orderType=DESC&teamId=8&defense_no=&year_from='+year+'&year_to='+year+'&gameType=R&split01=month&split02_1=6&split02_2=9&r_tpa_count=&tpa_count=0#/1')

    # 사이트 로딩 시간 고려
    time.sleep(7)

    # 리스트 값 선택
    driver.find_element_by_xpath("//select[@class='page-row-num']/option[@value='50']").click()

    # 사이트 로딩 시간 고려
    time.sleep(10)

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    tblSchedule = soup.find('table', {'class': 'ltb-table responsive'})
    trs = tblSchedule.find_all('tr')

    for average in list_average:
        for idx,tr in enumerate(trs):
            if idx > 0:
                tds = tr.find_all('td')
                if int(tds[4].text.strip())>average:
                    temp=[tds[1].text.strip(),tds[4].text.strip()]
                    searchList.append(temp)

    # csv 만들기
    data = pd.DataFrame(searchList)
    data.columns = ['이름','타석']
    data.head()
    data.to_csv(year + '한화선수명단.csv', encoding='UTF-8')
