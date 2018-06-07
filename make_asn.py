#Filename: make_asn.py
#Description: This creates associations between images and the association file that accompanies that.
#Date: August 4, 2016
#Author: Heather Kurtz with ASN writing help from Matthew Bourque

from astropy.io import fits
import numpy as np
import glob
from astropy.table import Table
import argparse
import os
from wfc3tools import calwf3



def make_asn_main(path):
    files_wo_asn=[]
    files_con_asn=[]
    asns=[]
    obs=[]
    
    
    os.chdir(path)
    #uses the vists to set new associations
    visits=[]
    list_of_files=glob.glob('*raw.fits')
    for files in list_of_files:
        name=files
        visit=name[:6]
        visits.append(visit)
        hdu=fits.open(files, mode='update')
        hdu[0].header['PCTECORR'] = 'OMIT'
        hdu.close()

    unique_visits= set(visits)
    obs_date=[]
    print (unique_visits)
    for items in unique_visits:
        asn_files=[]
        for j in range(len(list_of_files)):
            files=list_of_files[j]
            comp=files[:6]
            write_file=files[:9]
            if items==comp:
                asn_files.append(write_file)
                output=files[:6]+'010_asn.fits'
                files=files
            else:
                continue
                
        if len(asn_files)>1:
            row = [i+1 for i in range(len(asn_files))]
            memtype = ['EXP-CRJ' for f in asn_files]
            memprsnt = [True for f in asn_files]
            xoffset = [0. for f in asn_files]
            yoffset = [0. for f in asn_files]
            xdelta = [0. for f in asn_files]
            ydelta = [0. for f in asn_files]
            rotation = [0. for f in asn_files]
            scale = [1. for f in asn_files]
            # Change the last row to have a memtype of PROD-CRJ instead of EXP-CRJ
            #memtype[-1] = 'PROD-CRJ'
    	
            # Build the table
            columns = [row, asn_files, memtype, memprsnt, xoffset, yoffset, xdelta, ydelta, rotation, scale]
            names = ['row', 'MEMNAME', 'MEMTYPE', 'MEMPRSNT', 'XOFFSET', 'YOFFSET', 'XDELTA', 'YDELTA', 'ROTATION', 'SCALE']
            asn_table = Table(columns, names=names)
            
            # Save the table to a FITS file
            asn_table.write(output)
            
            # Update header to have required keywords
            hdulist = fits.open(output, mode='update')
            hdulist[0].header['INSTRUME'] = 'WFC3'
            hdulist[0].header['DETECTOR'] = 'UVIS'
            hdulist[0].header['PCTECORR'] = 'OMIT'
            hdulist.close()
            
        else:
            continue
    
    calwf3(output)



#
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

    make_asn_main(args.path)
