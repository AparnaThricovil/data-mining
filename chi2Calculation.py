'''
Original Value :

			|	RHS-present	|	RHS-absent |
------------|---------------|--------------|---------------				
LHS-present |		A 		|		B 	   |	 A+B = T1
LHS-absent	|		C		|		D	   |	 C+D = T2
-----------------------------------------------------------
			|	A+C = S1	|	B+D = S2   |		N

Expected Value :

			|	RHS-present	|	RHS-absent |
------------|---------------|--------------|---------------				
LHS-present |		X1 		|		Y1 	   |	 
LHS-absent	|		X2		|		Y2	   |	 
-----------------------------------------------------------
			
X1 = (S1*T1) / N
X2 = (S1*T2) / N
Y1 = (S2*T1) / N
Y2 = (S2*T2) / N


X2 = (A-X1)^2/X1 + (B-Y2)^2/Y2 + (C-X2)^2/X2 + (D-Y2)^2/Y2
'''
import math
def calculate(a,b,c,d):
	S1 = a + c
	S2 = b + d
	T1 = a + b
	T2 = c + d
	N = T1 + T2
	X1 = float(S1*T1)/N
	X2 = float(S1*T2)/N
	Y1 = float(S2*T1)/N
	Y2 = float(S2*T2)/N
	if(X1==0 and X2==0 and Y1==0 and Y2==0):
		chi2 = 0
	elif(X2==0 and Y1==0 and Y2==0):
		chi2 = math.pow((a-X1),2)/X1
	elif(X1==0 and X2==0 and Y1==0):
		chi2 = math.pow((c-Y2),2)/Y2
	elif(X1==0 and Y1==0 and Y2==0):
		chi2 = math.pow((c-X2),2)/X2
	elif(X1==0 and X2==0):
		chi2 = math.pow((a-Y1),2)/Y1 + math.pow((c-Y2),2)/Y2
	elif(X1==0 and Y1==0):
		chi2 = math.pow((a-X2),2)/X2 + math.pow((b-Y2),2)/Y2
	elif(X1==0 and Y2==0):
		chi2 = math.pow((a-X2),2)/X2 + math.pow((d-Y1),2)/Y1
	elif(X2==0 and Y1==0):
		chi2 = math.pow((b-X1),2)/X1 + math.pow((c-Y2),2)/Y2
	elif(X2==0 and Y2==0):
		chi2 = math.pow((c-X1),2)/X1 + math.pow((d-Y1),2)/Y1
	elif(Y1==0 and Y2==0):
		chi2 = math.pow((b-X1),2)/X1 + math.pow((d-X2),2)/X2
	elif(X1==0):
		chi2 = math.pow((b-Y1),2)/Y1 + math.pow((c-X2),2)/X2 + math.pow((d-Y2),2)/Y2
	elif(X2==0):
		chi2 = math.pow((a-X1),2)/X1 + math.pow((b-Y1),2)/Y1 + math.pow((d-Y2),2)/Y2
	elif(Y1==0):
		chi2 = math.pow((a-X1),2)/X1 + math.pow((c-X2),2)/X2 + math.pow((d-Y2),2)/Y2
	elif(Y2==0):
		chi2 = math.pow((a-X1),2)/X1 + math.pow((b-Y1),2)/Y1 + math.pow((c-X2),2)/X2
	else:
		chi2 = math.pow((a-X1),2)/X1 + math.pow((b-Y1),2)/Y1 + math.pow((c-X2),2)/X2 + math.pow((d-Y2),2)/Y2
	return float(chi2)