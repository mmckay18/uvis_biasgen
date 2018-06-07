import numpy as np
#!/usr/bin/env python
from astropy.io import fits
import matplotlib.pyplot as plt
import glob
import matplotlib.patches as mpatches
import os
from multiprocessing import Pool
from wfc3tools import calwf3
from stsci.tools import teal
from random import randint
import csv
import shutil
from astropy.table import Table
import argparse


def make_scidq_hist_main(path):
    os.chdir(path)
    List1=[]
    List2=[]
    print ('Old Bias File Chip1 SCI Histograms')
    print('Name','         ','Chip','    ','Max','        ','Min','     ','Mean','        ','Std Dev' ,'    ','Median')
    for fitsName1 in glob.glob('*flt.fits'):
        fitsName1=np.array(fitsName1)
        fitsName1=np.append(List1,fitsName1)
        for i in range(len(fitsName1)):
            h = fits.open(fitsName1[i])
            sci_chip1=h[4].data
            dq_chip1=h[6].data
            sci_chip1[dq_chip1 !=0.0]=np.nan
            print(h[0].header['Rootname'],'   ','chip1','   ',np.nanmax(sci_chip1),'  ',np.nanmin(sci_chip1),'  ', np.nanmean(sci_chip1),'     ',np.nanstd(sci_chip1),'   ',np.nanmedian(sci_chip1))
            h.close()
            
            bins=np.linspace(0.0,4.0,50)
            n,bins,patches=plt.hist(sci_chip1[~np.isnan(sci_chip1)], 50, facecolor='g', alpha=0.50) 
           
            
            #Titles for the histogram
            plt.title("{} Chip1 SCI Histograms".format(h[0].header['filename']))
            plt.xlabel("Pixel Value")
            plt.ylabel("Frequency")
            plt.yscale('log')
            plt.annotate('Mean {} \nSigma {}'.format("%.3f" % np.nanmean(sci_chip1),"%.3f" %np.nanstd(sci_chip1)), xy=(225, 175), xycoords='axes points',
                        size=12, bbox=dict(boxstyle='round', fc='w'))
            plt.savefig('{}_chip1_scidq_hist.png'.format(h[0].header['Rootname']))
            plt.clf()
        #write_with_nan_c1_stats(filename='2009_521_bias_chip1_stats_DQ.txt')
          
            
            
    print('')
    print ('New Bias File Chip2 SCI Histograms')
    print('Name','         ','Chip','    ','Max','        ','Min','     ','Mean','        ','Std Dev' ,'    ','Median')
    for fitsName2 in glob.glob('*flt.fits'):
        fitsName2=np.array(fitsName2)
        fitsName2=np.append(List2,fitsName2)
        for i in range(len(fitsName2)):
            h = fits.open(fitsName2[i])
            sci_chip2=h[1].data
            dq_chip2=h[3].data
            sci_chip2[dq_chip2 !=0]=np.nan
            print(h[0].header['Rootname'],'   ','chip2','   ',np.nanmax(sci_chip2),'  ',np.nanmin(sci_chip2),'  ', np.nanmean(sci_chip2),'     ',np.nanstd(sci_chip2),'   ',np.nanmedian(sci_chip2))
            h.close()
            
            bins=np.linspace(0.0,4.0,50) 
            n,bins,patches=plt.hist(sci_chip2[~np.isnan(sci_chip2)], 50, facecolor='pink', alpha=0.50) 
            
            
            #Titles for the histogram
            plt.title("{} Chip2 SCI Histograms".format(h[0].header['filename']))
            plt.xlabel("Pixel Value")
            plt.ylabel("Frequency")
            plt.yscale('log')
            plt.annotate('Mean {} \nSigma {}'.format("%.3f" % np.nanmean(sci_chip2),"%.3f" %np.nanstd(sci_chip2)), xy=(225, 175), xycoords='axes points',
                        size=12, bbox=dict(boxstyle='round', fc='w'))
            plt.savefig('{}_chip2_scidq_hist.png'.format(h[0].header['Rootname']))
            plt.clf()
            

        #write_with_nan_c2_stats(filename='2009_521_bias_chip2_stats_DQ.txt')   
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

    make_scidq_hist_main(args.path)






