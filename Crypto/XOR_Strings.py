s1 = raw_input("Enter the string 1 : ")
s2 = raw_input("Enter the string 2 : ")

n1 = len(s1)
n2 = len(s2)

n = n1 if n1<n2 else n2

s = []

for i in range(0,n):
	x = chr(ord(s1[i]) ^ ord(s2[i]))
	s.append(x)

print s
print "".join(s)

