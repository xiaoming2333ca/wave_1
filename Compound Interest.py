import math

original_balance = int(input("please enter your original balance that you deposit: "))

for i in range(1, 4):
    print(f"the {i} year's balance is {original_balance * pow(1.04, i)}")
