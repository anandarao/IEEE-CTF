pt = raw_input("Enter the plain text : ")
key = raw_input("Enter the key : ")

n = len(pt)
l = len(key)

ct = []

for i in range(0,n):
	ct.append(hex(int(key[i%l],base=16)^int(pt[i],base=16)))
	
ans=[]

for i in ct:
	ans.append(i[2])

print "Cipher Text : " + "".join(ans)