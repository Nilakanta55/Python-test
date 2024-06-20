import logging

# create a logger string
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"


def add_number(a,b):
    output = a + b
    print("Code executed succefully")

    return output

num = add_number(2,4)
print(num)