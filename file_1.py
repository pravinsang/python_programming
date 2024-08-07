f = open('myfile.txt', 'w')

f.write('From File\nHello world')
f.close()

f = open('myfile.txt', 'r')

print(f.read())
f.close()

