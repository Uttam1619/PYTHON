def add_5(a):
    return a+2
list1=[3,6,8,4,8,3,5,8,9,1]
print(list1)

for values in list1:
    print(f"original item was:{values},added 5 to it : {add_5(values)}")
    
