'''
Exercise 1: Calculate both the sum and the product of two values:
'''

def product(num1,num2):
    result = num1 * num2

    if result >= 1000:
        return num1 + num2
    return result
    
print(product(5,1005))
