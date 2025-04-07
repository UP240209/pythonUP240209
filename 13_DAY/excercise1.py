#1
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
negative_or_zero = [num for num in numbers if num <= 0]
print(negative_or_zero)
#2
list_of_lists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flattened_list = [item for sublist in list_of_lists for inner in sublist for item in inner]
print(flattened_list)
#3
list_of_tuples = [(x, 1, x, x**2, x**3, x**4, x**5) for x in range(11)]
print(list_of_tuples)
#4
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

flattened_list = [
    [country.upper(), country[:3].upper(), capital.upper()]
    for sublist in countries for country, capital in sublist
]

print(flattened_list)

#5
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

dict_list = [
    {'country': country.upper(), 'city': capital.upper()}
    for sublist in countries for country, capital in sublist
]

print(dict_list)

#6
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
concatenated_names = [f"{first[0]} {first[1]}" for sublist in names for first in sublist]
print(concatenated_names)
#7
calculate_slope = lambda x1, y1, x2, y2: (y2 - y1) / (x2 - x1) if x1 != x2 else None
calculate_y_intercept = lambda m, x, y: y - m * x