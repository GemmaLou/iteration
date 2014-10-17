#Gemma Buckle
#17/10/2014
#promts user for 8 numbes and prints total

num=0
total=0
for count in range(8):
    num=int(input("Please enter an integer: "))
    total=total+num
print("The total is {0}!".format(total))
