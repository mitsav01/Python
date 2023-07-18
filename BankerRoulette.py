#Simple Roulette game which gives a random name from entered data

import random

names=str(input("Enter everybody's name with comma: "))
names=names.split(",")
print(names)

random_number = random.randint(0,len(names)-1)
person_who_will_pay =names[random_number]


print(f"{person_who_will_pay} is going to pay today")

