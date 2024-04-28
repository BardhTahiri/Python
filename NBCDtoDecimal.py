```py
nbcd = {
    0:"0000",
    1:"0001",
    2:"0010",
    3:"0011",
    4:"0100",
    5:"0101",
    6:"0110",
    7:"0111",
    8:"1000",
    9:"1001"
    
}
NBCD = {
"0001":1,
"0010":2,
"0011":3,
"0100":4,
"0101":5,
"0110":6,
"0111":7,
"1000":8,
"1001":9
}
KODI5421 = {
    "0001":1,
    "0010":2,
    "0011":3,
    "0100":4,
    "1000":5,
    "1001":6,
    "0111":7,
    "1011":8,
    "1100":9
}
XS3 = {
    "0100":1,
    "0101":2,
    "0110":3,
    "0111":4,
    "1000":5,
    "1001":6,
    "1010":7,
    "1011":8,
    "1100":9
}
lst = []
def konvertimi_ne_binar(n):
   if n > 1:
       konvertimi_ne_binar(n//2)
   print(n % 2,end = '')
   
print ("Mirsevini ne programin e kodimit dhe dekodimit.!") 
a=int(input("Zgjedh nese doni te kodoni apo dekodoni. 1 [Kodo]; 2 [Dekodo]:")) 
if a == 1:
    nrdecimal=int(input(("Shkruani numrin decimal 4 shifror qe doni te kodoni:")))
    lst.append(nrdecimal)
    output = list(map(int, str(lst[0])))
    zgjedhjanr1=int(input(("Zgjedh kodin ne te cilin doni ta kodoni numrin decimal: 1 [NBCD]; 2 [8421] 3 [Numer heksadecimal] :")))
    if zgjedhjanr1 ==1:
        print(nbcd[output[0]] + " " + nbcd[output[1]] + " " + nbcd[output[2]] + " " + nbcd[output[3]])
    elif zgjedhjanr1 ==2:
        konvertimi_ne_binar(nrdecimal)
        print()
    else:
        print(hex(nrdecimal))
else:
     z2=int(input("Zgjedhni cilin kod do te dekodoni. 1 [NBCD]; 2 [5421]; 3 [XS3]:"))
if z2 ==1:
    print("Shkruani numrin ne NBCD:")
    nr1=input()
    nr2=input()
    nr3=input()
    nr4=input()
    print("Numri decimal eshte:")
    print(str(NBCD[nr1]) + str(NBCD[nr2]) + str(NBCD[nr3]) + str(NBCD[nr4]))
elif z2 ==2:
    print("Shkruani numrin ne [5421]:")
    nr1=input()
    nr2=input()
    nr3=input()
    nr4=input()
    print("Numri decimal eshte:")
    print(str(KODI5421[nr1]) + str(KODI5421[nr2]) + str(KODI5421[nr3]) + str(KODI5421[nr4]))
else:
    print("Shkruani numrin ne XS3:")
    nr1=input()
    nr2=input()
    nr3=input()
    nr4=input()
    print("Numri decimal eshte:")
    print(str(XS3[nr1]) + str(XS3[nr2]) + str(XS3[nr3]) + str(XS3[nr4]))
```
