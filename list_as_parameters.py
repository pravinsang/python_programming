def modify_list(list):
    index = int(input("Enter the index: "))
    value = input("Enter the value: ")
    list[index] = value
    return list

nobles = ['helium', 'none', 'argon', 'krypton', 'xenon', 'radon']
modify_list(nobles)
print(nobles)