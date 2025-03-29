dog = {}                                                            

dog["name"], dog["color"], dog["breed"], dog["legs"], dog["age"] = "Max", "brown", "Dachshund", 4, 5   
print(dog)

student = {                                                         
    "first_name":"David",
    "last_name":"Padilla",
    "gender":"male",
    "age":18,
    "marital_status":"single",
    "skills":["python", "sleeping", "math"],
    "country":"Mexico",
    "city":"Aguascalientes",
    "address":"Flor de Nochebuena #86"
}

print(len(student))                                                 

print(student["skills"])                                            
print(type(student["skills"]))

student['skills'].append('drawing')                                 

print(list(student.keys()))                                         

print(list(student.values()))                                       

print(student.items())                                              

del student["marital_status"]                                       

del student                                                         