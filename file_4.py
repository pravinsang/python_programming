even_num = []
odd_num = []
with open('source.txt','r') as src_file:
    str_numbers = src_file.readlines()
    numbers = list(map(int,str_numbers))
    for number in numbers:
        if number % 2 == 0:
            even_num.append(str(number) + '\n')
        else:
            odd_num.append(str(number) + '\n')

with open('even.txt','w') as even_file:
    even_file.writelines(even_num)

with open('odd.txt','w') as odd_file:
    odd_file.writelines(odd_num)

