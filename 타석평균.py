from bs4 import BeautifulSoup
from selenium import webdriver
import time

# 드라이버 가져오기
driver = webdriver.Chrome('C://Users//gkfka//Downloads//chromedriver_win32//chromedriver.exe')

# 연도 리스트
list_year=['2018', '2019', '2020']

# 페이지 리스트
list_page = ['1', '2', '3']

# 검색결과 담을 리스트
searchList = []


for year in list_year:

    sumResult = 0
    count = 0

    for page in list_page:
        # 사이트 열기
        url = driver.get('http://www.kbreport.com/leader/main?rows=100&order=oWAR&orderType=DESC&teamId=&defense_no=&year_from='+year+'&year_to='+year+'&gameType=R&split01=day&split02_1='+year+'-06-01&split02_2='+year+'-09-30&r_tpa_count=&tpa_count=0#/'+page)
        
        # 로딩까지 시간이 걸리므로 10초 정도는 기다려야 함
        time.sleep(5)
        
        
        # 리스트 값 선택
        driver.find_element_by_xpath("//select[@class='page-row-num']/option[@value='100']").click()

        # 로딩까지 시간이 걸리므로 10초 정도는 기다려야 함
        time.sleep(5)

        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        tblSchedule = soup.find('table', {'class': 'ltb-table responsive'})
        trs = tblSchedule.find_all('tr')
        for idx,tr in enumerate(trs):
            if idx > 0:
                tds = tr.find_all('td')
                print(tds[0].text.strip(), tds[4].text.strip())
                sumResult += int(tds[4].text.strip())
                count += 1

    average=sumResult/count
    temp = [year, sumResult, count,average]
    searchList.append(temp)


print(searchList)