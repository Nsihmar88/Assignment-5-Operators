# Write a python script which takes a three digit number from the user and 
# displays only its last digit.

number=int(input("Enter a three digit number: "))
number=number%10
print(int(number))