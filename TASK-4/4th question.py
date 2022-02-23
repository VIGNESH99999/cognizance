n=int(input("Choose number:"))
number=n
RE=0
while(n>0):
    when=n%10
    RE=RE*10+when
    n=n//10
if(number==RE):
    print("TRUE")
else:
    print("FALSE")