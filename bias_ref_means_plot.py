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
##%matplotlib inline 
import datetime as DT
import matplotlib.dates as dates
import parser
import pandas as pd
import skimage.morphology as morph
from skimage.morphology import disk
import matplotlib.dates as mdates
from astropy.table import Table, Column
from multiprocessing import Pool
import time


os.chdir('/grp/hst/wfc3r/mmckay/Final_full_frame_reference_files/')
#os.chdir('/grp/hst/wfc3r/mmckay/all_current_bias_ref_files_aug2017/')

list=sorted(glob.glob('*.fits')) 
file_mean1=[]
file_mean2=[]
file_date=[]
file_stddev1=[]
file_stddev2=[]
table_file_date=[]
#Number_of_files=[494,492,524,347,246,219,52,52,53]
for im in list:
    h = fits.open(im)
    sci_chip1=h[4].data
    sci_chip2=h[1].data
    dq_chip1=h[6].data
    dq_chip2=h[3].data
    
#    sci_chip1[dq_chip1 !=0]=np.nan
#    sci_chip2[dq_chip2 !=0]=np.nan
    date=h[0].header['useafter']
#    print(date[:11])
    date1=date[:11]
    sci_chip1 = sci_chip1 * 1.5
    sci_chip2 = sci_chip2 * 1.5
    file_date=np.append(file_date,date1)
    file_mean1=np.append(file_mean1,np.nanmean(sci_chip1))
    file_mean2=np.append(file_mean2,np.nanmean(sci_chip2))
    file_stddev1=np.append(file_stddev1,np.nanstd(sci_chip1))
    file_stddev2=np.append(file_stddev2,np.nanstd(sci_chip2))
    
#astropy table lists    
    table_date=date[6:11]
#    print(table_date)
    table_file_date = np.append(table_file_date, table_date)
#---------------------------------------------------------    
    file_date = [pd.to_datetime(d,format=None) for d in file_date]

    Mean_c1=np.mean(file_mean1)
    STD_c1 =np.std(file_mean1)
    
    Mean_c2=np.mean(file_mean2)
    STD_c2 =np.std(file_mean2)   
    
file_date = [pd.to_datetime(d,format='%Y-%m-%d') for d in file_date]
x = mdates.date2num(file_date)
print(file_stddev1)
print(file_mean1)
print(file_stddev2)
print(file_mean2)
polyfit1=np.polyfit(x,file_mean1,1)
polyfit1_data=((polyfit1[0]*x + polyfit1[1]))

plt.plot(x, polyfit1_data,'orange',linewidth=3)
plt.scatter(file_date,file_mean1)
plt.errorbar(file_date,file_mean1,yerr=file_stddev1,capsize=5, fmt='none')
plt.axhline(y=0, xmin=-100,xmax=100,linewidth=2, color='blue')
plt.xlabel('Year')
plt.ylabel('Mean Values (Electrons)')
plt.ylim(-1,1)
plt.title('2009-2016 Superbias(Ext4) Date-obs vs. Mean Value \n Overall Mean: {} e- Std.Dev: {} e-'.format("%.3f" %Mean_c1, "%.3f" %STD_c1))
plt.xticks(rotation=30)
plt.savefig('Statistics chip1 data plot.png')
plt.show()
plt.clf()

polyfit2=np.polyfit(x,file_mean2,1)
polyfit2_data=((polyfit2[0] * x + polyfit2[1]))

plt.plot(x, polyfit2_data, 'orange', linewidth = 3)
plt.scatter(file_date, file_mean2)
plt.errorbar(file_date, file_mean2, yerr = file_stddev2, capsize = 5, fmt = 'none')
plt.axhline(y=0, xmin = -100, xmax = 100, linewidth = 2, color = 'blue')
plt.xlabel('Year')
plt.ylabel('Mean Values (Electrons)')
plt.ylim(-1, 1)
plt.title('2009-2016 Superbias(Ext1) Date-obs vs. Mean Value \n Overall Mean: {} e- Std.Dev: {} e-'.format("%.3f" %Mean_c2, "%.3f" %STD_c2))
plt.xticks(rotation = 30)
plt.savefig('Statistics chip2 data plot.png')
plt.show()
plt.clf() 
