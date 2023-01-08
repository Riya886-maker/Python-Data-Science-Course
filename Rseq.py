num=54321
total=0

while num>0:
    num= num // 10
    rem= num % 10
    total+= total*10 + rem
    print(rem,num,total)