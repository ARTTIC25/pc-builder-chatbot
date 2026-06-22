from recommendations import recommend
from componet_detecter import detecter
from intent import purpose
import json
import re

message=input("You:")
numbers=re.findall(r"\d+",message)

if not numbers:
    print("bot: please provide a budget")
pp=purpose(message)
comp=detecter(message)
print("detected purpose\n",pp)
print("detected gpu by user:",comp)

budget=int(numbers[0])
build= recommend(budget,pp,comp)

print("\nbot:")
print("Loading......")
print("cpu:",build["cpu"])
print("gpus:",build["gpus"])
print("ram:",build["ram"])
