from recommendations import recommedn
import json

budget=int(input("Enter the budget of ur requirement"))
build= recommedn(budget)

print("\nRecommended system is :")
print("cpu:",build["cpu"])
print("gpus:",build["gpus"])
print("ram:",build["ram"])
