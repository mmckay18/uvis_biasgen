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
from astropy.table import Table
import datetime as DT
import matplotlib.dates as dates
import parser
import pandas as pd
import skimage.morphology as morph
from skimage.morphology import disk
import argparse






def store_data_main(file):
	file_mean1=[]
	file_mean2=[]
	file_date=[]
	file_mean1_top=[]
	file_mean1_bottom=[]
	file_mean2_top=[]
	file_mean2_bottom=[]

	for im in files:
	    h = fits.open(im)
	    sci_chip1=h[4].data
	    sci_chip2=h[1].data
	    dq_chip1=h[6].data
	    dq_chip2=h[3].data
	    
	    sci_chip1[dq_chip1 !=0]=np.nan
	    sci_chip2[dq_chip2 !=0]=np.nan
	    
	    sci_chip1_top=sci_chip1[1500:1900,:]
	    sci_chip1_bottom=sci_chip1[100:500,:]
	    sci_chip2_top=sci_chip2[1500:1900,:]
	    sci_chip2_bottom=sci_chip2[100:500,:]
	    
	    date=h[0].header['date-obs']
	    file_date=np.append(file_date,date)
	    file_mean1=np.append(file_mean1,np.nanmean(sci_chip1))
	    file_mean2=np.append(file_mean2,np.nanmean(sci_chip2))
	    
	    file_mean1_top=np.append(file_mean1_top,np.nanmean(sci_chip1_top))
	    file_mean1_bottom=np.append(file_mean1_bottom,np.nanmean(sci_chip1_bottom))
	    
	    file_mean2_top=np.append(file_mean2_top,np.nanmean(sci_chip2_top))
	    file_mean2_bottom=np.append(file_mean2_bottom,np.nanmean(sci_chip2_bottom))


	file_date = [pd.to_datetime(d,format='%Y-%m-%d') for d in file_date]
	Mean_c1=np.mean(file_mean1)
	STD_c1 =np.std(file_mean1)
	Mean_c1_top=np.mean(file_mean1_top)
	Mean_c1_bottom=np.mean(file_mean1_bottom)
	Mean_c2=np.mean(file_mean2)
	STD_c2 =np.std(file_mean2)
	Mean_c2_top=np.mean(file_mean2_top)
	Mean_c2_bottom=np.mean(file_mean2_bottom)
	#plt.scatter(file_date,file_mean1)
	chip1_upper_region =plt.scatter(file_date,file_mean1_top,color='green')
	chip1_lower_region =plt.scatter(file_date,file_mean1_bottom,color='red')
	chip1_total_average=plt.axhline(y=Mean_c1,linewidth=1, color='black')
	chip1_upper_average=plt.axhline(y=Mean_c1_top,linewidth=3, color='green')
	chip1_lower_average=plt.axhline(y=Mean_c1_bottom,linewidth=3, color='red')
	plt.ylim(-0.25,0.5)
	plt.xlabel('Date-Obs')
	plt.ylabel('Mean Values')
	plt.title(' Chip1 statistics \n Mean of mean values: {}  Std.Dev of mean Values: {}'.format("%.3f" %Mean_c1, "%.3f" %STD_c1))
	plt.xticks(rotation=30)
	plt.legend((chip1_upper_region,chip1_lower_region,chip1_total_average,chip1_upper_average,chip1_lower_average),
	           ('Upper region', 'Lower region','Total Average','Upper Region Average', 'Lower Region Average'),
	           scatterpoints=1,
	           loc='lower left',
	           ncol=2,
	           fontsize=8)
	#plt.savefig('Statistics chip1 data plot.png')
	#plt.show()
	#plt.clf()
	plt.scatter(file_date,file_mean2)
	chip2_upper_region =plt.scatter(file_date,file_mean2_top,color='red')
	chip2_lower_region =plt.scatter(file_date,file_mean2_bottom,color='green')
	chip2_total_average=plt.axhline(y=Mean_c2, xmin=-100,xmax=100,linewidth=1, color='black')
	chip2_upper_average=plt.axhline(y=Mean_c2_top, xmin=-100,xmax=100,linewidth=3, color='red')
	chip2_lower_average=plt.axhline(y=Mean_c2_bottom, xmin=-100,xmax=100,linewidth=3, color='green')
	plt.ylim(-0.3,0.4)
	plt.xlabel('Date-Obs')
	plt.ylabel('Mean Values')
	plt.title(' Chip2 statistics\n Mean of mean values: {}  Std.Dev of mean Values: {}'.format("%.3f" %Mean_c2, "%.3f" %STD_c2))
	plt.xticks(rotation=30)
	plt.legend((chip2_upper_region,chip2_lower_region,chip2_total_average,chip2_upper_average,chip2_lower_average),
	           ('Upper region', 'Lower region','Total Average','Upper Region Average', 'Lower Region Average'),
	           scatterpoints=1,
	           loc='lower left',
	           ncol=2,
	           fontsize=8)
	plt.savefig('Statistics chip2 data plot.png')
	#plt.show()
	#plt.clf()    
	













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
    os.chdir(args.path)
    os.system('pwd')
    files=glob.glob('*flt.fits')
    p=Pool(5)
    p.map(store_data_main,files)










