from recommendations import recommend
from componet_detecter import detecter
from intent import purpose
from compatibiltiy_test import compact
import json
import re

message=input("You:")
numbers=re.findall(r"\d+",message)

if not numbers:
    print("bot: please provide a budget")
pp=purpose(message)
comp=detecter(message)
print("Detected purpose:",pp)
print("Detected gpu by user:",comp)

budget=int(numbers[0])
build= recommend(budget,pp,comp)
comp=compact(build["cpu"],build["motherboard"],build["ram"])
total_price=build["cpu"]["price"]+build["gpus"]["price"]+build["ram"]["price"]+build["motherboard"]["price"]

print("\nbot:")
print("Loading......\n")
print("======Recommended System========")
print(f"Cpu:{build["cpu"]["name"]}:-{build["cpu"]["price"]}")
print(f"Gpus:{build["gpus"]["name"]}:-{build["gpus"]["price"]}")
print(f"Ram:{build["ram"]["name"]}:-{build["ram"]["price"]}")
print(f"Motherboard:{build["motherboard"]["name"]}:-{build["motherboard"]["price"]}\n")

print("Total price:-",total_price)
if comp:
    print("Compatible Build")
else:
    print("Incompatible Build")