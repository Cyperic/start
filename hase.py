import sys

print ("stylish cool hound")

try:
    d = open("styles.txt")
    e = open("Count.txt","r+")
except:
    print("Datei komisch")
    sys.exit(0)
allezeilen = d.readlines()
d.close()
for i in allezeilen:
    print(i,end ="")

zeile1 = e.readline()
e.seek(0)
new = int(zeile1)+1
print("\nCount:",new)
e.write(str(new))
e.close()



    

