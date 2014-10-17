#Gemma Buckle
#17/10/2014
#iteration rev 3

num_average=int(input("How many numbers do you want to be averaged? "))
num=0
num_count=1
average_num=0
for count in range(num_average):
    num=int(input("Please enter number {0}: ".format(num_count)))
    average_num=average_num+num
    num_count=num_count+1
average=average_num/num_average
print("The average of these numbers is {0}!".format(average))
