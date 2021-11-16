from numpy import float64, int64


solved=False
x=float64(-10) 
while solved==False or x<10:
    if (4**x)*5**(4*x+3)==10**(2*x+3):
        print("THE ASNWER IS")
        print(x)
        solved=True
    else:
        x+=0.1

print("fag")
