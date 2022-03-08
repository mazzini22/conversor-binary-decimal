print ('welcome to my humble conversor binary to decimal\n')
print ('type the digits in binary (right to left)\n') 

b1 =int( input ())
if b1== 1:
  b1 = 1
else:
    b1 = 0
  
b2=int( input ())
if b2==1:
    b2 = 2
else:
    b2 = 0

b3=int( input ())
if b3==1:
    b3 = 4
else:
    b3 = 0
b4=int( input ())
if b4==1:
    b4 = 8
else:
    b4 = 0
b5=int( input ())
if b5==1:
    b5 = 16
else:
    b5 = 0   

b6=int( input ())
if b6==1:
    b6 = 32
else:
    b7 = 0
b7=int( input ())
if b7==1:
    b7 = 64
else:
    b7 = 0
    
print('the decimal number is: ',b1+b2+b3+b4+b5+b6+b7)