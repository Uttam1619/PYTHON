totalInput = list()
for i in range(1):
    totalInput.append(input("Enter your name :"))
for i in range(1):
    totalInput.append(input("Enter your age:"))
for i in   range(1):
    totalInput.append(input("Enter your gender:"))
for i in range(1):
    totalInput.append(input("Enter your qualification:"))
for i in range(1):
    totalInput.append(input("Enter your address:"))
for i in range(1):
    totalInput.append(input("Enter your profession:"))

print(totalInput)

for i in totalInput:
    if i.startswith('u'):
        print(f"starts with u:{i}")
    else:
        print(f"not starts with u:{i}")





