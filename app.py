from recommendations import recommend
import json
import re
from intent import purpose

message=input("You:")
numbers=re.findall(r"\d+",message)
pp=purpose(message)
print("detected purpose",pp)


budget=int(numbers[0])
build= recommend(budget,pp)

print("\nRecommended system is :")
print("cpu:",build["cpu"])
print("gpus:",build["gpus"])
print("ram:",build["ram"])
