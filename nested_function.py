def outerFunction(text):
 
    def innerFunction():
        print(text)
 
    innerFunction()
    print("Remaining Part of outer function")
 
 
outerFunction('Hey!')