# 임의의 정수를 입력 받아서 1~정수까지 합을 구하는 프로그램
# 정수합을 구하는 로직은 함수(sumfunc)로 만들어야함

def sumfunc(num):
    sum = 0
    for j in range(1,num+1):
        sum = sum + j
    return sum


print("1이상의 정수를 입력 하시오")
num = int(input())
sum = sumfunc(num)
print(f'1 ~ {num}까지 정수의 합은 {sum} 입니다.')