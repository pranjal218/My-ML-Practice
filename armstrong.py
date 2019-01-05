n=int(input("enter a number"))
t=n
s=0
while(n>0):
	a=n%10;
	s=s+(a*a*a)
	n//=10
if(t==s):
	print("armstrong")
else:
	print("not armstrong")
print("end of file")