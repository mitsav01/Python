#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Write your code below this line 👇

Total_bill=float(input("Enter amount of bill: "))
Total_person=int(input("How many people were there?: "))

Tip=float(input("Percentage of Tip 10,12,15 or something else: "))
Per_person_contribution = float(Total_bill)/float(Total_person)*(1+(Tip/100))
round_two_digits=round(Per_person_contribution,2)
print(f"Per_person_contribution is $ {round_two_digits}" )
