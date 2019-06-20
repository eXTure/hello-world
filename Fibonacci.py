#Fibonacci sequence

n1 = 1
n2 = 1
n3 = 0
x = 1
sum_of_even = 1
print("1")

while x>0:
    x += 1

    n3 = n1 + n2
    n2 = n1
    n1 = n3
    
    if n3%2 == 0:
        sum_of_even += n3

    print(n3)
    if n3 >= 4000000:
        break

print("This program ran " + str(x) + " times")
print("Sum of even numbers is: " + str(sum_of_even))