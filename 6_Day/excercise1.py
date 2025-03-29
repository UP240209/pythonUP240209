empty_tuple = tuple()
brothers = ("Jacobo", "Miguel")
sisters = ("Vanessa", "Renata")
siblings = brothers + sisters
print(siblings)
print(len(siblings))
siblings = list(siblings)
siblings.append("Daniel")
siblings.append("Guadalupe")
family_members = siblings
family_members = tuple(family_members)
print(family_members)