
# read data
import pandas as pd

### Box plot
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import matplotlib.ticker as ticker

font_path = "./NanumGothic.ttf"
font_prop = fm.FontProperties(fname=font_path)
plt.rcParams['font.family'] = font_prop.get_name()

#######################################
###### 진료항목 vs 진료비 boxplot ######
#######################################

# df = pd.read_csv('../data_storage/fake_petinsurance_chart.csv')


# plt.figure(figsize = (10, 8))
# # sns.boxplot(x = 'age', y = 'claim_price', data = df)
# # plt.show()

# ax = sns.boxplot(x = 'disease_name', y = 'claim_price', data = df, )
# # y축의 값을 축약하지 않고 표시
# ax.yaxis.set_major_formatter(ticker.ScalarFormatter(useOffset=False))
# ax.ticklabel_format(style='plain', axis='y')

# # x축 레이블을 세로로 회전
# ax.set_xticklabels(ax.get_xticklabels(), rotation=90, fontproperties=font_prop)

# plt.savefig('disease_price_boxplot.png')


###################################
###### 나이 vs 진료비 산점도 #######
#####################################
import numpy as np
import pandas as pd

# 가상 데이터 생성
np.random.seed(0)
ages = np.random.uniform(0, 20, size=1000)  # 20세에서 70세 사이의 나이 100개
costs = ages * 150000 + np.random.normal(10000, 1500000, size=1000)  # 나이에 비례하는 진료비 (일부 노이즈 추가)

# 데이터 프레임으로 변환
data = pd.DataFrame({'Age': ages, 'claim_price': costs})

data.head()


# Seaborn 산점도
plt.figure(figsize=(10, 6))
ax = sns.scatterplot(x='Age', y='claim_price', data=data)
plt.figure(figsize=(10, 6))
sns.regplot(x='Age', y='claim_price', data=data, scatter_kws={'alpha':0.7}, line_kws={'color': 'red'})

# 회귀선의 상관계수 계산
correlation_coefficient = np.corrcoef(data['Age'], data['claim_price'])[0, 1]
print(f"상관계수 (Pearson correlation coefficient): {correlation_coefficient:.2f}")

# 그래프 꾸미기
plt.title('나이에 따른 진료비 산점도와 회귀선', fontsize=15, fontproperties=font_prop)
plt.xlabel('나이', fontsize=12, fontproperties=font_prop)
plt.ylabel('진료비', fontsize=12, fontproperties=font_prop)
plt.grid(True)
plt.tight_layout()

# 그래프 표시
plt.savefig('age_price_scatterplot.png')