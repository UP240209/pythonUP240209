import random

#1
def shuffle_list(lst):
    random.shuffle(lst)
    return lst

#2
def numeros():
    return random.sample(range(10), 7)
print(numeros)
