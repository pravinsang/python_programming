str1 = "Hello"
str2 = "World"
result1 = str1 + " " + str2                  #concatination of String
print("After concatination: "+result1)
result2 = result1 * 3                        #Repetition of String
print("After Repetition: "+result2)
first_char = str1[0]                         #indexing a String
last_char = str1[-1]
print("First char: "+ first_char)
print("Last char: "+ last_char)
first_word = result1[:5]                     #slicing a String
last_word =  result1[6:]
print("First word: "+ first_word)
print("last word: "+ last_word)