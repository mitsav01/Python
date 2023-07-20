#write a program to generate random password with desired number of letters,characters and symbols
import secrets
import string

print("Welcome to password generator")

num=int(input("How many number you want? "))
upper=int(input("How many uppercase letter you want? "))
lower=int(input("How many lowercase letter you want? "))
special=int(input("How many symbols you want? "))

total_length=num+upper+lower+special

uletters=string.ascii_uppercase
lletters=string.ascii_lowercase
number=string.digits
sym=string.punctuation

pwd=''
password=''
for i in range(num):
    pwd+=''.join(secrets.choice(number))
for i in range(upper):
    pwd+=''.join(secrets.choice(uletters))
for i in range(lower):
    pwd+=''.join(secrets.choice(lletters))
for i in range(special):
    pwd+=''.join(secrets.choice(sym))

print(pwd)