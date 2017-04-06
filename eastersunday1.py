
#  File: EasterSunday.py

#  Description: Calculate the date of easter sunday given the year desired by the user

#  Student Name: Arturo Reyes Munoz

#  Student UT EID: ar48836

#  Course Name: CS 303E

#  Unique Number: 50865

#  Date Created: 02/01

#  Date Last Modified: 02/02


y = eval (input ( "Enter year: " ))

a = y%19
b = y//100
c = y%100
d = b//4
e = b%4
g = (8*b+13)//25
h = (19*a+b-d-g+15)%30
j = c//4
k = c%4
m = (a+11*h)//319
r = (2*e+2*j-k-h+m+32)%7
n = (h-m+r+90)//25
p = (h-m+r+n+19)%32

if (n==2):
    month = "February"
elif (n==3):
        month = "March"
elif (n==4):
            month = "April"


        

print ( " In %d Easter Sunday is on %d of %s " % ( y, p, month))        
    
    








