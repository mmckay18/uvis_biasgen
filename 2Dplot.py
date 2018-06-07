from astropy.io import fits
import numpy as np
import matplotlib.pyplot as plt
import os

os.chdir('/grp/hst/wfc3v/martlin/Myles_GD_files/14031_quad_filters')



hdr1=fits.open('Original09_flt_mean_stack_chip1.fits')
hdr4=fits.open('Original09_flt_mean_stack_chip2.fits')

data1=hdr1[0].data
data4=hdr4[0].data

hdr1.close()
hdr4.close()

plotdata1=data1[0:2048,0:4096].reshape(2048,4096)
plotdata4=data4[0:2048,0:4096].reshape(2048,4096)
mean1=np.nanmean(plotdata1,0)
mean4=np.nanmean(plotdata4,0)

#---------------
#  	Chip2
#---------------


plt.plot(mean1)
plt.title('Original 2009 flt mean stack chip2')
plt.xlabel('columns')
plt.ylabel('row mean')
plt.axis([-200,4500,-1.0,1.5])
plt.savefig('Original09_mean_flt_chip2.png')
plt.show()

#---------------
#  	Chip1
#---------------


plt.plot(mean4)
plt.title('Original 2009 flt mean stack chip1')
plt.xlabel('columns')
plt.ylabel('row mean')
plt.axis([-200,4500,-1.0,1.5])
plt.savefig('Original09_mean_flt_chip1.png')
plt.show()

	
