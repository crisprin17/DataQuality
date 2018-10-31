#!/usr/bin/env python                                                                                                                     \
                                                                                                                                           
import sys
import re

def print_usage():
    print "Usage: make_draining_def.py"

#open file and create a list of the part on string we are interested in                                                                    
def list1():
    onelist=[]
    with open("/nova/app/users/crisprin/python/NIGHT_files.txt","r+") as f1:
        for line1 in f1:
            one = str(line1.split('.')[0])
            onelist.append(one)
    f1.close()
    return onelist

#open file and create a list of the part on string we are interested in                                                                    
def list2():
    twolist=[]
    with open("/nova/app/users/crisprin/python/NIGHT_UPMU_clean.txt","r+") as f2:
        for line2 in f2:
            two = str(line2.split('.')[0])
            twolist.append(two)
    f2.close()
    return twolist
    
    #clean the files from directory and empty lines                                                                                            
with open("/nova/app/users/crisprin/python/NIGHT_UPMU.txt","r+") as d1, open("/nova/app/users/crisprin/python/NIGHT_UPMU_clean.txt","w") a\
s d2:
    for line in d1:
        if ('pnfs' not in line):
            if not line.strip(): continue
            d2.write(line)
d1.close()
d2.close()

#create a new list with files that are only in one of the two lists                                                                        
newlist=[]
a =set(list1())
b =set(list2())

ExtraFile = ( b.difference(a) )
Processed = filter(lambda x: x in a, b)
Non_Processed = a - set(Processed)

with open("/nova/app/users/crisprin/python/NIGHT_files_Non_Processed.txt","w") as g1:
    for line3 in Non_Processed:
        g1.write(line3+'.reco.root\n')
g1.close()

with open("/nova/app/users/crisprin/python/NIGHT_files_ExtraFiles.txt","w") as g2:
    for line4 in ExtraFile:
        g2.write(line4+'.reco.root\n')
g2.close()
