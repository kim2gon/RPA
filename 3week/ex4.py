print("1~9중 원하는수를 입력하세요")
a = int(input())
if a > 0 and a < 10:
    for i in range(1,10):
        print(f"{a} X {i} = {a*i}")
else:
    print("1~9 사이의 수를 입력해 주세요")





i = 0
num = int(input("수를 입력해 주세요 : "))

if num > 0 and num < 10:
    for i in range(1,10):
        print(f"{num} X {i} = {num*i}")
else:
    print("1~9 사이의 수를 입력해 주세요")