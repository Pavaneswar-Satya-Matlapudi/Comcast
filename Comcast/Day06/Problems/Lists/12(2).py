l=[10,20,30,40,50,60,70]
l1=[20,40,10,30,22,33,4,55]

Result = [i for i in l + l1 if i not in l or i not in l1]

print(Result)