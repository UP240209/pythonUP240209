empty_list = list()

num = [1,2,3,4,5,6,7]

print("Number of variables:", len(num))

firstn = num[0]
print(firstn)
middlen = num[3]
print(middlen)
lastn = num[6]
print(lastn)

mixed_data_types = ["Benjamin", 18, 1.75, "single", "Flor de Nochebuena 84 int 19"]

it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle","Amazon"]

print(it_companies)

print("Number of companies: ",len(it_companies))

firstc = it_companies[0]
print(firstc)
middlec = it_companies[3]
print(middlec)
lastc = it_companies[6]
print(lastc)

it_companies[2] = "Intel"
print(it_companies)

it_companies.append("IT")
print(it_companies)

it_companies.insert(3,"It")
print(it_companies)

it_companies[2] = it_companies[2].upper()
print(it_companies)

result = "#;  ".join(it_companies)
print(result)

does_exist = 'Apple' in it_companies
print(does_exist)

it_companies.sort()
print(it_companies)

it_companies.sort(reverse=True)
print(it_companies)

threecompanies = it_companies[0:3]
print(threecompanies)

lastcom = it_companies[-3:]
print(lastcom)

mid = it_companies[4]
print(mid)

del it_companies[0]
print(it_companies)

del it_companies [3:4]
print(it_companies)

del it_companies[6]
print(it_companies)

it_companies.clear()
print(it_companies)

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
front_back = front_end + back_end
print(front_back)

full_stack = front_back
full_stack.append("Python")
full_stack.append("SQL")
print(full_stack)