def add_two_numbers ():
    num_one = 2
    num_two = 3
    total = num_one + num_two
    print(total)
add_two_numbers()

def area_circle ():
    pi = 3.14
    r = int(input("Enter radio: "))
    area = pi * r * r
    print(area)
area_circle()

def add_all_nums(*args):
    total = 0
    for arg in args:
        if isinstance(arg, (int, float)):  
            total += arg
        else:
            return f"Error: {arg} is not a number."  
    return total
print(add_all_nums(1, 2, 3, 4)) 
add_all_nums()

def convert_celsius_to_fahrenheit():
    C = float(input("Enter °C : "))
    F = (C * 9/5) + 32
    print(F)
convert_celsius_to_fahrenheit()

month = int(input())
def check_season(month):
    if month < 1 or month > 12:
        return "Error: Please enter a valid month number (1 to 12)."
    if month in [12, 1, 2]:
        return "Winter" 
    elif month in [3, 4, 5]:
        return "Spring"  
    elif month in [6, 7, 8]:
        return "Summer"  
    else:
        return "Autumn" 
    print(check_season(1))  
    print(check_season(4)) 
check_season(month)

def solve_quadratic_eqn(a,b,c):
     D = b * b - 4 * a * c
     X1 = (-b + D) / (2 * a)
     return X1

print(solve_quadratic_eqn(8,4,6))

def calculate_slope(x1, y1, x2, y2):

    if x2 - x1 == 0:
        return "Error: Division by zero. The line is vertical."
    slope = (y2 - y1) / (x2 - x1)
    return slope
x1, y1 = (1, 2)
x2, y2 = (3, 6)
slope = calculate_slope(x1, y1, x2, y2)
print(f"The slope of the line passing through the points ({x1}, {y1}) and ({x2}, {y2}) is: {slope}")

def print_list(lst):
    for item in lst:
        print(item)
my_list = [1, 2, 3, 4, 5]
print_list(my_list)

def reverse_list(arr):
    reversed_arr = []
    for i in range(len(arr) - 1, -1, -1):
        reversed_arr.append(arr[i])
    return reversed_arr
print(reverse_list([1, 2, 3, 4, 5]))

def capitalize_list_items():
    lista=[]
    lista.append(input("Inserte a la lista: "))
    print(lista.capitalize())
capitalize_list_items


def add_item(mutable, tba):
    mutable.append(tba)
    return mutable



def remove_item(mutable, tbr):
    mutable.remove(tbr)
    return mutable



def sum_of_numbers(high):
    sum_of_numbers = 0
    for i in range(high + 1):
        sum_of_numbers += i
    return sum_of_numbers



def sum_of_odds(high):
    sum_of_odd_nums = 0
    for i in range(high + 1):
        if i % 2 == 1:
            sum_of_odd_nums += i
    return sum_of_odd_nums



def sum_of_even(high):
    sum_of_even_nums = 0
    for i in range(high + 1):
        if i % 2 == 0:
            sum_of_even_nums += i
    return sum_of_even_nums