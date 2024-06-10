ten = set(range(10))
whole = {0, 1, 2, 3, 4}
odd = {1, 3, 5, 7, 9}
print(whole.difference(odd))
print(whole.intersection(odd))
print(whole.issubset(ten))
whole.remove(0)
print(whole)