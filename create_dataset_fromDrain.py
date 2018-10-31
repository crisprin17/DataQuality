!/usr/bin/env python                                                                                         \
                                                                                                               
import sys
import re
import samweb_client as swc

def print_usage():
    print "Usage: make_draining_def.py"

def listfiles():
    filelist=[]
    with open("NIGHT_draining_dataset.txt","r+") as f1:
        for line in f1:
            filelist.append(line)
    f1.close()
    return filelist

sam = swc.SAMWebClient("nova")

#sam.createDefinition()                                                                                        
defname = 'crisprin_draining_dataset_night_oct2018'
dimension = " or ".join( ["file_name %s" % f for f in listfiles()])

sam.createDefinition(defname, dimension)
print "definition %s created" %defname
print "taking a snapshot"
snap = sam.takeSnapshot(defname)
print "snapshot id %s" %snap
