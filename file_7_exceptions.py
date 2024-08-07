try:
    with open('myfile.txt',"r") as f:
        lines = f.readlines()
        for line in lines:
            print(line.strip())

except FileNotFoundError:
    print("Error File not found")
except PermissionError:
    print("Error You do not have permission")
except IOError:
    print("Error IO error occurs")
except Exception as e:
    print("An error occured",e)