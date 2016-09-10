import shutil
import glob
import os, sys

#Each directory used in this script will be different for each computer that this script runs on. Enter the corrects folders that correspond to your computer.

source = #this is the variable for the source of the documents
dest_leftovers = #variable for the leftover documents not added to anyones folder
dest_prem = #Priamwads box folder
dest_darin = #Darins box folder
dest_dom = #Dominics box folder
dest_josh = #Joshs box folder
dest_brendan= #Brendans box folder
dest_taylor = #Taylors box folder

list = glob.glob(source)
length = len(list)
leftovers = length%6

if(leftovers != 0):
    for x in xrange(0,leftovers):
    shutil.move(list[x],dest_leftovers)

list2 = glob.glob(source)
length2 = len(list2)

i = 0
j = 0

while i < length2:
    if(j == 0):
        shutil.move(list2[i],dest_prem)
        j = 1
        i = i + 1
    elif(j == 1):
        shutil.move(list2[i],dest_dom)
        j = 2
        i = i + 1
    elif(j == 2):
        shutil.move(list2[i],dest_darin)
        j = 3
        i = i + 1
    elif(j == 3):
        shutil.move(list2[i],dest_brendan)
        j = 4
        i = i + 1
    elif(j == 4):
        shutil.move(list2[i],dest_josh)
        j = 5
        i = i + 1
    elif(j == 5):
        shutil.move(list2[i],dest_taylor)
        j = 0
        i = i + 1