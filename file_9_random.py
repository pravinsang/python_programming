with open('myfile.txt',"r") as f:
    f.seek(7)
    data = f.read(6)
    position = f.tell()
    print(data)
    print(f"File pointer is at {position}")