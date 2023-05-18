#Uber  Interview question - Basic level programming question
#Given a string , find the longest palindrome that can be formed using the characters of the string.

x = "cabcadabaca"

dic = {}

#frequency of each character
for i in x:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

maxlength = 0
odd = 0

for key, value in dic.items():
    maxlength += int(value/2)*2
    if value%2 != 0:
        odd = 1



print(dic)
print(maxlength+odd)