def odd_values_string(str):
  result = ""
  for i in range(len(str)):
    if i % 2 == 0:
      result += str[i]
  return result

print(odd_values_string('Nitish'))
print(odd_values_string('Samanthakurthi'))