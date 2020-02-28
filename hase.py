import sys

print ("stylish hound")

try:
    d = open("styles.txt")
except:
    print("Datei komisch")
    sys.exit(0)
allezeilen = d.readlines()
d.close()
for i in allezeilen:
    print(i,end ="")

