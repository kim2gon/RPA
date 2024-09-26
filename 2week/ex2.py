a=123
b=15.556
print(a,b,sep=',', end='\n\n') #a,b 중간에 ,를 넣고 2줄을 띄운다 라는 뜻

print("a:{0} b:{1}".format(a, b))
print(f"a:{a} b:{b}")

print(f"a:{a:05d} b:{b:2f}")
print("a:%05d b:%.2f" % (a, b))