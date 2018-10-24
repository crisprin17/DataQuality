#!/usr/bin/env python

#python update_metadata.py --dataset=rcg_DDUpMu_Full_reco --offset=0 --limit=10

import sys
import math
#import ephem
from datetime import datetime
#from pytz import timezone
#import pytz
import samweb_client as swc
from optparse import OptionParser
from time import gmtime, strftime, time
import csv

ti=time()   
start_time=strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())   


DEFAULT_DEL_T=160

############################################################
# Setup the commandline parsing
version = "1.0"
usage = "usage: %prog [options]"
parser= OptionParser(usage=usage,version=version)

parser.add_option("-d","--dataset", dest="dataset", default="", help="Name of the SAM dataset to update")
parser.add_option("-o","--offset", dest="offset", default=0,  help="Offset into the dataset")
parser.add_option("-l","--limit",  dest="limit",  default=-1, help="Limit on number of files to process")
(options,args)=parser.parse_args()

# First get the list of files that match the pattern
sam = swc.SAMWebClient("nova")
# This line sets the role as high as possible (i.e. admin) if you have permissions
sam.role = '*'

############################################################
# Setup the SAM Dimesions for the data catalog queries
#runRange = '( run_number > 21000 and run_number < 21350 ) '
#runRange = '( run_number > 21000 and run_number < 21050 ) '
#dataTiers = '(data_tier pid or data_tier pidpart) '
#allTiers = ''
#numiStream = 'data_stream 0 '
#cosmicStream = 'data_stream 2 '
#sunmoonStream = '(data_stream ddmoon or data_stream ddsun) '
#upmuStream = '(data_stream upmuStream) '
snap='dataset_def_name_newest_snapshot '

# Set the offset and file limit to use into the snapshot or
# dataset this constructs the correct string that can be tacked on
# the dimensions string
offset=''
if (options.offset > 0) & (options.limit > 0) :
    offset = ' with offset %s limit %s'%(options.offset, options.limit)
    print offset
    print '*'*80

# Setup the List of dimensions that we will querey against    
if (options.dataset) :
    # User has specified something on the command line.  Use it.
    DIMList = [ snap + options.dataset + offset ]
#	DIMList = [ snap + options.dataset +' and defname:isgood_fd_prod4'+ offset ]
else:
    # Nothing was specified on the commandline so we instead use a preconstructed list
    # which may contain multiple datasets
    #
    # Construct a list of the definitions to run
    # in particular use the a snap shot of each one (assuming it exists)
    # to do this we put the magic string for use the latest snapshot in front of the dataset name
    DIMList = [ 
          snap +'rcg_DDUpMu_Full_reco'+offset
        ]

print DIMList
    
def is_prime(candidate):
    with open('goodRuns4SAM.csv','rb') as csvfile:
        for row in csv.reader(csvfile, delimiter = ','):
            if candidate in range(int(row[0]),int(row[2])+1):
#                print 'True for (%s) in range((%s),(%s))'%(candidate,row[0],row[2])
                return True
        return False


###################################################################
#
# Now for each file let's get the current metadata record
# and and record the livetime

# flist = ['fardet_r00021057_s01_DDMoon.raw']

# Open a file that we can put a cache into
# cachefile = open('filelist.cache','w')

# Loop over each of the defined SAM Dataset Dimesions
for theDIM in DIMList:
   # Determine the file list associated with the dimension
   #flist=sam.listFiles(defname=theDIM)
   flist=sam.listFiles(theDIM)
   todolist = flist
   nFiles = (len(flist))


   # Create a Report for the dimesion
   print '*'*60
   print '* Dim: %s' % (theDIM) 
   print "* %d files matching." % (nFiles)
   print '*'*60
   print '*'*60
   print '\n'


   count = 0
   count_errors=0
#   for f in flist :
#       cachefile.write(todolist)
#   cachfile.write('********************************')


   sum=0		
   for f in flist :
         count += 1
         # Get the metadata record for the file
         try:
           md=sam.getMetadata(f)
         except:
           print "Error: Unable to retrieve metadata for file (%s)"%(f)


         #print f		   
		 
         #This does not work because the gr information is stored in external database		   		 
         #novagr_ngood_tot_diblock = md['novagr_ngood_tot_diblock']
         #print "novagr:",novagr_ngood_tot_diblock

         try:
         #if 1:
           # We have the metadata for the file.  So we need to pull off the Sun position

             run        = md['Online.RunNumber']
             subrun  	  = md['Online.Subrun']
             start_t = md['Online.SubRunStartTime']
             end_t   = md['Online.SubRunEndTime']
             
             SunEnd=md['Analysis.SunPositionEnd']
             SunStart=md['Analysis.SunPositionStart']
             
#		   print "Start:",  SunStart
#		   print "End:",  SunEnd
             del_t=int(end_t)-int(start_t)
             if abs(del_t)>400:
			  #We should probably count these
                 print "!!! GREATER THAN 400s, %d setting to 160" %del_t
                 del_t=DEFAULT_DEL_T
                 count_errors+=1
                 
                 sum+=del_t
                 
                 
             AnalysisSelection=""
             
             if (SunStart=="BelowHorizon10" or SunStart=="BelowHorizon15"  or SunStart=="BelowHorizon20"):
		   	  #print "BELOW!"
                 AnalysisSelection="Night"
             
             if (SunStart=="AboveHorizon10" or SunStart=="AboveHorizon15" or SunStart=="AboveHorizon20"):
		   	  #print "ABOVE!"
                 AnalysisSelection="Day"		

             if (SunStart=="HorizonZone"):
		   	  #print "HORIZON!"
                 AnalysisSelection="Twilight"		

             res = is_prime(int(run))
             if (res == True):
                 newmetadata = {}
                 newmetadata['Upmu.AnalysisSelection']=AnalysisSelection
                 sam.modifyFileMetadata(f,newmetadata)			  


                 out_string="%s %s %s %s %s %d" %(run,subrun,AnalysisSelection,start_t,end_t,del_t)
                 print out_string

		   
         except Exception: 
           # There was some problem in updating the file.  Write out the file we had the problem with
             print "*"*20
             print "Unable to read metadata for: %s" %(f)
           # raise


         if count%100==0:  
             sys.stdout.write("\r%d of %d\n" %(count,nFiles)) 
             sys.stdout.flush()
                 
                 


   end_time=strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
   tf=time()
   t_diff=tf-ti

   print "\n start:",start_time
   print "end:",end_time
   print "seconds:%2.2f   avg:%2.2f" %(t_diff,t_diff/count)
   print "%d files with bad delta t, set to default (%d s)" %(count_errors,DEFAULT_DEL_T)



