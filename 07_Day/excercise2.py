A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

AB = A.union(B)
print(AB)

intersection = A.intersection(B)
print(intersection)

print(A.issubset(B))

print(A.isdisjoint(B))

print(A.symmetric_difference(B))

del A
del B