myList = ["mummy", "hannah", "murder for a jar of red rum", "mom", "seagull", "tomato", "no lemon, no melon", "some men interpret nine memos", "madam"]
 
for items in myList:
     clean_item = items.lower().replace(" ", "").replace(",", "")
     
     if clean_item == clean_item[::-1]:
         print(f"{items} is a palindrome")
     else:
        print(f"{items} is not a palindrome")