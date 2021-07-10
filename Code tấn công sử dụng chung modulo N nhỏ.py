#Nguyen Hai Dang
#Code tan cong dua theo viec n duoc nhieu nguoi su dung

def Euclidean_GCD(a, b):
	if a==0 or b ==0:
		return a+b
	while a!=b:
		if a>b:
			a=a-b
		else:
			b=b-a
	return a

def RSA_encryption(p, q, e):
	n = p*q
	lamb = (p-1)*(q-1)/Euclidean_GCD(p-1,q-1)
	k=0
	while ((1+lamb*k)%e)!=0:
		k=k+1
	k=k+1
	while ((1+lamb*k)%e)!=0:
		k=k+1
	d = int((1+lamb*k)/e)
	return d,n

def Find_r_s(t,e2,f):
	r=1
	while True:
		r=r+1
		if ((f+r*t)%e2)==0 and ((f+r*t)/e2)!=e2:
			break
	s=(f+r*t)/e2
	return (r,int(s))
def Find_D2(e1,d1,e2):
	t = e1*d1 - 1
	f = Euclidean_GCD(e2,t)
	r,s=Find_r_s(t,e2,f)
	while f!=1:
		t=t/f
		f = Euclidean_GCD(e2,t)
		r,s=Find_r_s(t,e2,f)
	return s
#message = "ILOVEAN"
#hash_mes = hash(message)

#print(RSA_encryption(5,7,11))
#print(Euclidean_GCD(20,15))

print(Find_D2(5,17,11))
