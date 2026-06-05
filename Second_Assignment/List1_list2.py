list1 = []
list2 = []


while True:
    x = input("enter x for list 1: ")
    list1.append(x)
    
    x = input("Are you done? Yes/no: ")
    if x == "yes":
        break
    
while True:
    x = input("enter x for list 2: ")
    list2.append(x)
        
    x = input("Are you done? yes/no: ")
    if x == "yes":
        break
        
if len(list1) != len(list2):
    print("length of list don't match")
else:
    print("length match.proceeding...")
            
    print(".")
    print(".")
    print(".")
            
    my_dict ={}
            
    for i in range(len(list1)):
        my_dict[list[i]] = list2[i]
                
        print(my_dict)
                