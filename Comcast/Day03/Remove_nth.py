
n = int(input("Enter the Index number :"))
str = input("Enter the String :")


modified_str = ''

for char in range(0, len(str)):

	if(char != n):
		modified_str += str[char]

print("Modified string after removing ", n, "th character ")
print(modified_str)
