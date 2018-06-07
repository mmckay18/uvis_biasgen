from astropy.io import fits
import numpy as np
import matplotlib.pyplot as plt
import os



os.chdir('/grp/hst/wfc3r/mmckay/compare_old_2009_to_new_2009/')
#Gain = 1.5
#electrons = counts(DN) * gain(e-/DN)
old=fits.open('u1r1346ri_bia.fits')
#print(old[1].header['*'])
old1=old[4].data    
#old1[old1 == 0] = np.nan
old2=old[1].data
#old2[old2 == 0] = np.nan

#print(old2.shape)
#
#old2 = np.delete(old2, old2[:19,:]) #left overscan
#print(old2.shape)
#old2 = np.delete(old2, old2[:,:25]) #right overscan
#old2 = np.delete(old2, old2[:,4096:])
#old2 = np.delete(old2, old2[:,2048:2108])

old1_median=np.nanmean(old1)*1.5
old2_median=np.nanmean(old2)*1.5


print(old1_median, old2_median)

new=fits.open('1681902ti_bia.fits')
#print(new[1].header['*'])
new1=new[4].data
#new1[new1 == 0] = np.nan
new2=new[1].data
#new2[new2 == 0] = np.nan

new1_median=np.nanmean(new1)*1.5
new2_median=np.nanmean(new2)*1.5
print(new1_median, new2_median)

percent_diff1= (((old1_median - new1_median)) / old1_median) * 100
percent_diff2= (((old2_median - new2_median)) / old2_median) * 100

diff1= ((old1_median - new1_median))
diff2= ((old2_median - new2_median))

diff_average=(diff1 + diff2)/2
#pd1 = 100*np.abs(old1_median - new1_median)/(np.median([old1_median,new1_median]))

print(diff1,'(electrons)', diff2,'(electrons)',diff_average)
print(percent_diff1,'%', percent_diff2, '%')

old1[2052:,:] = np.nan #bottom overscan
old1[:,:26] = np.nan #left overscan
old1[:,4097:] = np.nan #right overscan
old1[:,2048:2109] = np.nan #middle overscan

new1[2051:,:] = np.nan #bottom overscan
new1[:,:26] = np.nan #left overscan
new1[:,4096:] = np.nan #right overscan
new1[:,2048:2109] = np.nan #middle overscan

old2[:20,:] =np.nan #top overscan
old2[:,:26] =np.nan #left overscan
old2[:,4096:] = np.nan #right overscan
old2[:,2048:2109] =np.nan #middle overscan

new2[:20,:] =np.nan #top overscan
new2[:,:26] =np.nan #left overscan
new2[:,4096:] = np.nan #right overscan
new2[:,2048:2109] =np.nan #middle overscan



#old1[old1 == 0] = np.nan
#old2[old2 == 0] = np.nan
#new1[new1 == 0] = np.nan
#new2[new2 == 0] = np.nan



plt.clf()
diff1=(old1-new1)
diff2=(old2-new2)
bins=np.linspace(-15,15,60)
n,bins,patches=plt.hist(old1, bins, alpha=0.50) 

#sig_old1 = np.nanstd(old1); med_old1 = np.nanmedian(old1); h_old1, b_old1 = np.histogram(old1[~np.isnan(old1)],range=[med_old1-3*sig_old1,med_old1+3*sig_old1],bins=60)
#sig_new1 = np.nanstd(new1); med_new1 = np.nanmedian(new1); h_new1, b_new1 = np.histogram(new1[~np.isnan(new1)],range=[med_new1-3*sig_new1,med_new1+3*sig_new1],bins=60)
#sig_diff1 = np.nanstd(diff1); med_diff1 = np.nanmedian(diff1); h_diff1, b_diff1 = np.histogram(diff1[~np.isnan(diff1)],range=[med_diff1-3*sig_diff1,med_diff1+3*sig_diff1],bins=60)   
#plt.step(b_old1[:-1],h_old1)
#plt.step(b_new1[:-1],h_new1)
#plt.ylabel('Frequency')
#plt.xlabel('Pixel Value(Count)')
#plt.savefig('(Ext4){} Old Bias Ref vs New Bias Ref.png'.format(new[0].header['useafter']))
#plt.step(b_diff1[:-1],h_diff1)
#plt.show()
#plt.clf()

def f(x, a, b, c): #function for gaussian curve
	return a * py.exp(-(x - b)**2.0 / (2 * c**2)) #Guassian equation
from scipy import optimize 
x = [0.5 * (bins[i] + bins[i+1]) for i in range(len(bins)-1)]
#since bins need to have an extra value to complete the bin width (here bin =50) I had to
#subtract a value to match the deminsions of the n (here n=49)
try:
    popt,pcov = optimize.curve_fit(f, x, n)
except RuntimeError:
    print("Error - curve_fit failed")
#optimize.curve_fit found my values(a,b,c) for the function f for popt(show parameter)
y_fit = f(bins, *popt) #fit y data to to histogram = function f where x= bins and a,b,c set from *popt
x_fit = py.linspace(bins[0], bins[-1], 50) #same as bins but show setup
plot = plt.plot(x_fit,y_fit,'b--', linewidth=4) #plots curve
plt.savefig('{}_flt_chip2dq_hist_.pdf'.format(h[0].header['Rootname']))
plt.clf()    
plt.show()


sig_old2 = np.nanstd(old2); med_old2 = np.nanmedian(old2); h_old2, b_old2 = np.histogram(old2[~np.isnan(old2)],range=[med_old2-3*sig_old2,med_old2+3*sig_old2],bins=60)
sig_new2 = np.nanstd(new2); med_new2 = np.nanmedian(new2); h_new2, b_new2 = np.histogram(new2[~np.isnan(new2)],range=[med_new2-3*sig_new2,med_new2+3*sig_new2],bins=60)
sig_diff2 = np.nanstd(diff2); med_diff2 = np.nanmedian(diff2); h_diff2, b_diff2 = np.histogram(diff2[~np.isnan(diff2)],range=[med_diff2-3*sig_diff2,med_diff2+3*sig_diff2],bins=60)   
plt.step(b_old2[:-1],h_old2)
plt.step(b_new2[:-1],h_new2)
plt.ylabel('Frequency')
plt.xlabel('Pixel Value(Count)')
#plt.step(b_diff2[:-1],h_diff2)
plt.savefig('(Ext1){} Old Bias Ref vs New Bias Ref.png'.format(new[0].header['useafter']))
plt.show()
plt.clf()



