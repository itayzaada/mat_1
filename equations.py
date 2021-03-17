def powe (x,y): 
    if y==0:
        num=1
    elif y<0:
        c=y
        c=c+1
        num=1/x
        while (c!=0):
            num=1/x*num
            c=c+1
    else :
        d=y
        d=d-1
        num=x
        while (d!=0):
            num=x*num
            d=d-1  
    return num

def atz (x):
        z=x
        num=1
        while(z>1):
            num=num*z
            z=z-1
        return num

def exponent (x):
    num=1
    for i in range (1,100):
        num=num+((powe(x,i))/atz(i))
    return num


def Ln(x):
    yn=0
    yn_1=x-1.0
    if x<=0:
        yn_1=0
    else:
        while (yn-yn_1>0.001) | (yn-yn_1<-0.001):
            yn=yn_1
            yn_1=yn+2*((x-exponent(yn_1))/(x+exponent(yn_1)))
    return yn_1

def XtimesY(x,y):
 try:
    if x<=0 :
        num=0
    elif x==1:
        num=1
    else :
        num=exponent(y*Ln(x))
 except :
     num=0
 return num

def sqrt (x,y) :
 try:
  if y <=0 :
      num=0
  elif y==1 :
      num=1 
  else :
      num=XtimesY(y,1/x)
 except:
     num=0
 return num

def calculate (x) :
    num=exponent(x)*XtimesY(7,x)*XtimesY(x,-1)*sqrt(x,x)
    num = float('%0.6f' % num)
    return num