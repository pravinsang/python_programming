colors = ['red', 'orange', 'green']
colors.extend(['black', 'white'])
print(colors)
colors.append('blue')
print(colors)
colors.insert(2, 'yellow')
print(colors)
colors.remove('black')
index = colors.index('red')
print(f"First occurance of red in list is at {index}.")
colors.append('red')
print(colors)
index = colors.index('red', 2, 7)
print(f"First occurance of red between 2, 6 index in list is at {index}.")
colors.pop()
print(colors)
colors.sort(reverse=True)
print(colors)

#where do my list go?
# Programmers occasionally forget that many list methods return None rather than
# creating and returning a new list. As a result, lists sometimes seem to disappear:
# In this example, colors.sort() did two things: it sorted the items in the list, and it returned
# the value None. That’s why variable sorted_colors refers to None. Variable colors, on the
# other hand, refers to the sorted list:
sorted_colors = colors.sort()
print(sorted_colors)
print(colors)