# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 14:17:24 2017

@author: J.LI
"""

import os

#Part 1 
#IDF2JSON
#load file and remove head comments 
source = '1ZoneUncontrolled_win_1.idf'
idf_file = open(source)
t1 = open("t1.txt","w")
for row in idf_file.readlines():
    if row[0] == "!":
        row = row
    else:
        t1.write(row)
t1.close()

t2 = open("t1.txt","r")
t3 = open("t3.txt","w")
for row in t2.readlines():
    row = row.replace("!","\n-")
    t3.write(row)
t2.close()
t3.close()

t4 = open("t3.txt","r")
t5 = open("t5.txt","w")
for row in t4.readlines():
    if row[0] == "-":
        row = row
    else:
        t5.write(row)
t5.close()
t4.close()

#replace computerphobe 
t6 = open("t5.txt","r")
t7 = open("t7.txt","w")
for row in t6.readlines():
    row = row.replace(",                        ","Null,                    ")
    row = row.replace('  ','_',2)    
    index1 = row.rfind(",")
    index2 = row.rfind(";")
    length = len(row)
    if index1 > index2:
        blank1 = row[index1+1:length-1]        
        row = row.replace(blank1,"")
    else:
        blank2 = row[index2+1:length-1]
        row = row.replace(blank2,"")
    row = row.replace(",\n",",_")
    row = row.replace(":","___")
    if len(row) > 1:
        t7.write(row)
t6.close()
t7.close()

t8 = open("t7.txt","r")
t9 = open("t9.txt","w")
alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
for row in t8.readlines():    
    index = row.find(",")
    if row[index-1:index] in alphabet:
        row = row.replace(",",'":"',1)
    row = row.replace(";",'",')
    row = row.replace("_",'"',1)
    count = row.count('\\')
    if count > 1:
        row = row.replace('\\',"BACKSLASH")
    t9.write(row)
t8.close()
t9.close()

#transform to json
t10 = open("t9.txt","r")
t11 = open("t11.txt","w")
t12 = t10.read()
t13 = t12.replace('"','{"',1)
t13 = t13[::-1]
t13 = t13.replace(",","}",1)
t13 = t13[::-1]
t13 = t13.replace(",\n",",")
t11.write(t13)
t10.close()
t11.close()

#create json file
IDF2JSON = source.replace("idf","json")
if os.path.exists(IDF2JSON) == True:
    os.remove(IDF2JSON)
    os.rename("t11.txt",IDF2JSON)
else:
    os.rename("t11.txt",IDF2JSON)
print("IDF2JSON Complete.")

#Part 2
#transform json to idf
#load file
b1 = open(IDF2JSON,"r").read()
IDF2JSON_back = source.replace(".idf","_IDF2JSON_back.idf")
b2 = open("b2.txt","w")
b1 = b1.replace('{"','"',1)
b1 = b1[::-1]
b1 = b1.replace("}",",",1)
b1 = b1[::-1]
b1 = b1.replace('",','",\n')
b2.write(b1)
b2.close()

b3 = open("b2.txt","r")
b4 = open("b4.txt","w")
for row in b3.readlines():
    row = row.replace("BACKSLASH",'\\')
    row = row.replace('"','_',1)
    row = row.replace('",',';')
    row = row.replace('":"',",",1)
    row = row.replace(",_",",\n")
    row = row.replace("___",":")
    row = row.replace('_','  ')
    row = row.replace("Null,",",")
    b4.write(row)
b3.close()
b4.close()
#create IDF2JSON_back file
if os.path.exists(IDF2JSON_back) == True:
    os.remove(IDF2JSON_back)
    os.rename("b4.txt",IDF2JSON_back)
else:
    os.rename("b4.txt",IDF2JSON_back)
print("IDF2JSON_back Complete.")

#remove temp files  
os.remove("t1.txt")
os.remove("t3.txt")
os.remove("t5.txt")
os.remove("t7.txt")
os.remove("t9.txt")
os.remove("b2.txt")


