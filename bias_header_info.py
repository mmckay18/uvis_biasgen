#Created by Myles McKay

#Use
#python bias_header_info.py --path='./2010biasfiles/set2_2010/' --files='*raw.fits'




from astropy.io import fits
import numpy as np
import os
import glob
import argparse

def bias_header_info_main(path,files):

	os.chdir(path)
	list_of_files=glob.glob(files)
	flc_files = glob.glob('*flc.fits')
	flt_files = glob.glob('*_flt.fits')
	raw_files=glob.glob('*.fits')
	
	for image in list_of_files:
		hdu=fits.open(image)
		print(hdu[0].header['filename'],hdu[0].header['filter'],hdu[0].header['useafter'],hdu[0].header['detector']) #,hdu[0].header['targname']
		hdu.close()
	
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
    files_help = 'Type of files (*raw.fit,*flt.fits)'
    # Add arguments:
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', '-path', dest = 'path', action = 'store',
                        type = str, required = True, help = path_help)
    parser.add_argument('--files', '-files', dest = 'files', action = 'store',
    					type = str, required = True, help = files_help)
    # Parse args:
    args = parser.parse_args()

    return args
# -------------------------------------------------------------------
if __name__ == '__main__':
    args = parse_args()

    bias_header_info_main(args.path, args.files)	