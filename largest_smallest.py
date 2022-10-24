'''This scripts stores the largest and smallest number entered by 
the user, prints the results once done is entered.'''
largest = None
smallest = None
while True :
    sval = input ('Enter a number ')
    if sval == 'done':
        break
    try:
        x = int(sval)
    except:
        print ('Invalid input')
        continue
    if largest is None and smallest is None:
            largest = x
            smallest = x
    elif  x < smallest:
        smallest = x
    elif x > largest:
        largest = x
print ("Maximum is", largest)
print ("Minimum is", smallest)
