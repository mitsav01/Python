#Write a program to convert Kilometer into Milege


print("How many Kilometers you want to Convert?")
kms = input()
miles= float(kms)/1.609
print(f"Your input is {kms} km." )
print("In miles,"  +kms+ f" km is {round(miles,2)} miles ")
