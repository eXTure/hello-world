#If number is not provided, return sum of 100
#Otherwise, return a sum of numbers

def sum_numbers(numbers=None):
    result = 0
    if(numbers==None):
        for i in range(1, 101):
            result += i
        return result
    else:
        for number in numbers:
            result += number
        return result
        
print(sum_numbers())