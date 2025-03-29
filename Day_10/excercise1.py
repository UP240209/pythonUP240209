count = 0                                                                       
while count < 11:
    print(count)
    count = count + 1
for i in range(0,11):
    print(i)

count = 10                                                                      
while -1 < count:
    print(count)
    count = count - 1
for i in range(10, -1, -1):
    print(i)

triangle = "#"                                                                  
for i in range(0, 7):
    print(triangle)
    triangle = triangle + "#"

square = ""                                                                     
for row in range(8):
    for col in range(8):
        square = square + "# "
    square = square + "\n"
print(square)

for i in range(11):                                                             
    print(f"{i} x {i} = {i*i}")

for i in ['Python', 'Numpy','Pandas','Django', 'Flask']:                        
    print(i)

for i in range(101):                                                            
    if i%2==0:
        print(i)

for i in range(101):                                                            
    if i%2==1:
        print(i)