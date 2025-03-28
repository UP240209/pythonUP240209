family_members = ('Jacobo', 'Miguel', 'Vanessa', 'Renata', 'Daniel', 'Guadalupe')
siblings = family_members[0:2]  # First two members
parents = family_members[4:6] 

fruits = ('apple', 'banana', 'orange')
vegetables = ('carrot', 'broccoli', 'spinach')
animal_products = ('milk', 'cheese', 'eggs')

food_stuff_tp = fruits + vegetables + animal_products

food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)

middle_item_tp = food_stuff_tp[len(food_stuff_tp) // 2]
middle_item_lt = food_stuff_lt[len(food_stuff_lt) // 2]
print(middle_item_lt)
print(middle_item_tp)

middle_items_tp = food_stuff_tp[len(food_stuff_tp) // 2 - 1:len(food_stuff_tp) // 2 + 1]
middle_items_lt = food_stuff_lt[len(food_stuff_lt) // 2 - 1:len(food_stuff_lt) // 2 + 1]
print(middle_item_lt)
print(middle_item_tp)

first_three_items = food_stuff_lt[:3]
last_three_items = food_stuff_lt[-3:]
print(first_three_items)
print(last_three_items)

del food_stuff_tp

nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')

is_estonia_nordic = 'Estonia' in nordic_countries
is_iceland_nordic = 'Iceland' in nordic_countries
print(is_estonia_nordic)  
print(is_iceland_nordic)  