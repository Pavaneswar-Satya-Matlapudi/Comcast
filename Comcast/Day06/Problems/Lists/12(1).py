l=[10,20,30,40,50,60,70]
l1=[20,40,10,30,22,33,4,55]
r=[x for x in l for y in l1 if x==y]
print(r)