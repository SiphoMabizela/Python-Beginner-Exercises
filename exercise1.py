'''
Exercise 1: Calculate both the sum and the product of two values:
'''

def product(num1,num2):
    result = float(num1 * num2)

    if result >= 1000:
        return result
    else:
        return num1 + num2

print(product(1000,1001))

