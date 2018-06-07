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

def rename_files_main(path):
    #current = os.getcwd()
    #gets current directory
    
    #base_path = '/grp/hst/wfc3v/mmckay/internal_flats/tung3_files/tung3_F200LP/TEST'
    
    #os.chdir(base_path)
    os.chdir(path)
    base_path = path
    name_matches=[]
    check=[]
    number=[]
    
    setOfNumbers=set()
    while len(setOfNumbers) < 600:
        setOfNumbers.add(str(randint(111,999)))
    
    my_list=list(setOfNumbers)
    
    #for i in range(106):
     #   num=randint(102,999)
      #  nums=str(num)
       # number.append(nums)
    
    list_of_files=glob.glob('*raw.fits')
    
    for i in range(len(list_of_files)):
        #for num in setOfNumbers:
        
        files=list_of_files[i]
        curentName= os.path.join(base_path, files)
        name=files[9:]
        num=my_list[i]
        new_name='imam11'+num+name
        check.append(new_name)
        name_matches.append((files,new_name))
        fileName= os.path.join(base_path, new_name)
        os.rename(curentName, fileName)
    
       
    with open('name_matches.csv','w') as out:
        csv_out=csv.writer(out)
        csv_out.writerow(['origanal','new'])
        for row in name_matches:
            csv_out.writerow(row)
                
    
    
    
    #os.chdir(current)
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

    rename_files_main(args.path)
