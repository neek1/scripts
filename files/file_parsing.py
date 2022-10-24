'''This script reads the mbox-short.txt file, pulls 
and avergaes the spam confidence'''
# Use the file name mbox-short.txt  
fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print("Invalid file name:", fname)
    quit()
count = 0
tot = 0.0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    print(line)
    colpos = line.find(":")
    xstr = line[colpos+1:]
    ystr = xstr.lstrip()
    yval = float(ystr)
    count = count + 1
    tot = tot + yval
print("Average spam confidence:", tot/count)
print("done")
