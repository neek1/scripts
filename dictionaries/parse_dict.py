'''This script reads the mbox-short.txt file, creates a dictionary of all
the emails from the From lines and provides email with most occurrances'''

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

#sender = list ()
email = dict ()
#Finds lines that starts wiith From_ and pulls email
for line in handle:
    if not line.startswith ('From ') :
        continue
    #print (line)
    words = line.split()
    #print (words[1])
'''#creates a list with all senders email
     if words[1] not in sender:
        sender.append (words[1])
print (sender) '''
#Checks if email is in dictionary, if not adds email, and counts occurances
    email [words[1]] = email.get (words[1],0) + 1
#print (email)

#max loop; determines which email has the most occurances
largest = None
address = None
for k,v in email.items ():
    if largest is None or v > largest:
        largest = v
        address = k
print (address,largest)
