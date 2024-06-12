def outerFunction(text):
 
    def innerFunction():
        print(text)
 
    return innerFunction
 
myfunction = outerFunction('Hey!')
myfunction()