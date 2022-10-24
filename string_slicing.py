'''This script splices the provided text and prints the number'''
text = "X-DSPAM-Confidence:    0.8475"
colpos = text.find(":")
print (colpos)
newstr = text[colpos+1:]
x = newstr.lstrip()
num = float(x)
print (num)
