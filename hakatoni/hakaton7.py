user_input = int(input('whrite a number:' ))
mylist= []


while user_input != 0:
    mylist.append(user_input)
    user_input= int(input('write any number:' ))

print(max(mylist))