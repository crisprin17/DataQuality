#!/usr/bin/env python                                                                                                                                                    
import sys
import re
import samweb_client as swc

def print_usage():
    print "Usage: make_draining_def.py"

def listfiles():
    filelists = [[] for _ in range(10)]
    with open("TWILIGHT_snapshotID.txt","r+") as f1:
        for i, line in enumerate(f1):
            data = str(line.split(';')[0])
            filelists[i % 10].append(data)
    f1.close()
    return filelists

snapshotid = open("TWILIGHT_combo_snapshotID.txt","w")

sam = swc.SAMWebClient("nova") 
for j in range (10):
    defname ="crisprin_TWILIGHT_draining_"+str(j)+"batch_oct2018_new"     
    dimension =" or ".join( ["dataset_def_name_newest_snapshot %s" % f for f in listfiles()[j] ] )


    sam.createDefinition(defname, dimension)
    print "definition %s created" %defname
    print "taking a snapshot"
    snap = sam.takeSnapshot(defname)
    print "snapshot id %s" %snap
    snapshotid.write(str(defname)+'; snap ID'+str(snap)+'\n')

snapshotid.close()
