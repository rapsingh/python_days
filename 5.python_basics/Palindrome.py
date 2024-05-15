def checkPalindrome(s):
	k=[]
	p=[]
	for i in s:
		if i.isalpha() or i.isdigit():
			i=i.lower()
			k.append(i)
			p.insert(0,i)
	if k == p:return "Yes"
	
	
