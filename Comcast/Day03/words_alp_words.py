
test_str = 'Python3.0 is the lastest version98'

print("The original string is : " + test_str)
res = []
temp = test_str.split()
for idx in temp:
    if any(chr.isalpha() for chr in idx) and any(chr.isdigit() for chr in idx):
        res.append(idx)
print("Words with alphabets and numbers : " + str(res))
