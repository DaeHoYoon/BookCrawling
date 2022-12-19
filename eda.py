# EDA

## 2022년 9월 국내 베스트셀러를 통해 알아보는 연령별 관심사

import pandas as pd
import numpy as np

import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)

plt.style.use("fivethirtyeight")

import warnings
warnings.filterwarnings("ignore")

from wordcloud import WordCloud

df = pd.read_csv("./book_df2.csv", encoding="cp949")
df = df.loc[:,["책제목","대분류", "중분류", "소분류", "연령"]]
df.head()

# 함수

def new_df(df, column_name):
    df_new = df[column_name].value_counts().reset_index(name="빈도")
    df_new.rename(columns={"index": column_name}, inplace=True)
    return df_new

def new_df_year(df, years, column_name):
    df_new_year = df[df["연령"]==years]
    df_new_year = new_df(df_new_year, column_name)
    nan_idx = df_new_year[df_new_year[column_name].str.contains("없음")].index
    df_new_year.drop(nan_idx, inplace=True)
    return df_new_year

def new_df_year_fix(df, years, column_name1, fix, column_name2):
    df_new_year = df[(df["연령"]==years)&(df[column_name1]==fix)]
    df_new_year = new_df(df_new_year, column_name2)
    nan_idx = df_new_year[df_new_year[column_name2].str.contains("없음")].index
    df_new_year.drop(nan_idx, inplace=True)
    return df_new_year


def make_bar_plot(df, column_name, num, years=None):
    plt.figure(figsize=(15, 8))
    plt.title("{} {} 빈도".format(years, column_name), fontsize=30)
    plt.bar(df.iloc[:,0].head(num), df.iloc[:,1].head(num))
    plt.xticks(fontsize=20, rotation=20)
    plt.yticks(fontsize=20)
    plt.show
    plt.savefig('./chart/{}_{}_빈도_bar_plot.jpg'.format(years, column_name))
    
    
def make_word_cloud(df, column_name):
    plt.figure(figsize=(15, 8))
    wc1 = df.set_index(column_name).to_dict()["빈도"]
    wordcloud = WordCloud(font_path='c:/Windows/Fonts/malgun.ttf',background_color='white').generate_from_frequencies(wc1)
    plt.grid(False)
    plt.axis("off")
    plt.imshow(wordcloud);
    plt.savefig('./chart/{}_word_cloud.jpg'.format(column_name))

    
def make_pie(df, years, column_name):
    ratio=[]
    ratio.append(round(df['빈도'][0]/df['빈도'].sum(),2))
    ratio.append(round(df['빈도'][1:].sum()/df['빈도'].sum(),2))
    name = [df[column_name][0], '기타']
    pie_x = [ratio, name]
    
    plt.figure(figsize=(15, 8))
    plt.title("{} {} 순위".format(years, column_name), fontsize=30)
    plt.pie(pie_x[0], labels=pie_x[1], autopct='%.1f%%', startangle=270, labeldistance=0.2, textprops = {'size':15})
    plt.show
    plt.savefig('./chart/{}_{}_순위_pie_chart.jpg'.format(years, column_name))

## 1. 분류별 빈도

# def new_df(df, column_name):
#     df_new = df[column_name].value_counts().reset_index(name="빈도")
#     df_new.rename(columns={"index": column_name}, inplace=True)
#     return df_new

df_new_big = new_df(df, "대분류")
df_new_mid = new_df(df, "중분류")
df_new_sm = new_df(df, "소분류")

### 가. 대분류

df_new_big.head(10)

# def make_bar_plot(df, column_name, num, years=None):
#     plt.figure(figsize=(15, 8))
#     plt.title("{} {} 빈도".format(years, column_name), fontsize=30)
#     plt.bar(df.iloc[:,0].head(num), df.iloc[:,1].head(num))
#     plt.xticks(fontsize=20, rotation=20)
#     plt.yticks(fontsize=20)
#     plt.show()

make_bar_plot(df_new_big, "대분류", 10, "전체연령")

make_word_cloud(df_new_big, "대분류")

### 나. 중분류

df_new_mid.head(10)

make_bar_plot(df_new_mid, "중분류", 10, "전체연령")

## 다. 소분류

df_new_sm.head(10)

make_bar_plot(df_new_sm, "소분류", 10, "전체연령")

## 2. 연령별 빈도

df.head()

def new_df_year(df, years, column_name):
    df_new_year = df[df["연령"]==years]
    df_new_year = new_df(df_new_year, column_name)
    nan_idx = df_new_year[df_new_year[column_name].str.contains("없음")].index
    df_new_year.drop(nan_idx, inplace=True)
    return df_new_year

df_year10_big = new_df_year(df, "10대", "대분류")
df_year10_mid = new_df_year(df, "10대", "중분류")
df_year10_sm = new_df_year(df, "10대", "소분류")

df_year20_big = new_df_year(df, "20대", "대분류")
df_year20_mid = new_df_year(df, "20대", "중분류")
df_year20_sm = new_df_year(df, "20대", "소분류")

df_year30_big = new_df_year(df, "30대", "대분류")
df_year30_mid = new_df_year(df, "30대", "중분류")
df_year30_sm = new_df_year(df, "30대", "소분류")

df_year40_big = new_df_year(df, "40대", "대분류")
df_year40_mid = new_df_year(df, "40대", "중분류")
df_year40_sm = new_df_year(df, "40대", "소분류")

df_year50_big = new_df_year(df, "50대", "대분류")
df_year50_mid = new_df_year(df, "50대", "중분류")
df_year50_sm = new_df_year(df, "50대", "소분류")

df_year60_big = new_df_year(df, "60대", "대분류")
df_year60_mid = new_df_year(df, "60대", "중분류")
df_year60_sm = new_df_year(df, "60대", "소분류")

### 10대_대분류

df_year10_big

make_bar_plot(df_year10_big, "대분류", 10, "10대")

### 10대_중분류

df_year10_mid.head(10)

make_bar_plot(df_year10_mid, "중분류", 10, "10대")

### 10대_소분류

df_year10_sm.head(10)

make_bar_plot(df_year10_sm, "소분류", 10, "10대")

### 20대_대분류

df_year20_big.head(10)

make_bar_plot(df_year20_big, "대분류", 10, "20대")

### 20대_중분류

df_year20_mid.head()

make_bar_plot(df_year20_mid, "중분류", 10, "20대")

### 20대_소분류

df_year20_sm.head()

make_bar_plot(df_year20_sm, "소분류", 10, "20대")

### 30대_대분류

df_year30_big.head()

make_bar_plot(df_year30_big, "대분류", 10, "30대")

### 30대_중분류

df_year30_mid.head()

make_bar_plot(df_year30_mid, "중분류", 10, "30대")

### 30대_소분류

df_year30_sm.head()

make_bar_plot(df_year30_sm, "소분류", 10, "30대")

### 40대_대분류

df_year40_big.head()

make_bar_plot(df_year40_big, "대분류", 10, "40대")

### 40대_중분류

df_year40_mid.head()

make_bar_plot(df_year40_mid, "중분류", 10, "40대")

### 40대_소분류

df_year40_sm.head()

make_bar_plot(df_year40_sm, "소분류", 10, "40대")

### 50대_대분류

df_year50_big.head()

make_bar_plot(df_year50_big, "대분류", 10, "50대")

### 50대_중분류

df_year50_mid.head()

make_bar_plot(df_year50_mid, "중분류", 10, "50대")

### 50대_소분류

df_year50_sm.head()

make_bar_plot(df_year50_sm, "소분류", 10, "50대")

### 60대_대분류

df_year60_big.head()

make_bar_plot(df_year60_big, "대분류", 10, "60대")

### 60대_중분류

df_year60_mid.head()

make_bar_plot(df_year60_mid, "중분류", 10, "60대")

### 60대_소분류

# df_year60_sm.drop('없음',axis=1)


make_bar_plot(df_year60_sm, "소분류", 10, "60대")

## 3. 분류별 최고 빈도

# 연령별 대분류 > 중분류 > 소분류 랭킹 관심사 파이차트 만들기

### 10대

big_df1 = new_df_year(df,'10대', '대분류')
make_pie(big_df1, '10대', '대분류')

big_fix_df1 = new_df_year_fix(df, '10대', '대분류','고등학습서', '중분류')
make_pie(big_fix_df1, '10대', '중분류')

mid_fix_df1 = new_df_year_fix(df, '10대', '중분류','EBS-고등', '소분류')
make_pie(mid_fix_df1, '10대', '소분류')

### 20대

big_df2 = new_df_year(df,'20대', '대분류')
make_pie(big_df2, '20대', '대분류')

big_fix_df2 = new_df_year_fix(df, '20대', '대분류','소설', '중분류')
make_pie(big_fix_df2, '20대', '중분류')

mid_fix_df2 = new_df_year_fix(df, '20대', '중분류','한국소설', '소분류')
make_pie(mid_fix_df2, '20대', '소분류')

### 30대

big_df3 = new_df_year(df,'30대', '대분류')
make_pie(big_df3, '30대', '대분류')

big_fix_df3 = new_df_year_fix(df, '30대', '대분류','경제경영', '중분류')
make_pie(big_fix_df3, '30대', '중분류')

mid_fix_df3 = new_df_year_fix(df, '30대', '중분류','재테크/투자', '소분류')
make_pie(mid_fix_df3, '30대', '소분류')

### 40대

big_df4 = new_df_year(df,'40대', '대분류')
make_pie(big_df4, '40대', '대분류')

big_fix_df4 = new_df_year_fix(df, '40대', '대분류','소설', '중분류')
make_pie(big_fix_df4, '40대', '중분류')

mid_fix_df4 = new_df_year_fix(df, '40대', '중분류','한국소설', '소분류')
make_pie(mid_fix_df4, '40대', '소분류')

### 50대

big_df5 = new_df_year(df,'50대', '대분류')
make_pie(big_df5, '50대', '대분류')

big_fix_df5 = new_df_year_fix(df, '50대', '대분류','고등학습서', '중분류')
make_pie(big_fix_df5, '50대', '중분류')

mid_fix_df5 = new_df_year_fix(df, '50대', '중분류','EBS-고등', '소분류')
make_pie(mid_fix_df5, '50대', '소분류')

### 60대

big_df6 = new_df_year(df,'60대', '대분류')
make_pie(big_df6, '60대', '대분류')

big_fix_df6 = new_df_year_fix(df, '60대', '대분류','시/에세이', '중분류')
make_pie(big_fix_df6, '60대', '중분류')

mid_fix_df6 = new_df_year_fix(df, '60대', '중분류','에세이/산문', '소분류')
make_pie(mid_fix_df6, '60대', '소분류')

def new_df(df, column_name):
    df_new = df[column_name].value_counts().reset_index(name="빈도")
    df_new.rename(columns={"index": column_name}, inplace=True)
    return df_new

round(new_df_year(df, "60대", "대분류")['빈도'][1]/new_df_year(df, "10대", "대분류")['빈도'].sum(),2)