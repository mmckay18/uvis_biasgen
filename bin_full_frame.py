from pyraf import iraf
import os


filename= '2009_final_bias_ref.fits'
os.chdir('/grp/hst/wfc3r/mmckay/bin_test')
mkimage big.fits option='make' value=1.0 ndim=2 dims='4206 2070'
imcopy (filename//“[4,noinherit][1:2048,1:2051]”, “big.fits[0][26:2073,20:2070]”, verb+)
imcopy (filename//“[4,noinherit][2049:4096,1:2051]”, “big.fits[0][2134:4181,20:2070]”,verb+)
imcopy (filename//“[1,noinherit][1:2048,1:2051]”, “big.fits[0][26:2073,1:2051]”, verb+)
imcopy (filename//“[1,noinherit][2049:4096,1:2051]”, “big.fits[0][2134:4181,1:2051]”, verb+)

blkavg (“big.fits”,“bbig.fits”,b1=2,b2=2,option=“average”)
blkavg (“big.fits”,“bbig.fits”,b1=3,b2=3,option=“average”)