#Filename: sort_files.py
#Description: This changes the file name so I can make assosiations
#Date: August 10, 2016
#Author: Heather Kurtz

from astropy.io import fits
import shutil
#to move fiels
import os
#to move files
import glob
#gets lots of files and gives their files names
from random import randint
import csv
import argparse

def correct_name_main(path):
#gets current directory
    base_path = path
 #   base_path = '/grp/hst/wfc3v/mmckay/internal_flats/tung3_raw/tung3_F200LP'
    
    os.chdir(path)
    
    name_new=[]
    old_name=[]
    name_matches=[]
    
    fileSB=open('name_matches.csv', 'r')
        
    for line in fileSB:
        q= [d for d in line.split(',')]
        old_name.append(q[0])
        name_new.append(q[1]) #reads second colom
    
    
    list_of_raw=glob.glob('*raw.fits')
    
    for i in range(len(list_of_raw)):
        #for num in setOfNumbers:
        File=list_of_raw[i]
        file=File[:9]
        for j in range(len(name_new)):
            name_comp=name_new[j]
            comp_name=name_comp[:9]
            if file==comp_name:
                curentName= os.path.join(base_path, File)
                name=File[9:]
                old=old_name[j]
                OLD=old[:9]
                file_name=OLD+name
                #check.append(file_name)
                name_matches.append((File,file_name))
                fileName= os.path.join(base_path, file_name)
                os.rename(curentName, fileName)
            else:
                continue
    
    list_of_flt=glob.glob('*flt.fits')
    
    for i in range(len(list_of_flt)):
        #for num in setOfNumbers:
        File=list_of_flt[i]
        file=File[:9]
        for j in range(len(name_new)):
            name_comp=name_new[j]
            comp_name=name_comp[:9]
            if file==comp_name:
                curentName= os.path.join(base_path, File)
                name=File[9:]
                old=old_name[j]
                OLD=old[:9]
                file_name=OLD+name
                #check.append(file_name)
                name_matches.append((File,file_name))
                fileName= os.path.join(base_path, file_name)
                os.rename(curentName, fileName)
            else:
                continue

    list_of_flc=glob.glob('*flc.fits')
    
    for i in range(len(list_of_flc)):
        #for num in setOfNumbers:
        File=list_of_flc[i]
        file=File[:9]
        for j in range(len(name_new)):
            name_comp=name_new[j]
            comp_name=name_comp[:9]
            if file==comp_name:
                curentName= os.path.join(base_path, File)
                name=File[9:]
                old=old_name[j]
                OLD=old[:9]
                file_name=OLD+name
                #check.append(file_name)
                name_matches.append((File,file_name))
                fileName= os.path.join(base_path, file_name)
                os.rename(curentName, fileName)
            else:
                continue

    list_of_tra=glob.glob('*.tra')
    
    for i in range(len(list_of_tra)):
        #for num in setOfNumbers:
        File=list_of_tra[i]
        file=File[:9]
        for j in range(len(name_new)):
            name_comp=name_new[j]
            comp_name=name_comp[:9]
            if file==comp_name:
                curentName= os.path.join(base_path, File)
                name=File[9:]
                old=old_name[j]
                OLD=old[:9]
                file_name=OLD+name
                #check.append(file_name)
                name_matches.append((File,file_name))
                fileName= os.path.join(base_path, file_name)
                os.rename(curentName, fileName)
            else:
                continue
    fileSB.close()
        
    with open('matches.csv','w') as out:
        csv_out=csv.writer(out)
        csv_out.writerow(['origanal','new'])
        for row in name_matches:
            csv_out.writerow(row)
            


def parse_args():
    """Parses command line arguments.

    Parameters:
        nothing

    Returns:
        args : argparse.Namespace object
            An argparse object containing all of the added arguments.

    Outputs:
        nothing
    """

    #Create help string:
    path_help = 'Path to the folder with files to run tweakreg.'
    
    # Add arguments:
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', '-path', dest = 'path', action = 'store',
                        type = str, required = True, help = path_help)

    # Parse args:
    args = parser.parse_args()

    return args
# -------------------------------------------------------------------
if __name__ == '__main__':
    args = parse_args()

    correct_name_main(args.path)


    
