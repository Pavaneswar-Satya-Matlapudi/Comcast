employees = ['Nitish', 'Dinesh']
defaults = {"designation": 'Developer', "salary": 8000}

res = dict.fromkeys(employees, defaults)
print(res)

print(res["Dinesh"])