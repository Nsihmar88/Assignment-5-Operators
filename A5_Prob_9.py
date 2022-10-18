# Write a python script to use NOT IN operator to display the data not present in list.

li=[1,2,'naresh',5,4.5,6,9,0b101,7]
s=10
if s not in li:
    print('\n'f'{s} is not present in the list',end='\n\n')
else:
    print('\n'f'{s} is present in the list',end='\n\n')