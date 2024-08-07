f = open('myfile.txt', 'a')
names = ["Krishna\n", "Shiva\n", "Sita\n"]
f.writelines(names)
f.close()
