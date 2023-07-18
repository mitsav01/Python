#Write a program to calculate BMI from person's height and weight and show if it is normal or not

print("BMI Calculator")
weight=float(input("Enter weight in kg: "))
height=float(input("Enter height in m: "))

BMI= round(weight/(height**2),2)

print(f"Your BMI is {BMI}")

if BMI>25:
    print("You are overweight.")
elif BMI>18.5:
    print("You are healthy.")
elif BMI>=40:
    print("You are obese")
else:
    print("You are underweight")
