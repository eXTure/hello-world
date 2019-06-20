#FizzBuzz challenge
#Write a program that prints the numbers from 1 to 100.
#But for multiples of three print "Fizz" instead of the number
#and for the multiples of five print "Buzz"

for i in range(1, 101):
    if i%3 == 0:
        if(i%5 == 0):
            print("FizzBuzz")
            continue
        print("Fizz")
        continue
    elif i%5 == 0:
        print("Buzz")
        continue
    print(i)
