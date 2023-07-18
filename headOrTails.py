#Write a program which behaves as a coin for Toss consisting of Two States: Heads or Tails

import random

number=random.randint(0,1)

if number==1:
    print("Heads")
else:
    print("Tails")