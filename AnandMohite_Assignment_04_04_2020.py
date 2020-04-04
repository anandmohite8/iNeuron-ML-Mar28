1. Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, 
between 2000 and 3200 (both included). The numbers 
obtained should be printed in a comma-separated sequence on a single line.

#Program 1#
input_number=[]
for x in range(2000, 3200):
    if (x%7==0) and (x%5!=0):
        input_number.append(str(x))
print (','.join(input_number))



2. Write a Python program to accept the user's first and last name and then getting them 
printed in the the reverse order with a space between first name and last name.

#Program 2#
fname = input("Input your First Name : ")
lname = input("Input your Last Name : ")
print (lname + " " + fname)



3. Write a Python program to find the volume of a sphere with diameter 12 cm. Formula: V=4/3 * π * r3

#Program 3#
pi = 3.1415926535897931
r= 12
V= 4/3*pi* r**3
print('Volume of a sphere with diameter 12 cm is: ',V)


4. Write a program which accepts a sequence of comma-separated numbers from console and generate a list.

#Program 4#
import numpy
values = input("Please provide a sequence of comma-separated numbers: ")
l = values.split(",")
print(l)


5. Create the below pattern using nested for loop in Python.

#Program 5#
max_dot_size=5;
#Print the Dots in gorward order
for first_dot in range(max_dot_size):
    for j in range(first_dot):
        print ('* ', end="")
    print('')

#Print the Dots in reverse order
for first_dot in range(max_dot_size,0,-1):
    for j in range(first_dot):
        print('* ', end="")
    print('')


6. Write a Python program to reverse a word after accepting the input from the user.

#Program 6#
input_word = input("Provide a word to reverse :-")
length=len(input_word)

print("Reverse of that word is :-", end="")
for char in range(length -1, -1, -1):
    print(input_word[char], end="")




7. Write a Python Program to print the given string in the format specified in the sample output.
WE, THE PEOPLE OF INDIA, having solemnly resolved to constitute India into a SOVEREIGN, SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC and to secure to all its citizens

#Program 7#
print("WE, THE PEOPLE OF INDIA,\n\t having solemnly resolved to constitute India into a SOVEREIGN,! \n\t\t SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC \n\t\t and to secure to all its citizens")


