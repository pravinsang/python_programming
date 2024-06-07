life = [['Nepal', 68.45], ['India', 67.24], ['China', 78.21]]
print(life[0])
print(life[0][0])
print(life[1][0])
nepal = life[0]
print(nepal)
print(nepal[1])
#Suppose the life expectancy of nepal changes to 70.55
#we can change it using the sublist reference
#changes in sublist can be seen in the main list
nepal[1] = 70.55
print(life)