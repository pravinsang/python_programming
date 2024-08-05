import logging

logging.basicConfig(filename='test.log', level=logging.DEBUG)

def div(a, b):
    try:
        return a / b
    except Exception:
        logging.exception(f"An error occurred with a, b = {a}, {b}")

a = 20
b = 0

result = div(a, b)
if result is not None:
    logging.debug(f"{a}/{b} = {result}")
else:
    logging.debug(f"Division failed for {a}/{b}")
