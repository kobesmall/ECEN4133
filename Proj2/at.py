
import os, random, re, time, hashlib



#for i in range(1):
while(True):
    
    passwrd = ""
    for i in range(0,4):
        x = str(random.randint(0, 1000000))
        passwrd += x
        #print(x)
    md5s =  hashlib.md5(passwrd.encode()).digest()
    #print(md5s)

    if ( md5s.find(b"'='") != -1):
        print(md5s)
        print('\n\n Input password:   ' ,passwrd)
        
        break

