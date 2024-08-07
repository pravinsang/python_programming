f = open('myfile.txt', 'w')
names = ["Ram\n", "Hari\n", "Shyam\n"]
f.writelines(names)
f.close()

f = open('myfile.txt',"r")
lines = f.readlines()
for line in lines:
    print(line.strip())