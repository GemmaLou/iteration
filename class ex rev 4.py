#Gemma Buckle
#17/10/2014
#rev ex 4

user_num=int(input("Please enter a number between 10 and 20, 10 and 20 included: "))
while 10>user_num>20:
    user_num=int(input("Invalid! Please try again. Enter a number between 10 and 20, 10 and 20 included. "))
print("Thank you! {0} is within range! :)".format(user_num))
