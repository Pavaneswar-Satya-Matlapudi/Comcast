sampleDict = {
  "name": "Dinesh",
  "age":25,
  "salary": 80000,
  "city": "Chennai" }

keys = ["name", "salary"]
re={k :sampleDict[k] for k in keys}
print(re)