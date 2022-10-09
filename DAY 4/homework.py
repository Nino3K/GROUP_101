# მომხმარებელს შემოატანინე ორი სახელი და დარინტე ის რომელსაც მეტი თანხმოვანი აქვს
name1 = input("enter name 1: ")
name2 = input("enter name 2: ")

ammount_of_consonant_in_name1 = 0
ammount_of_consonant_in_name2 = 0

for char in name1:
   if char  not in "aeiou":
        ammount_of_consonant_in_name1 += 1
for char in name2:
   if char not in "aeiou":
       ammount_of_consonant_in_name2 += 1 
if ammount_of_consonant_in_name1 > ammount_of_consonant_in_name2:
   print("the ammount of consonant in name1 is more and it contains {} consonant". format(ammount_of_consonant_in_name1))  
if ammount_of_consonant_in_name2 > ammount_of_consonant_in_name1:
   print("the ammount of consonant in name2 is more and it contains {} consonant". format(ammount_of_consonant_in_name2))   
else:
    print("they have equal consonant")
