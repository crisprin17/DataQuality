# DataQuality
update_metadata.py = Compare run number with a good run table and for the good run change the metadata of the file. This will make the query shorter and much faster to retrieve files from SAM.

calculate_lifetime_mine.py = Directly from SAM it retrieves the online subrun start and end time for each run in the  dataset definition and sum it to calculate the total livetime of the sample

make_draining_def.py = Compare two files containing files name. List 1 contains all the initial files, list 2 contains the files that have been sucessfully process from files in list1 (they may be duplicate and we don't want them). Create two new lists, one with the unprocessed files one with the extra files

create_dataset_fromDrain.py = Starting from a list of files, interacts with SAMweb to create definition using those files and take a snapshot of the definition 

create_combo_defSAM.py = same that create_dataset_fromDrain.py but in this case create combo definition

build_DQ_histograms.py = PYROOT script to check the quality of our data. Extract info on mean track lengths etc from root file and then compare the value of the data with their mediam value and write on an output files the run that dissociate from the media for more than two sigma. Those runs will be removed from our dataset
