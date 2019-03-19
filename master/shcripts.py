def numberd(*argv):
	a=0
	b=0
	for arg in argv:
		if arg=='a':
			a+=1
		else:
			b+=1
	total=b+a
	a_percent=((a/total)*100)
	b_percent=((b/total)*100)
	if a>b:
		p="a"
	else: 
		p="b"			
	return {"a_percent":a_percent,"b_percent":b_percent,"pref":p}	

