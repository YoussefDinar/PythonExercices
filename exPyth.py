

# moyenne d'une collection de valeurs entrées#
L = []
i=0
val=1
while val!=0:
    if val!=0:
        val=float(input(f"Type a value {i+1} "))
        L.append(val)
        i=i+1
    else:
        break

somme=0
for k in L:
    somme+=k

Moy=somme/(i-1)
print(f"La moyenne : {Moy}")



         #BINAIRE EN DECIMAL#
def binaryToDec(n):
    return int(n,2)
print (binaryToDec('1100'))



 #TYPE DU TRIANGLE#

L1= float(input("Entrer la longueur 1 du triangle \n"))
L2= float(input("Entrer la longueur 2 du triangle \n"))
L3= float(input("Entrer la longueur 3 du triangle \n"))

if L1==L2 and L2==L3:
    print("Le triangle est equilatéral \n")
elif L1==L2 and L3!=L2 or L2==L3 and L1!=L2 or L1==L3 and L2!=L1:
    print("Le triangle est isocèle \n")
else:
    print("Le triangle est scalène \n")  



# DECIMAL EN BINAIRE #
def DecToBin(number):
        if number >= 1:
            DecToBin(number // 2)
            print (number % 2) 

DecToBin(12)

#Fonctions sur les listes des nombres#

def listInt():
    List = []
    while True:
     x = int(input())
     if not x:
            List1 = []
     for i in range(len(List)):
            List1.append(min(List))
            List.remove(min(List))
            return List1   
     else:
        List.append(x)

newL = listInt()
#print("insert values")
print(newL) 

#ispangram#
import string

def ispangram(str):
	alphabets = "abcdefghijklmnopqrstuvwxyz"
	for char in alphabets:
		if char not in str.lower():
			return False
	return True

string = 'The five boxing wizards jump quickly'
if(ispangram(string) == True):
	print("Yes it's a pangram")
else:
	print("No it's not a pangram")
          
   #datetime#	
import datetime
now = datetime.datetime.now()
print(now.year, now.month, now.day)	


#HEX2INT#
hex = input("Enter Hexadecimal Number: ")
 
c = count = i = 0
len = len(hex) - 1
while len>=0:
    if hex[len]>='0' and hex[len]<='9':
        x = int(hex[len])
    elif hex[len]>='A' and hex[len]<='F':
        x = ord(hex[len]) - 55
    elif hex[len]>='a' and hex[len]<='f':
        x = ord(hex[len]) - 87
    else:
        c = 1
        break
    count = count + (x * (16 ** i))
    len = len - 1
    i = i+1
 
if c == 0:
    print("\nDecimal Value = ", count)
else:
    print("\nerror!")


import random

def Rand_Password():
    Length = random.randint(7,10)
    s = ""
    for i in range(Length+1):
        j = random.randrange(33,126)
        s += chr(j)
    return s

print(Rand_Password())   

def GET_ALPHABET():
    S = ""
    for i in range(65,91):
        S += chr(i)
    return S


def Password_valide(Password):
    spech = "%#:$*"
    lowrc = GET_ALPHABET()
    uprc = GET_ALPHABET()
    if len(Password) >= 8:
        if lowrc in Password:
            if uprc in Password:
               if spech in Password:
                   return True
               else: return False 
            else: return False
        else: return False                           
    else: return False

print(Password_valide("JKAUKl0$Q"))



#CONVERT A NUMBER TO A BASE#
def DcToBase(x,Base):
    L = []
    while x!=0:
        L.insert(0,x%Base)
        x = x//Base
    return L    

def NumberBase(n,Base):
    if(Base ==16):
        L = DcToBase(n,Base)
        return L
    elif(Base == 2):
        L = DcToBase(n,Base)
        return L
    elif(Base ==8):
        L =  DcToBase(n,Base)   
        return L
    else:    
        return 'Error'
    
print(NumberBase(5658,2))
print(NumberBase(5658,8))
print(NumberBase(5658,16))
