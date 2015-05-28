pt = raw_input("Enter the plain text : ")
pt = pt.upper()

key = raw_input("Enter the key : ")
key = key.upper()

ct = []

for i in range(0,len(pt)):
	a = (ord(pt[i]) - 65 + ord(key[i % len(key)]) - 65) % 26 + 65
	ct.append(chr(a))
	
print "Plain Text : %s " % pt
print "Key : %s " % key
print "Cipher Text : %s " % "".join(ct)
