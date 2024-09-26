import pandas as pd

data = {'이름' : ['Kim', 'Park', 'Lee', 'ho'],
        '국어' : [90, 58, 88, 100],
        '영어' : [100, 60, 80, 70],
        '수학' : [55, 65, 76, 88] }
df = pd.DataFrame(data)

# 1. 데이터 필터림(데이터프레임)
# 2. 분석, 계산

print("1> ----------------------------------")
print("국어 평균 : ", df['국어'].mean(), end="\n\n")
print("국어 중간 : ", df['국어'].median(), end="\n\n") #짝수는 가운데 두 숫자의 평균
print("국어 최소 : ", df['국어'].min(), end="\n\n")
print("국어 최대 : ", df['국어'].max(), end="\n\n")

print("2> ----------------------------------")
print("Kim 총점 : ", df.iloc[0, 1:4].sum(), end="\n\n") #0번째 행의 1~3번째 열
print("Kim 평균 : ", df.iloc[0, 1:4].mean(), end="\n\n")

print("3> ----------------------------------")
print("수학 4분위 \n", df['수학'].quantile([0.25,0.5,0.75]), end="\n\n")
print("수학 분산 : ", df['수학'].var(), end="\n\n")
print("수학 표준편차 : ", df['수학'].std(), end="\n\n")