#Write a program,asking user to enter a number then determine whether it is odd or even

print("Odd or Even")
num=int(input("Enter a number: "))

if num%2==0 and num!=0:
    print(f"{num} is even number")
elif num==0:
    print("You have entered zero")
else:
    print(f"{num} is odd number")