import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

length_name_list = len(names)

chose_person = random.randint(0,length_name_list - 1)

print(names[chose_person])