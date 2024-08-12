import os

cur_dir = os.getcwd()
print(cur_dir)
files = os.listdir('.')
print(files)
get_file = os.path.exists('myfile.txt')
print(get_file)
path = os.path.join('folder', 'subfolder', 'file.txt')
print(path)