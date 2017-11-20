# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 18:55:56 2017

@author: J.LI
"""

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
    row = row.replace(":","___")
    row = row.replace("    ",",",1)
    start = row.find("!")
    length = len(row)
    p = row[start:length-1]
    if start > 0:
        row = row.replace(p,"")
        row = row.replace(",",'"'+p+'":"',1)
    row = row.replace("!-","").replace("{","(").replace("}",")") 
    if row[0] != "!":
        t3.write(row)
t2.close()
t3.close()

#replace computerphobe 
t4 = open("t3.txt","r")
t5 = open("t5.txt","w")
for row in t4.readlines():
    row = row.replace(",                        ","Null,")
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
    if len(row) > 1:
        t5.write(row)
t4.close()
t5.close()

t6 = open("t5.txt","r")
t7 = open("t7.txt","w")
alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
for row in t6.readlines():
    if row[0] != '"':
        row = row.replace(",",'":"',1)
    m = len(row)
    if row[m-2:m-1] == '"' :
        if row.count(':') == 1: 
            row = row.replace(':"\n',':{')
    row = row.replace(':"\n',',').replace(',\n','",')
    row = row.replace(";",'",')
    count = row.count('\\')
    if count > 1:
        row = row.replace('\\',"BACKSLASH")
    if row[0] == '_':
        row = row.replace('_','"_',1)
    t7.write(row)
t6.close()
t7.close()

#transform to json
t8 = open("t7.txt","r")
t9 = open("t9.txt","w")
for row in t8.readlines():
    n = row.count(':')
    if n >= 2:
        row = row.replace(',\n','},')
    row = row.replace(',\n',',')
    t9.write(row)
t8.close()
t9.close() 

#transform to json
t10 = open("t9.txt","r").read()
t11 = open("t11.txt","w")   
t12 = t10.replace('"','{"',1)
t12 = t12[::-1]
t12 = t12.replace(",","}",1)
t12 = t12[::-1]
t11.write(t12)
t11.close()

#create json file
IDF2JSON = source.replace("idf","json")
if os.path.exists(IDF2JSON) == True:
    os.remove(IDF2JSON)
    os.rename("t11.txt",IDF2JSON)
else:
    os.rename("t11.txt",IDF2JSON)
print("IDF2JSON Complete.")

#remove temp files  
os.remove("t1.txt")
os.remove("t3.txt")
os.remove("t5.txt")
#os.remove("t7.txt")
#os.remove("t9.txt")


