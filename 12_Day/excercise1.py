import random
import string
#level 1

charachters = string.ascii_letters + string.digits
def random_user_id():
    user="".join(random.choices(charachters, k=6))
    return user
print(random_user_id())

charsize = int(input('Inserte el tamaño de los caracteres: '))
charlimit = int(input('Insterte el numero de ID que se van a hacer : '))
def user_id_gen_by_user(): 
    user = [''.join(random.choices(charachters, k=charsize)) for _ in range(charlimit)]
    return user
print(user_id_gen_by_user())

def rgb_color_gen():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    return r,g,b
print(rgb_color_gen())