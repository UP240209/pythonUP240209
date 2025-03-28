word_1 = "Thirty"                                                                       #1
word_2 = "days"
word_3 = "of"
word_4 = "Python"
space = " "
sentence = word_1 + space + word_2 + space + word_3 + space + word_4
print(sentence)

word_a = "Coding"                                                                       #2
word_b = "for"
word_c = "all"
sentence_2 = word_a + space + word_b + space + word_c
print(sentence_2)

company = sentence_2

print(company)

print(len(company))

print(company.upper())

print(company.lower())

print(company.capitalize())
print(company.title())
print(company.swapcase())

print(company[0:6])

print("Coding" in company)

print(company.replace("Coding", "Python"))

sentence_3 = "Python for everyone"
print(sentence_3.replace("everyone", "all"))

print(company.split())

print("Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon".split(", "))

print("Coding for all"[0])

last_index = len("Coding For All")-1
last_letter = "Coding for all"[last_index]
print(last_index)
print(last_letter)

print("Coding for all"[10])

abbreviation = ""
for letter in "Python For Everyone":
    if (letter.isupper()) == True:
        abbreviation += letter
print(abbreviation)

abbreviation_02 = ""
for letter in "Coding For All":
    if (letter.isupper()) == True:
        abbreviation_02 += letter
print(abbreviation_02)

print(company.find("C"))

print(company.find("f"))

print(company.rfind("i"))

print("You cannot end a sentence with because because because is a conjunction".find("because"))

print("You cannot end a sentence with because because because is a conjunction".rfind("because"))