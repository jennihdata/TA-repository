word = input("Please enter a word: ")

result = ""
for i in reversed (word):
    result += i
#print(result)

if word == result :
    print("True")
else:
    print("False")