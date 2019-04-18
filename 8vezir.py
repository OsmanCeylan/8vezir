import random
import time
import threading
import contextlib

print ("Bulama ihtimali 2 yuz trilyonda 1 dir :D");
loop=True
def stop():
    global loop
    loop=False
A=[7]
timer=threading.Timer(2,stop)
timer.start()
x=6
m=7
while loop:
    A.append(x)
    A.remove(m)
    m=m-1
    x=x-1
    print(A)
    if A[0]==0:
        print ("Basla");
    if A[0]==0:break
afk=0
dota=0
while afk==0: 
	F=[]
	k=1
	coz=0
	while k<9:
		a=random.randrange(1,9)
		b=random.randrange(1,9)
		F.append((a,b))
		k=k+1
	#2 while's seaching for a any same places' queens
	k=0
	m=7
	g4=[0]
	z=0
	while m>0:
			k=0
			while k<m:
					if F[k]==F[m]:
							z=z+1
							g4.append(z)
					k=k+1
			m=m-1
	for i2 in range(0,len(g4)):
			Eb0=g4[0]
			if g4[i2]>Eb0:
					Eb0=g4[i2]
	if Eb0==0:
			print ("Hicbir vezir ayni yerde degil");
			coz=coz+1
	else:
			print (Eb0, "tane ayni yerde vezir var")
	#This part is search for a any queens can beat each other from horizonal and vertical side
	u=0
	g5=[0]
	g6=[0]
	t=7
	z=0
	c=0
	while t>0:
			u=0
			while u<t:
					(n,m)=F[u]
					(h,j)=F[t]
					if n==h:
							z=z+1
							g5.append(z)
					if m==j:
							c=c+1
							g6.append(c)
					u=u+1
			t=t-1
	for i1 in range(0,len(g5)):
			Eb1=g5[0]
			if g5[i1]>Eb1:
					Eb1=g5[i1]
	for p1 in range(0,len(g6)):
			Eb2=g6[0]
			if g6[p1]>Eb2:
					Eb2=g6[p1]
	if Eb1==0:
			print ("Hicbir vezir yatay da birbirini tehdit etmemekte")
			coz=coz+1
	else:
			print (Eb1,"tane yatayda tehdit eden vezir var")
	if Eb2==0:
			print ("Hicbir vezir dikeyde birbirini tehdit etmemekte")
			coz=coz+1
	else:
			print (Eb2,"tane dikeyde tehdit eden vezir var")
	#This part is search for a any queens can beat eack other from cross side(right-up cross)

	g8=[0]
	u=0
	t=7
	z=0
	while t>0:
			u=0
			while u<t:
					(n,m)=F[u]
					(h,j)=F[t]
					while int(n)<=8 and int(m)>=0:
							if int(n)+1==h and int(m)-1==j:
									z=z+1
									g8.append(z)
							n=int(n)+1
							m=int(m)-1
					u=u+1
			t=t-1
	for i0 in range(0,len(g8)):
			Eb9=g8[0]
			if g8[i0]>Eb9:
					Eb9=g8[i0]
	if Eb9==0:
			print ("Hicbir vezir sag carpraz yukari dogrultuda birbirlerini tehdit etmemekte")
			coz=coz+1
	else:
			print (Eb9,"tane sag carpraz yukari dogrultuda birbirlerini tehdit eden vezir var")
	#This part is search for a any queens can beat eack other from cross side(right-down cross)

	g0=[0]
	u=0
	t=7
	z=0
	while t>0:
			u=0
			while u<t:
					(n,m)=F[u]
					(h,j)=F[t]
					while int(n)>=0 and int(m)<=8:
							if int(n)-1==h and int(m)+1==j:
									z=z+1
									g0.append(z)
							n=int(n)-1
							m=int(m)+1
					u=u+1
			t=t-1
	for i9 in range(0,len(g0)):
			Ebv=g0[0]
			if g0[i9]>Ebv:
					Ebv=g0[i9]
	if Ebv==0:
			print ("Hicbir vezir sag carpraz asagi dogrultuda birbirlerini tehdit etmemekte")
			coz=coz+1
	else:
			print (Ebv,"tane sag carpraz asagi dogrultuda birbirlerini tehdit eden vezir var")
	#This part is search for a any queens can beat eack other from cross side(left-up cross)
	yu=[0]
	u=0
	t=7
	z=0
	while t>0:
			u=0
			while u<t:
					(n,m)=F[u]
					(h,j)=F[t]
					while int(n)>=0 and int(m)>=0:
							if int(n)-1==h and int(m)-1==j:
									z=z+1
									yu.append(z)                
							n=int(n)-1
							m=int(m)-1
					u=u+1
			t=t-1
	for bu in range(0,len(yu)):
			Ru=yu[0]
			if yu[bu]>Ru:
					Ru=yu[bu]
	if Ru==0:
			print ("Hicbir vezir sol carpraz yukari dogrultuda birbirlerini tehdit etmemekte")
			coz=coz+1
	else:
			print (Ru,"tane sol carpraz yukari dogrultuda birbirlerini tehdit eden vezir var")

	#This part is search for a any queens can beat eack other from cross side(left-down cross)
	jo=[0]
	u=0
	t=7
	z=0
	while t>0:
			u=0
			while u<t:
					(n,m)=F[u]
					(h,j)=F[t]
					while int(n)<=8 and int(m)<=8:
							if int(n)+1==h and int(m)+1==j:
									z=z+1
									jo.append(z)
							n=int(n)+1
							m=int(m)+1
					u=u+1
			t=t-1
	for tu in range(0,len(jo)):
			gh=jo[0]
			if jo[tu]>gh:
					gh=jo[tu]
	if gh==0:
			print ("Hicbir vezir sol carpraz asagi dogrultuda birbirlerini tehdit etmemekte")
			coz=coz+1
	else:
			print (gh,"tane sol carpraz asagi dogrultuda birbirlerini tehdit vezir var")
	if coz==7:
			print ("\n!Tebrikler Olabilecek 92 Sonuctan 1'ine Ulastiniz!\n\n\
				   !Congralations!\n")
			dota=dota+1
			afk=afk+1
	print ("Vezirler ve Koordinatlari;",F,"Toplam vezir saysi:8",dota,"kadar cozum bulabildim") 
