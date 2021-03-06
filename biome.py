# Function to apply colors to the different regions of the map
def height(h):
	if h >=84: 
		return brighten('#c7c7c7', h-84) # ππ―π°πΈ ππ°πΆπ΅π’πͺπ―
	elif h >= 70: 
		return brighten('#414042', h-70) # ππ°πΆπ΅π’πͺπ―
	elif h >= 40: 
		return brighten('#265218', h-50) # ππ­π’π΅
	elif h >= 30:
		return brighten('#d2c78b', h-40) # ππ’π―π₯
	else: 
		return brighten('#1b1c69', h) # ππ’π΅π¦π³

# Function to adjust color shades
def brighten(color, rate):
    color = color.replace('#', '')
    s = '#'
    for i in [0,2,4]:
        c = color[i:i+2]
        c = int(c, 16)
        c = int(c + (rate*1))
        c = format(c, '02x')
        s += c
    return s
