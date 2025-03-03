age = 18                                                                #1
height = 1.78                                                           #2
complex_var = 2+3j                                                      #3

base_triangle = float(input("Enter the base of a triangle: "))          #4
height_triangle = float(input("Enter the height of a triangle: "))
area_triangle = (base_triangle * height_triangle)/2
print("The area of the triangle is ", area_triangle)

side_a = float(input("Enter side A: "))                                 #5
side_b = float(input("Enter side B: "))
side_c = float(input("Enter side C: "))
perimeter = side_a + side_b + side_c
print("The perimeter of the triangle is ", perimeter)

length = float(input("Insert the length of a rectangle: "))             #6
width = float(input("Insert the width of a rectangle: "))
area_rectangle = length*width
print(area_rectangle)

r = float(input("Enter the value of the radius: "))                     #7
area_of_circle = (r**2)*3.14
circum_of_circle = 2*r*3.14
print("The area of your circle is", area_of_circle)
print("The circumference of your circle is: ", circum_of_circle)

slope = 2                                                               #8
y_inter = -2
x_inter = (slope*0 - y_inter)/slope
print("The slope of the ecuation is: ", int(slope))
print("The x-intercept of the ecuation is: ", int(x_inter))
print("The y-intercept of the ecuation is: ", int(y_inter))

x1, x2, y1, y2 = 2, 6, 2, 10                                            #9
slope_2 = (y2 - y1)/(x2 - x1)
euclidean_dist = ((x2 - x1)**2 + (y2 - y1)**2)**(1/2)
print("The distance between the points is: ", euclidean_dist)
print("The slope of the second ecuation is: ", int(slope_2))

print("Are the two slopes equal? ", slope == slope_2)                   #10


for x in range(-10, 11):                                                #11
    y = x**2 + 6*x + 9
    if y == 0:
        print(f"y is equal to 0 when x has a value of: {x}")

word_length = len("dragon") - len("python")                             #12
if bool(word_length) is False:
    print("Both words are the same length")
else:
    print("The words have a different length")

words = ['python', 'dragon']                                            #13, 15
if all('on' in word for word in words):
    print("The letters 'on' can be found in both words")
else:
    print("There is no 'on' in both dragon and python")

if "jargon" in "I hope this course is not full of jargon":              #14
    print("The word 'jargon' can be found in the sentence")
else:
    print("The word 'jargon' cannot be found in the sentence")

print(str(float(len("python"))))                                        #16

number = float(input("Enter a number: "))                               #17
if number%2 == 0:
    print("The number is an even number")
else:
    print("The number isn´t an even number")

if 7//3 == int(2.7):                                                    #18
    print(True)
else:
    print(False)

if type("10") == type(10):                                              #19
    print(True)
else:
    print(False)

if int(9.8) == 10:                                                      #20
    print(True)
else:
    print(False)

hours = float(input("Enter hours: "))                                   #21
rate = float(input("Enter rate per hour: "))
weekly_earning = hours*rate
print("Your weekly earning is: ", weekly_earning)

years = float(input("Enter the years you´ve lived: "))                  #22
seconds = years*31536e+3
print("You´ve lived for", int(seconds), "seconds.")

table = [                                                               #23
    [1, 1, 1, 1, 1],
    [2, 1, 2, 4, 8],
    [3, 1, 3, 9, 27],
    [4, 1, 4, 16, 64],
    [5, 1, 5, 25, 125],
]
for row in table:
    print(f"{row[0]:<4} {row[1]:<4} {row[2]:<4} {row[3]:<4} {row[4]:<4}")