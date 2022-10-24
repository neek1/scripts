'''This script reads the romeo.txt file, creates an alphabetized list 
of all the words used in the passage'''
# Use the file name romeo.txt 
fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print("Invalid file name:",fname)
    quit()
lst = list()
for line in fh:
    wrds = line.split()
    if len(wrds) < 1:
        continue
    for wrd in wrds:
        if wrd not in lst:
            lst.append(wrd)
            continue
lst.sort()
print(lst)
