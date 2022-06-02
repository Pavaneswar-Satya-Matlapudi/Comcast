sample_dict = {
    "name": "Dinesh",
    "age": 25,
    "salary": 80000,
    "city": "Chennai"
}
keys = ["name", "salary"]

for k in keys:
    sample_dict.pop(k)
print(sample_dict)