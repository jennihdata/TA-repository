#1
# num1 = int(input("Insert a number: "))
# num2 = int(input("Insert another number: "))
# num3 = int(input("Insert another number: "))
#
# def max_of_three(num1, num2, num3):
#     if num1 > num2 and num1 > num3:
#         return num1
#     elif num2 > num1 and num2 > num3:
#         return num2
#     else:
#         return num3
# print(max_of_three(num1, num2, num3))

#2
# string = input("Insert a word: ")
# def length(string):
#     a=0
#     for i in string:
#         a += 1
#     print(a)
# length (string)

#3
# word = input("Please type in an alphabet: ")
# vowel = ('a', 'i', 'u', 'e', 'o')
# def isVowel (word):
#      if word not in vowel:
#          print("False")
#      else:
#          print("True")
# isVowel (word)

#4
#word =input("Insert a word: ")
#reverse=""
#for i in reversed(word):
#    reverse += i
#print(reverse)

#5
# character = str(input("Please enter a word: "))
# list1 = ["one", "two", "three", "four", "five"]
# def is_member (character, list1):
#     for i in list1:
#         if character == i:
#             return True
#     return False
# print(is_member(character, list1))

#6
# list1 = ["one", "two", "three", "four", "five"]
# list2 = ["six", "seven", "eight", "nine", "one"]
# def is_member (list1, list2):
#     for j in list1:
#         for i in list2:
#             if i == j:
#                 return True
#     return False
#
# print(is_member(list1, list2))

#7
# def generate_n_chars(n, c):
#     a =""
#     for i in range (n):
#         a += c
#     return a
# print(generate_n_chars(10,"x"))

#8
a = [4,9,7]
def histogram(a):
    for i in a:
        print('*' * i)
histogram(a)

#9
# k = ["word", "hello", "one", "three"]
# def lengthwords (k):
#     length_of_words = []
#     for i in k:
#         length_of_words.append(len(i))
#     return length_of_words
# print(lengthwords(k))

#10
# h = ["apple", "chicken", "monkey", "laptop"]
# def find_longest_word (h):
#     length_of_h = []
#     for i in h:
#         length_of_h.append(len(i))
#     maxNum = max(length_of_h)
#     print (maxNum)
# find_longest_word(h)

#11
# sent = input("Please enter a sentence: ")
# alphabet = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')
# def is_pangram (alphabet):
#     for i in alphabet:
#         if i not in sent:
#             return False
#     return True
# print(is_pangram(alphabet))
#

# 12a
# vowel = ('a','e','i','o','u')
# verb = input("Please enter a verb: ")
# def make_ing_form (verb):
#     if  verb.endswith("e") and verb.endswith("ee") or len(verb)==2:
#         return verb + "ing"
#     elif verb.endswith("ie"):
#         return verb[:-2] + "ying"
#     elif verb.endswith('e'):
#         return verb[:-1] + "ing"
#     elif verb.endswith("e") and (verb[-2]is vowel) and (ver[-3] is not vowel):
#         return verb + verb[:-1] + "ing"
#     else:
#         return verb + "ing"
# print(make_ing_form(verb))
#
