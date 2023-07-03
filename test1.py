#printing a message to the index of a variable 
names=['Abigail', 'Ajo', 'Becky', 'Joojo', 'Tina']
message=f"Nice to see you again {names[2]}"
print(message)


guest_list = ['Agnes','Bernice','Lizzy']
# add print statement that says initial invites
print(f"Hi, {guest_list[0]}! This is an invitation to my dinner.")
print(f"Hi, {guest_list[1]}! This is an invitation to my dinner.")
print(f"Hi, {guest_list[2]}! This is an invitation to my dinner.")

#change an item in a list
guest_list[guest_list.index('Agnes')]='Becky'
print(guest_list)

# guest_list[get_me_the_index_of_Abby] and change it to 'Deborah'
guest_list[0] = "James"
print(guest_list)

#changing guest list
#taking out a guest name
print(f"Hello,{guest_list[1]}, sorry to hear you can't make it")
print(guest_list)

guest_list[1]="Bob"
print(guest_list)

#update guest list
print(f"Hi, {guest_list[0]}! This is an invitation to my dinner.")
print(f"Hi, {guest_list[1]}! This is an invitation to my dinner.")
print(f"Hi, {guest_list[2]}! This is an invitation to my dinner.")

#inviting more people 
print(f"Hi, {guest_list[:3]}! I found a bigger dinner table.")

#using insert() at beginning of list
guest_list.insert(0,"Tina")
print(guest_list)

#using insert() at the middle of list
guest_list.insert(3,"Vick")
print(guest_list)

#appending to the end of list
guest_list.append("Nana")
print(guest_list)

#reducing guest list
print(f"Sorry guys, {guest_list[:6]}! I can only invite two people")
 
#removning guest using pop()
popped_item = guest_list.pop(0)
print(popped_item)
print(f"Hi, {popped_item}! sorry I can't invite you.")

popped_item = guest_list.pop(1)
print(popped_item)
print(f"Hi, {popped_item}! sorry I can't invite you.")

popped_item = guest_list.pop(2)
print(popped_item)
print(f"Hi, {popped_item}! sorry I can't invite you.")


popped_item = guest_list.pop(2)
print(popped_item)
print(f"Hi, {popped_item}! sorry I can't invite you.")


print(guest_list)

#getting updated list
print(f"Hi, {guest_list[0]}! you're still invited to my dinner.")
print(f"Hi, {guest_list[1]}! you're still invited to my dinner.")

#removing list using de()
del guest_list[:3]
print(guest_list)

#del guest_list[0]
#print(guest_list)











