with open('myfile.bin','wb') as myfile:
    binary_data = b'\x48\x65\x6c\x6c\x6f'
    myfile.write(binary_data)

with open('myfile.bin','rb') as myfile:
    binary_data_from_file = myfile.read()
    print(binary_data_from_file)
