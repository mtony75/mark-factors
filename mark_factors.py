#----------------------------------
# Practice Python Program by mark fleming jr
# Program will be run to help kids find factors of numbers
#------------------------------------

# Variable sub_number
# Number retrived from user to find factors
# of.
print "Please enter a number"
sub_number = raw_input()

# Find if number entered is a number

if sub_number.isdigit():
    print "This is a number"
else:
    print "This is not a number"

#print "Press Any Key"
#raw_input()
int_number = int(sub_number)
for factors in range(1,int_number):
    if int_number%factors == 0:
        print factors

print int_number

    
