# DataQuality
update_metadata.py = Compare run number with a good run table and for the good run change the metadata of the file. This will make the query shorter and much faster to retrieve files from SAM.

calculate_lifetime_mine.py = Directly from SAM it retrieves the online subrun start and end time for each run in the  dataset definition and sum it to calculate the total livetime of the sample

make_draining_def.py = Compare two files containing files name. List 1 contains all the initial files, list 2 contains the files that have been sucessfully process from files in list1 (and maybe extra). Create two new lists, one with the unprocessed files one with the extra files

create_dataset_fromDrain.py = Starting from a list of files, interacts with SAMweb to create definition using those files and take a snapshot of the definition 
