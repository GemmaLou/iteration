amount=0
total=0
user_input=0
while user_input>=0:
    user_input=int(input("Please enter a number followed by 'enter', repeating to find the average of these numbers. When you are done, please enter '-1': "))
    if user_input>0:
        total=total+user_input
        amount=amount+1
average=total/amount
print("The average of these numbers is {0}!".format(average))

