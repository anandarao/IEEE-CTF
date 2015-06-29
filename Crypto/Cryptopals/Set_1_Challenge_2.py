input1 = raw_input("Input 1 : ")
input2 = raw_input("Input 2 : ")

#input1 = '1c0111001f010100061a024b53535009181c'
#input2 = '686974207468652062756c6c277320657965'

output = []

for i in range(0,len(input1)):
	output.append(hex(int(input1[i],base=16)^int(input2[i],base=16)))

print "Output : ",
print "".join(i[2] for i in output)