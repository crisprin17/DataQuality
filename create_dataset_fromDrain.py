#!/usr/bin/env python                                                                                                                                                    
import sys
import re
import samweb_client as swc

def print_usage():
    print "Usage: make_draining_def.py"

def listfiles():
    filelists = [[] for _ in range(100)]
    with open("TWILIGHT_files_Non_Processed.txt","r+") as f1:
        for i, line in enumerate(f1):
           filelists[i % 100].append(line)
    f1.close()
    return filelists

snapshotid = open("TWILIGHT_snapshotID.txt","w")

sam = swc.SAMWebClient("nova") 
for j in range (100):
    defname = 'crisprin_draining_dataset_TWILIGHT_'+str(j)+'_oct2018_new'
    dimension = " or ".join( ["file_name %s" % f for f in listfiles()[j] ] )  


    sam.createDefinition(defname, dimension)
    print "definition %s created" %defname
    print "taking a snapshot"
    snap = sam.takeSnapshot(defname)
    print "snapshot id %s" %snap
    snapshotid.write(str(defname)+'; snap ID'+str(snap)+'\n')

snapshotid.close()
