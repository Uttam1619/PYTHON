items = [55,76,89,True,False,True,[43,76],{'Bihar':'Patna'},4.5,6.9,7.5,"India",
         "America","London",(3.14,),(5,)]
for index,values in enumerate(items):
    print(index,values)

for index,values in enumerate(items):
    if type(values)==int:
        print(f"this is integer:{values}")


for index,values in enumerate(items):
    if type(values)==float:
        print(f"this is float:{values}")

for index,values in enumerate(items):
    if type(values)==str:
        print(f"this is string:{values}")

for index,values in enumerate(items):
    if type(values)==bool:
        print(f"this is boolean:{values}")


for index,values in enumerate(items):
    if type(values)==list:
        print(f"this is list:{values}")


for index,values in enumerate(items):
    if type(values)==dict:
        print(f"this is dictonaries:{values}")

for index,values in enumerate(items):
    if type(values)==tuple:
        print(f"this is tuple:{values}")


