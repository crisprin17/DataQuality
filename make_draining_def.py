#!/usr/bin/env python                                                                                                                                                    
import sys
import re
import collections
def print_usage():
    print "Usage: make_draining_def.py"

#open file and create a list of the part on string we are interested in
def list1():
    onelist=[]
    with open("/nova/app/users/crisprin/python/TWILIGHT_files.txt","r+") as f1:
        for line1 in f1:
            one = str(line1.split('_S')[0])
            onelist.append(one)
    f1.close()
    return onelist

#open file and create a list of the part on string we are interested in 
def list2():
    twolist=[]
    with open("/nova/app/users/crisprin/python/TWILIGHT_UPMU_clean.txt","r+") as f2:
        for line2 in f2:
            two = str(line2.split('_S')[0])
            twolist.append(two)
    f2.close()
    return twolist

#clean the files from directory and empty lines
with open("/nova/app/users/crisprin/python/TWILIGHT_UPMU.txt","r+") as d1, open("/nova/app/users/crisprin/python/TWILIGHT_UPMU_clean.txt","w") as d2:
    for line in d1:
        if ('pnfs' not in line):
            if not line.strip(): continue
            d2.write(line)
d1.close()
d2.close()




#create a new list with files that are only in one of the two lists
a =set(list1())
b = list1()
Ndup = len(b) - len(a)
print "Number of files in the definition:"+str(len(b))
print "Number of files in the definition withouth duplicates:"+str(len(a))
print "Number of duplicate"+str(Ndup)
Duplicate = [item for item, count in collections.Counter(b).items() if count > 1]
c =set(list2())
print "Number UPMU files in folder"+str(len(c))
ExtraFile = [x for x in c if x not in a]
print "Number of extra files in UPMU folder:"+str(len(ExtraFile))
print len(set(ExtraFile))
print ExtraFile
Process = [x for x in b if x in c ]
print "Number of succesfully processed files with duplicates:"+str(len(Process))
Processed = (set(Process))
print "Number of succesfully processed files without duplicates:"+str(len(Processed))
Non_Processed = [x for x in b if x not in c]
print "Number of non processed files with duplicate"+str(len(Non_Processed))
print "Number of non processed files without duplicate"+str(len(set(Non_Processed)))



with open("/nova/app/users/crisprin/python/TWILIGHT_files_Non_Processed.txt","w") as g1:
    for line3 in Non_Processed:
        g1.write(line3+'_S17-10-30_v1_data.reco.root\n')
g1.close()

with open("/nova/app/users/crisprin/python/TWILIGHT_files_ExtraFiles.txt","w") as g2:
    for line4 in ExtraFile:
        g2.write(line4+'_S17-10-30_v1_data.reco.root\n')
g2.close()

with open("/nova/app/users/crisprin/python/TWILIGHT_files_Duplicate.txt","w") as g3:
    for line5 in Duplicate:
        g3.write(line5+'_S17-10-30_v1_data.reco.root\n')
g2.close()
