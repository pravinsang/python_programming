with open('myfile.bin','wb') as myfile:
    binary_data = b"\x50\x79\x74\x68\x6f\x6e\x20\x69\x73\x20\x65\x61\x73\x79"
    myfile.write(binary_data)

with open('myfile.bin','rb') as myfile:
    binary_data_from_file = myfile.read()
    print(binary_data_from_file)