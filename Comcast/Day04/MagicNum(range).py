sum1 = 0
n = 145
temp = n
while(n):
    i=1
    j=1
    k = n%10
    while(i<=k):
        j= j*i
        i= i+1
    sum1 = sum1+j
    n=n//10
if(sum1 == temp):
    print(f"{temp} is Magic number")
else:
    print("Nope")