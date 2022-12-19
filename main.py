#%%
import requests as req
from bs4 import BeautifulSoup

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium import webdriver

import numpy as np
import pandas as pd
import time


# 크롬 창 열기
driver = webdriver.Chrome('./chromedriver.exe') 

# 인터파크 연령별 베스트셀러 창 열기
driver.get('https://mbook.interpark.com/shop/ranking/age') 

# 2초 쉬기
time.sleep(2)

df_au_pu_set=[]

for age in range(6):
    titles_df = []
    age_df = []
    
    # 연령 드롭박스 선택
    select_age = Select(driver.find_element(By.ID,'selectAge'))
    select_age.select_by_index(age)
   
    # 끝까지 스크롤바 다운해서 정의 
    last_height = driver.execute_script("return document.body.scrollHeight") 

    while True:
        #끝까지 스크롤 다운
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight)") 
        #대기
        time.sleep(1)
        #스크롤 다운 후 다시 가져오기
        new_height = driver.execute_script("return document.body.scrollHeight")
        
        #스크롤 다운해도 계속 그 위치면 브레이크함.
        if new_height == last_height: 
            time.sleep(1)
            break

        last_height = new_height 
        #결과적으로 끝까지 스크롤바 다운이 됐음
        
        
    # 그 페이지에서 html 가져오고, 그걸  정리해주고  soup1으로 지정    
    soup = BeautifulSoup(driver.page_source,'lxml') 

    # div태그들 중에서 class가 multiTxtEllipsis인것들 모두 찾아줘(베스트셀러 책 이름들)
    titles = soup.find_all("div",{'class':'multiTxtEllipsis'} ) 

    for i in titles:
        titles_df.append(i.get_text()) # 리스트에 베스트셀러 책 이름들을 모두 저장
        age_df.append('{0}대'.format((age+1)*10))

    
    col_name = ['연령','책제목']
    df_au_pu = pd.DataFrame(zip(age_df,titles_df), columns=col_name)
    df_au_pu_set.append(df_au_pu)



driver = webdriver.Chrome('./chromedriver.exe') 
driver.get('https://book.interpark.com/bookPark/html/book.html?smid1=header&smid2=book') 
time.sleep(2) 

df_info_set = []

driver.find_element(By.CLASS_NAME,'noToday').click()

book_all_list = [titles_df1,titles_df2,titles_df3,titles_df4,titles_df5,titles_df6]


for titles_df in book_all_list:

    author_df=[]
    publisher_df=[]
    class_df1 = []
    class_df2 = []
    class_df3 = [] 
 
    for name in titles_df:    

        search = driver.find_element(By.NAME,'query')
        search.click()
        search.clear()
        time.sleep(2)
        search.send_keys(name)
        time.sleep(2)
        search.send_keys(Keys.RETURN)
        driver.implicitly_wait(10)
        
        driver.find_element(By.LINK_TEXT,'판매량순').click()
        time.sleep(2)
        driver.find_element(By.CLASS_NAME,'bimgWrap').click()
        time.sleep(2)
        
        if len(driver.window_handles) == 1:
            driver.switch_to.window(driver.window_handles[0])
        else :
            driver.switch_to.window(driver.window_handles[1])
        
    

        last_height = driver.execute_script("return document.body.scrollHeight") 

        while True:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight)") 
            time.sleep(1)
            new_height = driver.execute_script("return document.body.scrollHeight")

            if new_height == last_height: 
                time.sleep(1)
                break

            last_height = new_height 
            
            time.sleep(2)

        soup = BeautifulSoup(driver.page_source,'lxml')

        # 작가, 출판사, 대중소분류 위치 찾아서 가져오기
        FIND_au_pu = soup.select('table#prdNoticeTable')
        FIND_class = soup.select('div.fiedCell')

        for i in FIND_au_pu:
            x =  i.text
            au_pu_df = x.split(' ')
            author = au_pu_df[2]
            publisher = au_pu_df[4]

        for i in FIND_class:
            y = i.text
            class_df = y.split('\n')
            class1 = class_df[4]
            class2 = class_df[5]
            class3 = class_df[6]

        #작가, 출판사, 대중소분류 리스트에 가져온 값들 넣기
        author_df.append(author)
        publisher_df.append(publisher)
        class_df1.append(class1)
        class_df2.append(class2)
        class_df3.append(class3)

        #값 가져왔으니 새로 열린 탭 닫기
        time.sleep(3)
        
        if len(driver.window_handles) == 1:
            driver.switch_to.window(driver.window_handles[0])
            driver.back()    
            driver.implicitly_wait(10)
        else :
            driver.switch_to.window(driver.window_handles[1])
            time.sleep(3)
            driver.close()
     


        # 원래 기본 탭에서 다시 뒤로가기 하고 새로운 검색 준비하기
        driver.switch_to.window(driver.window_handles[0])
        driver.back()    
        driver.implicitly_wait(10)

        # 책제목, 작가, 출판사, 대중소분류 리스트들 묶어서 데이터프레임 만들기
        col_name_info = ['책제목','작가','출판사','대분류','중분류','소분류']
        col_df = zip(titles_df,author_df,publisher_df,class_df1,class_df2,class_df3)
        df_info = pd.DataFrame(col_df,columns=col_name_info)
        df_info_set.append(df_info)

    

book_all_list = [titles_df1,titles_df2,titles_df3,titles_df4,titles_df5,titles_df6]
au_pu_all_df = [au_pu_df1,au_pu_df2,au_pu_df3,au_pu_df4,au_pu_df5,au_pu_df6]
info_all_df = [info_df1,info_df2,info_df3,info_df4,info_df5,info_df6]

total_df = []

for df1, df2 in zip(au_pu_all_df, info_all_df):
    total_df.append(pd.concat([df1, df2],axis=1))

book_all_df = pd.concat([total_df[0],total_df[1],total_df[2],total_df[3],total_df[4],total_df[5]])
book_df2 = book_all_df.reset_index(drop=True)
book_df2

book_df2.to_csv('./book_df2.csv')
# %%
