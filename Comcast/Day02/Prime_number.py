
start = 50
stop = 150
count=0

print("Prime numbers between", start, "and", stop, "are:")

for val in range(start, stop):
  if val > 1:
    for i in range(2, val):
      if (val % i) == 0:
        break
    else:
      count=count+1
      print(val, end=" ")
print()
print(f"Count of {count}")