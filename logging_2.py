import logging

logging.basicConfig(filename = 'test.log',level=logging.DEBUG)

def div(a, b):
    return a / b

a = 10
b = 0
logging.debug(f"{a}/{b} = {div(a, b)}")