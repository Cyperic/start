import sys

print ("HELLO THERE")

try:
    d = open("styles.txt")
except:
    print("Datei komisch")
    sys.exit(0)
allezeilen = d.readlines()
d.close()
print(allezeilen)
