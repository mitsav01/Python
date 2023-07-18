"""I was reading this article by Tim Urban - Your Life in Weeks and realised just how little time we actually have.
https://waitbutwhy.com/2014/05/life-weeks.html

Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.
It will take your current age as the input and output a message with our time left in this format:

You have x days, y weeks, and z months left.
Where x, y and z are replaced with the actual calculated numbers
"""


age=int(input("What is your age?"))

remaining_years=90-age
remaining_months=12*remaining_years
remaining_weeks=4*remaining_months

print(f"You have {remaining_years} years, {remaining_months} months and {remaining_weeks} weeks left")
