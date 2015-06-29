hexi = raw_input("Input : ")
n = len(hexi)
hexm = hexi[::-1]
r = n % 3
if r>0:
	hexm += (3-r)*'0'
n = len(hexm)

base64 = []

htable = {
	'a':10,
	'b':11,
	'c':12,
	'd':13,
	'e':14,
	'f':15
}

table_64 = {
	0:'A',	16:'Q',	32:'g',	48:'w',
	1:'B',	17:'R',	33:'h',	49:'x',
	2:'C',	18:'S',	34:'i',	50:'y',
	3:'D',	19:'T',	35:'j',	51:'z',
	4:'E',	20:'U',	36:'k',	52:'0',
	5:'F',	21:'V',	37:'l',	53:'1',
	6:'G',	22:'W',	38:'m',	54:'2',
	7:'H',	23:'X',	39:'n',	55:'3',
	8:'I',	24:'Y',	40:'o',	56:'4',
	9:'J',	25:'Z',	41:'p',	57:'5',
	10:'K',	26:'a',	42:'q',	58:'6',
	11:'L', 27:'b',	43:'r',	59:'7',
	12:'M', 28:'c',	44:'s',	60:'8',
	13:'N', 29:'d',	45:'t',	61:'9',
	14:'O', 30:'e',	46:'u',	62:'+',
	15:'P', 31:'f',	47:'v',	63:'/'
}

hexm = hexm.lower()

for i in range(0,n,3):
	temp = hexm[i:i+3]
	if temp[0].isdigit():
		c1 = int(temp[0])
	else:
		c1 = htable[temp[0]]
	if temp[1].isdigit():
		c2 = int(temp[1])
	else:
		c2 = htable[temp[1]]
	if temp[2].isdigit():
		c3 = int(temp[2])
	else:
		c3 = htable[temp[2]]
	c1 += (c2&3)<<4
	c3 = c3<<2
	c3 += (c2&12)>>2
	base64.append(c1)
	base64.append(c3)

out = ""

for i in base64:
	out += table_64[i]

print "Output : %s" % out[::-1]
	

