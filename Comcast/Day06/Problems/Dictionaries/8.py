sample_dict = {
    "name": "DInesh",
    "age": 25,
    "salary": 80000,
    "city": "Chennai"
}

sample_dict['location'] = sample_dict.pop('city')
print(sample_dict)