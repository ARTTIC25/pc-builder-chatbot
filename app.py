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
print("detected purpose:",pp)
print("detected gpu by user:",comp)

budget=int(numbers[0])
build= recommend(budget,pp,comp)
total_price=build["cpu"]["price"]+build["gpus"]["price"]+build["ram"]["price"]

print("\nbot:")
print("Loading......\n")
print("======Recommended System========")
print(f"Cpu:{build["cpu"]["name"]}:-{build["cpu"]["price"]}")
print(f"Gpus:{build["gpus"]["name"]}:-{build["gpus"]["price"]}")
print(f"ram:{build["ram"]["name"]}:-{build["ram"]["price"]}\n")

print("Total price:-",total_price)