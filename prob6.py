n=eval(input("Introduceti un numar n="))
s1=0
s2=0
s3=1
s4=0
s5=0
s6=0
a=1
for i in range(1,n+1) :
    s1+=i
    s2+=(i-1)*1
    s3+=a
    s4+=i**2
    s5+=i/(i+1)
    s6+=i*2
    a*=i
print(s1,s2,s3-1,s4,s5,s6)
