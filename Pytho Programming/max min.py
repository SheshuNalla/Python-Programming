l=[15,2,7,25,10]

maxi=l[0]
mini=l[0]
for i in l:
	if i > maxi:
	   maxi=i
	if i < mini:
		mini=i
print(maxi,mini)