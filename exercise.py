# Guess the output of each answer before you click RUN
# Try to write down your answer before and see how you do... keep it mind I made it a little tricky for you :)

print((5 + 4) * 10 / 2)

print(((5 + 4) * 10) / 2)

print((5 + 4) * (10 / 2))

print(5 + (4 * 10) / 2)

print(5 + 4 * 10 // 2)


# Exercise Augmented Assignment Operator
# Guess what happens here before you click RUN!
# counter = 0
#
# counter += 1
# counter += 1
# counter += 1
# counter += 1
# counter -= 1
# counter *= 2
#
# print(counter) #what will this print?


# age = "21"
# print("age =", int(age))

#formaring string

# 1 What would be the output of the below 4 print statements?
#Try to answer these before you click RUN!

# print("Hello {}, your balance is {}.".format("Cindy", 50))
#
# print("Hello {0}, your balance is {1}.".format("Cindy", 50))
#
# print("Hello {name}, your balance is {amount}.".format(name="Cindy", amount=50))
#
# print("Hello {0}, your balance is {amount}.".format("Cindy", amount=50))

# 2 How would you write this using f-string? (Scroll down for answer)





# name = 'Cindy'
# amount = 50
# print(f"Hello {name}, your balance is {amount}.")

#string

#Guess the output of each print statement before you click RUN!
# python = 'I am PYHTON'
#
# print(python[1:4])
# print(python[1:])
# print(python[:])
# print(python[1:100])
# print(python[-1])
# print(python[-4])
# print(python[:-3])
# print(python[-3:])
# print(python[::-1])
#lists
#What is the output of this code?
#Before you clikc RUN, guess the output of each print statement!
# new_list = ['a', 'b', 'c']
# print(new_list[1])
# print(new_list[-2])
# print(new_list[1:3])
# new_list[0] = 'z'
# print(new_list)
#
# my_list = [1,2,3]
# bonus = my_list + [5]
# my_list[0] = 'z'
# print(my_list)
# print(bonus)
#matrix
# using this list:
# basket = ["Banana", ["Apples", ["Oranges"], "Blueberries"]];
# access "Oranges" and print it:
# You will find the answer if you scroll down to the bottom, but attempt it yourself first!

# Solution:
# basket[1][1][0]

#list2
# Exercise List Methods
# SCROLL FOR ANSWERS!
# using this list,
# basket = ["Banana", "Apples", "Oranges", "Blueberries"]

# 1. Remove the Banana from the list

# 2. Remove "Blueberries" from the list.

# 3. Put "Kiwi" at the end of the list.

# 4. Add "Apples" at the beginning of the list

# 5. Count how many apples in the basket

# 6. empty the basket










# 1. Remove the Banana from the list
# basket.remove('Banana')
# 2. Remove "Blueberries" from the list.
# basket.remove('Blueberries')
# 3. Put "Kiwi" at the end of the list.
# basket.append('Kiwi')
# 4. Add "Apples" at the beginning of the list
# basket.insert(0, 'Apples')
# 5. Count how many apples in the basket
# basket.count('Apples')
# 6. empty the basket
# basket.clear()
# print(basket)
#common lists
#fix this code so that it prints a sorted list of all of our friends (alphabetical). Scroll to see answer
# friends = ['Simon', 'Patty', 'Joy', 'Carrie', 'Amira', 'Chu']

# new_friend = ['Stanley']

# print(friends.sort() + new_friend)













































# Solution: (keep in mind there are multiple ways to do this, so your answer may vary. As long as it works that's all that matters!)
# friends.extend(new_friend)
# print(sorted(friends))


#dictionary 2
# Exercise Dictionary Methods
# Scroll to see answers.

# 1 Create a user profile for your new game.
# This user profile will be stored in a dictionary with keys: 'age', 'username', 'weapons', 'is_active' and 'clan'

# 2 iterate and print all the keys in the above user.

# 3 Add a new weapon to your user

# 4 Add a new key to include 'is_banned'. Set it to false

# 5 Ban the user by setting the previous key to True

# 6 create a new user2 my copying the previous user and update the age value and username value.


#ANSWERS BELOW:

# 1 Create a user profile for your new game.
# This user profile will be stored in a dictionary with keys: 'age', 'username', 'weapons', 'is_active' and 'clan'
# user_profile = {
#     'age': 0,
#     'username': ' ',
#     'weapons': None,
#     'is_active': False,
#     'clan': None
# }

# 2 iterate and print all the keys in the above user.
# print(user_profile.keys())

# 3 Add a new weapon to your user
# user_profile['weapons'] = 'Katana'

# 4 Add a new key to include 'is_banned'. Set it to false
# user_profile.update({'is_banned': False})

# 5 Ban the user by setting the previous key to True
# user_profile['is_banned'] = True

# 6 create a new user2 my copying the previous user and update the age value and username value.
# user2 = user_profile.copy()
# user2.user2pdate({'age': 50, 'username': 'User2'})
# print(user_profile)
# print(user2)
#sets
#Scroll to bottom to see solution
# You are working for the school Principal. We have a database of school students:
# school = {'Bobby','Tammy','Jammy','Sally','Danny'}

#during class, the teachers take attendance and compile it into a list.
# attendance_list = ['Jammy', 'Bobby', 'Danny', 'Sally']

#using what you learned about sets, create a piece of code that the school principal can use to immediately find out who missed class so they can call the parents. (Imagine if the list had 1000s of students. The principal can use the lists generated by the teachers + the school database to use python and make his/her job easier): Find the students that miss class!











































#Solution: Notice how we don't have to convert the attendance_list to a set...it does it for you.
#print(school.difference(attendance_list))


