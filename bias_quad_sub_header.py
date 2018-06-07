
#------------------------------------------------------
#2009 Bias reference file header
#------------------------------------------------------
prihdr=hdu_ref[0].header
del prihdr['history']
del prihdr['comment']
prihdr['APERTURE']='QUAD_CORNER_SUBARRAYS'
prihdr['CCDAMP']='SINGLE_AMP'
prihdr['DATE']='2017-02-24T15:31:48'
prihdr['CAL_VER']='3.4 (28-Sep-2016)'
prihdr['ORIGIN']='COMMON 2016_2'
prihdr['OPUS_VER']='HSTIO/CFITSIO March 2010'
prihdr['useafter']='May 14 2009 00:00:00'
prihdr['PEDIGREE']='INFLIGHT 26/06/2009 12/12/2009'
prihdr['TIME-OBS']='18:19:06'
prihdr['comment']='Reference file created by Myles McKay.'
prihdr['HISTORY']=''
prihdr['HISTORY']=' CCD parameters table:                                                   ' 
prihdr['HISTORY']='   reference table iref$t291659mi_ccd.fits                               ' 
prihdr['HISTORY']='     GROUND                                                              ' 
prihdr['HISTORY']='     UVIS-1 CCD characteristics from TV3 data                            ' 
prihdr['HISTORY']='     From TV3 data                                                       ' 
prihdr['HISTORY']=' Uncertainty array initialized.                                          ' 
prihdr['HISTORY']=' DQICORR complete ...                                                    ' 
prihdr['HISTORY']='   values checked for saturation                                         ' 
prihdr['HISTORY']='   DQ array initialized ...                                              ' 
prihdr['HISTORY']='   reference table iref$u5d2012li_bpx.fits                               ' 
prihdr['HISTORY']='     INFLIGHT 23/06/2009 15/10/2009                                      ' 
prihdr['HISTORY']='     Based on SMOV and Cycle 17 data.----------------------------------- ' 
prihdr['HISTORY']=' BLEVCORR complete; bias level from overscan was subtracted.             ' 
prihdr['HISTORY']=' BLEVCORR includes correction for drift along lines.                     ' 
prihdr['HISTORY']='   Overscan region table:                                                ' 
prihdr['HISTORY']='   reference table iref$q911321oi_osc.fits                               ' 
prihdr['HISTORY']='     GROUND                                                              ' 
prihdr['HISTORY']='     WFC3 normal overscan CCD data compatible                            ' 
prihdr['HISTORY']='------------------------------------------------------------------------ ' 
prihdr['HISTORY']='OPUS_VER= OPUS 2012_4c  / OPUS software system version number'
prihdr['HISTORY']='CSYS_VER= hstdp-2016.2  / Calibration software system version id'                                     
prihdr['HISTORY']=''
prihdr['HISTORY']='Update Discription:' 
prihdr['HISTORY']='This reference file is an update of u6n1741hi_bia.fits.'
prihdr['HISTORY']='The following updates were applied:'
prihdr['HISTORY']='- More files were processed for a better signal to noise ratio.'
prihdr['HISTORY']='- Calwf3 3.4 was used to calibrate the individual bias files '
prihdr['HISTORY']='   and flag cosmic rays.'
prihdr['HISTORY']='- The good pixels in the resulting flt images were '
prihdr['HISTORY']='   averaged using Python 3.5.'
prihdr['HISTORY']='- Standard propagation of errors was used to populate the error arrays.'
prihdr['HISTORY']=''
prihdr['HISTORY']='This file was generated using calwf3 Version 3.4 (28-Sep-2016)'         
prihdr['HISTORY']='with the following files:'                                      

files=glob.glob('/grp/hst/wfc3u/mmckay/2009biasfiles/2009_crrg_fits/*_flt.fits')
for im in files:
    h=fits.open(im)
    prihdr['HISTORY']= '{}{}'.format(h[0].header['Rootname'],'_raw.fits')





#------------------------------------------------------
#2010a Bias reference file header
#------------------------------------------------------

prihdr=hdu_ref[0].header
del prihdr['history']
del prihdr['comment']
prihdr['APERTURE']='QUAD_CORNER_SUBARRAYS'
prihdr['CCDAMP']='SINGLE_AMP'
prihdr['DATE']='2017-02-24T15:31:48'
prihdr['CAL_VER']='3.4 (28-Sep-2016)'
prihdr['ORIGIN']='COMMON 2016_2'
prihdr['OPUS_VER']='HSTIO/CFITSIO March 2010'
prihdr['USEAFTER']='Jan 1 2010 00:00:00'
prihdr['PEDIGREE']='INFLIGHT 01/01/2010 27/05/2010'
prihdr['TIME-OBS']='18:19:06'
prihdr['comment']='Reference file created by Myles McKay.'
prihdr['HISTORY']=''
prihdr['HISTORY']=' CCD parameters table:                                                   ' 
prihdr['HISTORY']='   reference table iref$t291659mi_ccd.fits                               ' 
prihdr['HISTORY']='     GROUND                                                              ' 
prihdr['HISTORY']='     UVIS-1 CCD characteristics from TV3 data                            ' 
prihdr['HISTORY']='     From TV3 data                                                       ' 
prihdr['HISTORY']=' Uncertainty array initialized.                                          ' 
prihdr['HISTORY']=' DQICORR complete ...                                                    ' 
prihdr['HISTORY']='   values checked for saturation                                         ' 
prihdr['HISTORY']='   DQ array initialized ...                                              ' 
prihdr['HISTORY']='   reference table iref$u5d2012li_bpx.fits                               ' 
prihdr['HISTORY']='     INFLIGHT 23/06/2009 15/10/2009                                      ' 
prihdr['HISTORY']='     Based on SMOV and Cycle 17 data.----------------------------------- ' 
prihdr['HISTORY']=' BLEVCORR complete; bias level from overscan was subtracted.             ' 
prihdr['HISTORY']=' BLEVCORR includes correction for drift along lines.                     ' 
prihdr['HISTORY']='   Overscan region table:                                                ' 
prihdr['HISTORY']='   reference table iref$q911321oi_osc.fits                               ' 
prihdr['HISTORY']='     GROUND                                                              ' 
prihdr['HISTORY']='     WFC3 normal overscan CCD data compatible                            ' 
prihdr['HISTORY']='------------------------------------------------------------------------ ' 
prihdr['HISTORY']='OPUS_VER= OPUS 2012_4c  / OPUS software system version number'
prihdr['HISTORY']='CSYS_VER= hstdp-2016.2  / Calibration software system version id'                                     
prihdr['HISTORY']=''
prihdr['HISTORY']='Update Discription:' 
prihdr['HISTORY']='This reference file is an update of u6n1741li_bia.fits.'
prihdr['HISTORY']='The following updates were applied:'
prihdr['HISTORY']='- More files were processed for a better signal to noise ratio.'
prihdr['HISTORY']='- Calwf3 3.4 was used to calibrate the individual bias files '
prihdr['HISTORY']='   and flag cosmic rays.'
prihdr['HISTORY']='- The good pixels in the resulting flt images were '
prihdr['HISTORY']='   averaged using Python 3.5.'
prihdr['HISTORY']='- Standard propagation of errors was used to populate the error arrays.'
prihdr['HISTORY']=''
prihdr['HISTORY']='This file was generated using calwf3 Version 3.4 (28-Sep-2016)'         
prihdr['HISTORY']='with the following files:'                                      

files=glob.glob('/grp/hst/wfc3u/mmckay/2010biasfiles/2010a_crrg_flts/*flt.fits')
for im in files:
    h=fits.open(im)
    prihdr['HISTORY']= '{}{}'.format(h[0].header['Rootname'],'_raw.fits')






#------------------------------------------------------
#2010b Bias reference file header
#------------------------------------------------------

prihdr=hdu_ref[0].header
del prihdr['history']
del prihdr['comment']
prihdr['APERTURE']='QUAD_CORNER_SUBARRAYS'
prihdr['CCDAMP']='SINGLE_AMP'
prihdr['DATE']='2017-02-24T15:31:48'
prihdr['CAL_VER']='3.4 (28-Sep-2016)'
prihdr['ORIGIN']='COMMON 2016_2'
prihdr['OPUS_VER']='HSTIO/CFITSIO March 2010'
prihdr['USEAFTER']='May 27 2010 00:00:00'
prihdr['PEDIGREE']='INFLIGHT 27/05/2010 31/12/2010'
prihdr['TIME-OBS']='18:19:06'
prihdr['comment']='Reference file created by Myles McKay.'
prihdr['HISTORY']=''
prihdr['HISTORY']=' CCD parameters table:                                                   ' 
prihdr['HISTORY']='   reference table iref$t291659mi_ccd.fits                               ' 
prihdr['HISTORY']='     GROUND                                                              ' 
prihdr['HISTORY']='     UVIS-1 CCD characteristics from TV3 data                            ' 
prihdr['HISTORY']='     From TV3 data                                                       ' 
prihdr['HISTORY']=' Uncertainty array initialized.                                          ' 
prihdr['HISTORY']=' DQICORR complete ...                                                    ' 
prihdr['HISTORY']='   values checked for saturation                                         ' 
prihdr['HISTORY']='   DQ array initialized ...                                              ' 
prihdr['HISTORY']='   reference table iref$u5d2012li_bpx.fits                               ' 
prihdr['HISTORY']='     INFLIGHT 23/06/2009 15/10/2009                                      ' 
prihdr['HISTORY']='     Based on SMOV and Cycle 17 data.----------------------------------- ' 
prihdr['HISTORY']=' BLEVCORR complete; bias level from overscan was subtracted.             ' 
prihdr['HISTORY']=' BLEVCORR includes correction for drift along lines.                     ' 
prihdr['HISTORY']='   Overscan region table:                                                ' 
prihdr['HISTORY']='   reference table iref$q911321oi_osc.fits                               ' 
prihdr['HISTORY']='     GROUND                                                              ' 
prihdr['HISTORY']='     WFC3 normal overscan CCD data compatible                            ' 
prihdr['HISTORY']='------------------------------------------------------------------------ ' 
prihdr['HISTORY']='OPUS_VER= OPUS 2012_4c  / OPUS software system version number'
prihdr['HISTORY']='CSYS_VER= hstdp-2016.2  / Calibration software system version id'                                     
prihdr['HISTORY']=''
prihdr['HISTORY']='Update Discription:' 
prihdr['HISTORY']='This reference file is an update of u6n1741li_bia.fits.'
prihdr['HISTORY']='The following updates were applied:'
prihdr['HISTORY']='- More files were processed for a better signal to noise ratio.'
prihdr['HISTORY']='- Calwf3 3.4 was used to calibrate the individual bias files '
prihdr['HISTORY']='   and flag cosmic rays.'
prihdr['HISTORY']='- The good pixels in the resulting flt images were '
prihdr['HISTORY']='   averaged using Python 3.5.'
prihdr['HISTORY']='- Standard propagation of errors was used to populate the error arrays.'
prihdr['HISTORY']=''
prihdr['HISTORY']='This file was generated using calwf3 Version 3.4 (28-Sep-2016)'         
prihdr['HISTORY']='with the following files:'                                      

files=glob.glob('/grp/hst/wfc3u/mmckay/2010biasfiles/2010b_crrg_flts/*flt.fits')
for im in files:
    h=fits.open(im)
    prihdr['HISTORY']= '{}{}'.format(h[0].header['Rootname'],'_raw.fits')





#------------------------------------------------------
#2011 Bias reference file header
#------------------------------------------------------

prihdr=hdu_ref[0].header
del prihdr['history']
del prihdr['comment']
prihdr['APERTURE']='QUAD_CORNER_SUBARRAYS'
prihdr['CCDAMP']='SINGLE_AMP'
prihdr['DATE']='2017-02-24T15:31:48'
prihdr['CAL_VER']='3.4 (28-Sep-2016)'
prihdr['ORIGIN']='COMMON 2016_2'
prihdr['OPUS_VER']='HSTIO/CFITSIO March 2010'
prihdr['USEAFTER']='Jan 01 2011 00:00:00'
prihdr['PEDIGREE']='INFLIGHT 01/01/2011 31/12/2011'
prihdr['TIME-OBS']='18:19:06'
prihdr['comment']='Reference file created by Myles McKay.'
prihdr['HISTORY']=''
prihdr['HISTORY']=' CCD parameters table:                                                   ' 
prihdr['HISTORY']='   reference table iref$t291659mi_ccd.fits                               ' 
prihdr['HISTORY']='     GROUND                                                              ' 
prihdr['HISTORY']='     UVIS-1 CCD characteristics from TV3 data                            ' 
prihdr['HISTORY']='     From TV3 data                                                       ' 
prihdr['HISTORY']=' Uncertainty array initialized.                                          ' 
prihdr['HISTORY']=' DQICORR complete ...                                                    ' 
prihdr['HISTORY']='   values checked for saturation                                         ' 
prihdr['HISTORY']='   DQ array initialized ...                                              ' 
prihdr['HISTORY']='   reference table iref$u5d2012li_bpx.fits                               ' 
prihdr['HISTORY']='     INFLIGHT 23/06/2009 15/10/2009                                      ' 
prihdr['HISTORY']='     Based on SMOV and Cycle 17 data.----------------------------------- ' 
prihdr['HISTORY']=' BLEVCORR complete; bias level from overscan was subtracted.             ' 
prihdr['HISTORY']=' BLEVCORR includes correction for drift along lines.                     ' 
prihdr['HISTORY']='   Overscan region table:                                                ' 
prihdr['HISTORY']='   reference table iref$q911321oi_osc.fits                               ' 
prihdr['HISTORY']='     GROUND                                                              ' 
prihdr['HISTORY']='     WFC3 normal overscan CCD data compatible                            ' 
prihdr['HISTORY']='------------------------------------------------------------------------ ' 
prihdr['HISTORY']='OPUS_VER= OPUS 2012_4c  / OPUS software system version number'
prihdr['HISTORY']='CSYS_VER= hstdp-2016.2  / Calibration software system version id'                                     
prihdr['HISTORY']=''
prihdr['HISTORY']='This file was generated using calwf3 Version 3.4 (28-Sep-2016)'         
prihdr['HISTORY']='with the following files:'                                      

files=glob.glob('/grp/hst/wfc3u/mmckay/2011biasfiles/2011_crrg_files/*flt.fits')
for im in files:
    h=fits.open(im)
    prihdr['HISTORY']= '{}{}'.format(h[0].header['Rootname'],'_raw.fits')








#------------------------------------------------------
#2012 Bias reference file header
#------------------------------------------------------

prihdr=hdu_ref[0].header
del prihdr['history']
del prihdr['comment']
prihdr['APERTURE']='QUAD_CORNER_SUBARRAYS'
prihdr['CCDAMP']='SINGLE_AMP'
prihdr['DATE']='2017-02-24T15:31:48'
prihdr['CAL_VER']='3.4 (28-Sep-2016)'
prihdr['ORIGIN']='COMMON 2016_2'
prihdr['OPUS_VER']='HSTIO/CFITSIO March 2010'
prihdr['USEAFTER']='Jan 01 2012 00:00:00'
prihdr['PEDIGREE']='INFLIGHT 01/01/2012 31/12/2012'
prihdr['TIME-OBS']='18:19:06'
prihdr['comment']='Reference file created by Myles McKay.'
prihdr['HISTORY']=''
prihdr['HISTORY']=' CCD parameters table:                                                   ' 
prihdr['HISTORY']='   reference table iref$t291659mi_ccd.fits                               ' 
prihdr['HISTORY']='     GROUND                                                              ' 
prihdr['HISTORY']='     UVIS-1 CCD characteristics from TV3 data                            ' 
prihdr['HISTORY']='     From TV3 data                                                       ' 
prihdr['HISTORY']=' Uncertainty array initialized.                                          ' 
prihdr['HISTORY']=' DQICORR complete ...                                                    ' 
prihdr['HISTORY']='   values checked for saturation                                         ' 
prihdr['HISTORY']='   DQ array initialized ...                                              ' 
prihdr['HISTORY']='   reference table iref$u5d2012li_bpx.fits                               ' 
prihdr['HISTORY']='     INFLIGHT 23/06/2009 15/10/2009                                      ' 
prihdr['HISTORY']='     Based on SMOV and Cycle 17 data.----------------------------------- ' 
prihdr['HISTORY']=' BLEVCORR complete; bias level from overscan was subtracted.             ' 
prihdr['HISTORY']=' BLEVCORR includes correction for drift along lines.                     ' 
prihdr['HISTORY']='   Overscan region table:                                                ' 
prihdr['HISTORY']='   reference table iref$q911321oi_osc.fits                               ' 
prihdr['HISTORY']='     GROUND                                                              ' 
prihdr['HISTORY']='     WFC3 normal overscan CCD data compatible                            ' 
prihdr['HISTORY']='------------------------------------------------------------------------ ' 
prihdr['HISTORY']='OPUS_VER= OPUS 2012_4c  / OPUS software system version number'
prihdr['HISTORY']='CSYS_VER= hstdp-2016.2  / Calibration software system version id'                                     
prihdr['HISTORY']=''
prihdr['HISTORY']='This file was generated using calwf3 Version 3.4 (28-Sep-2016)'         
prihdr['HISTORY']='with the following files:'                                      

files=glob.glob('/grp/hst/wfc3u/mmckay/2012biasfiles/2012_crrg_flts/*flt.fits')
for im in files:
    h=fits.open(im)
    prihdr['HISTORY']= '{}{}'.format(h[0].header['Rootname'],'_raw.fits')














#------------------------------------------------------
#2013 Bias reference file header
#------------------------------------------------------

prihdr=hdu_ref[0].header
del prihdr['history']
del prihdr['comment']
prihdr['APERTURE']='QUAD_CORNER_SUBARRAYS'
prihdr['CCDAMP']='SINGLE_AMP'
prihdr['DATE']='2017-02-24T15:31:48'
prihdr['CAL_VER']='3.4 (28-Sep-2016)'
prihdr['ORIGIN']='COMMON 2016_2'
prihdr['OPUS_VER']='HSTIO/CFITSIO March 2010'
prihdr['USEAFTER']='Jan 01 2013 00:00:00'
prihdr['PEDIGREE']='INFLIGHT 01/01/2013 31/12/2013'
prihdr['TIME-OBS']='18:19:06'
prihdr['comment']='Reference file created by Myles McKay.'
prihdr['HISTORY']=''
prihdr['HISTORY']=' CCD parameters table:                                                   ' 
prihdr['HISTORY']='   reference table iref$t291659mi_ccd.fits                               ' 
prihdr['HISTORY']='     GROUND                                                              ' 
prihdr['HISTORY']='     UVIS-1 CCD characteristics from TV3 data                            ' 
prihdr['HISTORY']='     From TV3 data                                                       ' 
prihdr['HISTORY']=' Uncertainty array initialized.                                          ' 
prihdr['HISTORY']=' DQICORR complete ...                                                    ' 
prihdr['HISTORY']='   values checked for saturation                                         ' 
prihdr['HISTORY']='   DQ array initialized ...                                              ' 
prihdr['HISTORY']='   reference table iref$u5d2012li_bpx.fits                               ' 
prihdr['HISTORY']='     INFLIGHT 23/06/2009 15/10/2009                                      ' 
prihdr['HISTORY']='     Based on SMOV and Cycle 17 data.----------------------------------- ' 
prihdr['HISTORY']=' BLEVCORR complete; bias level from overscan was subtracted.             ' 
prihdr['HISTORY']=' BLEVCORR includes correction for drift along lines.                     ' 
prihdr['HISTORY']='   Overscan region table:                                                ' 
prihdr['HISTORY']='   reference table iref$q911321oi_osc.fits                               ' 
prihdr['HISTORY']='     GROUND                                                              ' 
prihdr['HISTORY']='     WFC3 normal overscan CCD data compatible                            ' 
prihdr['HISTORY']='------------------------------------------------------------------------ ' 
prihdr['HISTORY']='OPUS_VER= OPUS 2013_1  / OPUS software system version number '
prihdr['HISTORY']='CSYS_VER= hstdp-2016.2 / Calibration software system version id'                                     
prihdr['HISTORY']=''
prihdr['HISTORY']='This file was generated using calwf3 Version 3.4 (28-Sep-2016)'         
prihdr['HISTORY']='with the following files:'                                      

files=glob.glob('/grp/hst/wfc3u/mmckay/2013biasfiles/2013_crrg_flts/*flt.fits')
for im in files:
    h=fits.open(im)
    prihdr['HISTORY']= '{}{}'.format(h[0].header['Rootname'],'_raw.fits')













#------------------------------------------------------
#2014 Bias reference file header
#------------------------------------------------------

prihdr=hdu_ref[0].header
del prihdr['history']
del prihdr['comment']
prihdr['APERTURE']='QUAD_CORNER_SUBARRAYS'
prihdr['CCDAMP']='SINGLE_AMP'
prihdr['DATE']='2017-02-24T15:31:48'
prihdr['CAL_VER']='3.4 (28-Sep-2016)'
prihdr['ORIGIN']='COMMON 2016_2'
prihdr['OPUS_VER']='HSTIO/CFITSIO March 2010'
prihdr['USEAFTER']='Jan 01 2014 00:00:00'
prihdr['PEDIGREE']='INFLIGHT 01/01/2014 31/12/2014'
prihdr['TIME-OBS']='18:19:06'
prihdr['comment']='Reference file created by Myles McKay.'
prihdr['HISTORY']=''
prihdr['HISTORY']=' CCD parameters table:                                                   ' 
prihdr['HISTORY']='   reference table iref$t291659mi_ccd.fits                               ' 
prihdr['HISTORY']='     GROUND                                                              ' 
prihdr['HISTORY']='     UVIS-1 CCD characteristics from TV3 data                            ' 
prihdr['HISTORY']='     From TV3 data                                                       ' 
prihdr['HISTORY']=' Uncertainty array initialized.                                          ' 
prihdr['HISTORY']=' DQICORR complete ...                                                    ' 
prihdr['HISTORY']='   values checked for saturation                                         ' 
prihdr['HISTORY']='   DQ array initialized ...                                              ' 
prihdr['HISTORY']='   reference table iref$u5d2012li_bpx.fits                               ' 
prihdr['HISTORY']='     INFLIGHT 23/06/2009 15/10/2009                                      ' 
prihdr['HISTORY']='     Based on SMOV and Cycle 17 data.----------------------------------- ' 
prihdr['HISTORY']=' BLEVCORR complete; bias level from overscan was subtracted.             ' 
prihdr['HISTORY']=' BLEVCORR includes correction for drift along lines.                     ' 
prihdr['HISTORY']='   Overscan region table:                                                ' 
prihdr['HISTORY']='   reference table iref$q911321oi_osc.fits                               ' 
prihdr['HISTORY']='     GROUND                                                              ' 
prihdr['HISTORY']='     WFC3 normal overscan CCD data compatible                            ' 
prihdr['HISTORY']='------------------------------------------------------------------------ ' 
prihdr['HISTORY']='OPUS_VER= HSTDP 2014_3 / OPUS software system version number  '
prihdr['HISTORY']='CSYS_VER= hstdp-2016.2 / Calibration software system version id'                                     
prihdr['HISTORY']=''
prihdr['HISTORY']='This file was generated using calwf3 Version 3.4 (28-Sep-2016)'         
prihdr['HISTORY']='with the following files:'                                      

files=glob.glob('/grp/hst/wfc3u/mmckay/2014biasfiles/2014_crrg_flts/*flt.fits')
for im in files:
    h=fits.open(im)
    prihdr['HISTORY']= '{}{}'.format(h[0].header['Rootname'],'_raw.fits')

















#------------------------------------------------------
#2015 Bias reference file header
#------------------------------------------------------

prihdr=hdu_ref[0].header
del prihdr['history']
del prihdr['comment']
prihdr['APERTURE']='QUAD_CORNER_SUBARRAYS'
prihdr['CCDAMP']='SINGLE_AMP'
prihdr['DATE']='2017-02-24T15:31:48'
prihdr['CAL_VER']='3.4 (28-Sep-2016)'
prihdr['ORIGIN']='COMMON 2016_2'
prihdr['OPUS_VER']='HSTIO/CFITSIO March 2010'
prihdr['USEAFTER']='Jan 01 2015 00:00:00'
prihdr['PEDIGREE']='INFLIGHT 01/01/2015 31/12/2015'
prihdr['TIME-OBS']='18:19:06'
prihdr['comment']='Reference file created by Myles McKay.'
prihdr['HISTORY']=''
prihdr['HISTORY']=' CCD parameters table:                                                   ' 
prihdr['HISTORY']='   reference table iref$t291659mi_ccd.fits                               ' 
prihdr['HISTORY']='     GROUND                                                              ' 
prihdr['HISTORY']='     UVIS-1 CCD characteristics from TV3 data                            ' 
prihdr['HISTORY']='     From TV3 data                                                       ' 
prihdr['HISTORY']=' Uncertainty array initialized.                                          ' 
prihdr['HISTORY']=' DQICORR complete ...                                                    ' 
prihdr['HISTORY']='   values checked for saturation                                         ' 
prihdr['HISTORY']='   DQ array initialized ...                                              ' 
prihdr['HISTORY']='   reference table iref$u5d2012li_bpx.fits                               ' 
prihdr['HISTORY']='     INFLIGHT 23/06/2009 15/10/2009                                      ' 
prihdr['HISTORY']='     Based on SMOV and Cycle 17 data.----------------------------------- ' 
prihdr['HISTORY']=' BLEVCORR complete; bias level from overscan was subtracted.             ' 
prihdr['HISTORY']=' BLEVCORR includes correction for drift along lines.                     ' 
prihdr['HISTORY']='   Overscan region table:                                                ' 
prihdr['HISTORY']='   reference table iref$q911321oi_osc.fits                               ' 
prihdr['HISTORY']='     GROUND                                                              ' 
prihdr['HISTORY']='     WFC3 normal overscan CCD data compatible                            ' 
prihdr['HISTORY']='------------------------------------------------------------------------ ' 
prihdr['HISTORY']='OPUS_VER= HSTDP 2014_4b / OPUS software system version number '
prihdr['HISTORY']='CSYS_VER= hstdp-2016.2 / Calibration software system version id'                                     
prihdr['HISTORY']=''
prihdr['HISTORY']='This file was generated using calwf3 Version 3.4 (28-Sep-2016)'         
prihdr['HISTORY']='with the following files:'                                      

files=glob.glob('/grp/hst/wfc3u/mmckay/2015biasfiles/2015_crrg_flts/*flt.fits')
for im in files:
    h=fits.open(im)
    prihdr['HISTORY']= '{}{}'.format(h[0].header['Rootname'],'_raw.fits')


















#------------------------------------------------------
#2016 Bias reference file header
#------------------------------------------------------

prihdr=hdu_ref[0].header
del prihdr['history']
del prihdr['comment']
prihdr['APERTURE']='QUAD_CORNER_SUBARRAYS'
prihdr['CCDAMP']='SINGLE_AMP'
prihdr['DATE']='2017-02-24T15:31:48'
prihdr['CAL_VER']='3.4 (28-Sep-2016)'
prihdr['ORIGIN']='COMMON 2016_2'
prihdr['OPUS_VER']='HSTIO/CFITSIO March 2010'
prihdr['USEAFTER']='Jan 01 2016 00:00:00'
prihdr['PEDIGREE']='INFLIGHT 01/01/2016 31/12/2016'
prihdr['TIME-OBS']='18:19:06'
prihdr['comment']='Reference file created by Myles McKay.'
prihdr['HISTORY']=''
prihdr['HISTORY']=' CCD parameters table:                                                   ' 
prihdr['HISTORY']='   reference table iref$t291659mi_ccd.fits                               ' 
prihdr['HISTORY']='     GROUND                                                              ' 
prihdr['HISTORY']='     UVIS-1 CCD characteristics from TV3 data                            ' 
prihdr['HISTORY']='     From TV3 data                                                       ' 
prihdr['HISTORY']=' Uncertainty array initialized.                                          ' 
prihdr['HISTORY']=' DQICORR complete ...                                                    ' 
prihdr['HISTORY']='   values checked for saturation                                         ' 
prihdr['HISTORY']='   DQ array initialized ...                                              ' 
prihdr['HISTORY']='   reference table iref$u5d2012li_bpx.fits                               ' 
prihdr['HISTORY']='     INFLIGHT 23/06/2009 15/10/2009                                      ' 
prihdr['HISTORY']='     Based on SMOV and Cycle 17 data.----------------------------------- ' 
prihdr['HISTORY']=' BLEVCORR complete; bias level from overscan was subtracted.             ' 
prihdr['HISTORY']=' BLEVCORR includes correction for drift along lines.                     ' 
prihdr['HISTORY']='   Overscan region table:                                                ' 
prihdr['HISTORY']='   reference table iref$q911321oi_osc.fits                               ' 
prihdr['HISTORY']='     GROUND                                                              ' 
prihdr['HISTORY']='     WFC3 normal overscan CCD data compatible                            ' 
prihdr['HISTORY']='------------------------------------------------------------------------ ' 
prihdr['HISTORY']='OPUS_VER= HSTDP 2015_3  / OPUS software system version number  '
prihdr['HISTORY']='CSYS_VER= hstdp-2016.2 / Calibration software system version id'                                     
prihdr['HISTORY']=''
prihdr['HISTORY']='This file was generated using calwf3 Version 3.4 (28-Sep-2016)'         
prihdr['HISTORY']='with the following files:'                                      

files=glob.glob('/grp/hst/wfc3u/mmckay/2016biasfiles/2016_crrg_flts/*flt.fits')
for im in files:
    h=fits.open(im)
    prihdr['HISTORY']= '{}{}'.format(h[0].header['Rootname'],'_raw.fits')







#------------------------------------------------------
#2017 Bias reference file header
#------------------------------------------------------

prihdr=hdu_ref[0].header
del prihdr['history']
del prihdr['comment']
del prihdr['DESCRIP']
prihdr['APERTURE']='QUAD_CORNER_SUBARRAYS'
prihdr['DESCRIP']='Bias intended for use with subarrays.-----------' 
prihdr['CCDAMP']='SINGLE_AMP'
prihdr['DATE']='2018-02-06T15:31:48'
prihdr['CAL_VER']='3.4 (28-Sep-2016)'
prihdr['ORIGIN']='COMMON 2016_2'
prihdr['OPUS_VER']='HSTIO/CFITSIO March 2010'
prihdr['USEAFTER']='Jan 01 2017 00:00:00'
prihdr['PEDIGREE']='INFLIGHT 01/01/2017 31/12/2017'
prihdr['TIME-OBS']='18:19:06'
prihdr['comment']='Reference file created by Myles McKay.'
prihdr['HISTORY']=''
prihdr['HISTORY']=' CCD parameters table:                                                   ' 
prihdr['HISTORY']='   reference table iref$t291659mi_ccd.fits                               ' 
prihdr['HISTORY']='     GROUND                                                              ' 
prihdr['HISTORY']='     UVIS-1 CCD characteristics from TV3 data                            ' 
prihdr['HISTORY']='     From TV3 data                                                       ' 
prihdr['HISTORY']=' Uncertainty array initialized.                                          ' 
prihdr['HISTORY']=' DQICORR complete ...                                                    ' 
prihdr['HISTORY']='   values checked for saturation                                         ' 
prihdr['HISTORY']='   DQ array initialized ...                                              ' 
prihdr['HISTORY']='   reference table iref$u5d2012li_bpx.fits                               ' 
prihdr['HISTORY']='     INFLIGHT 23/06/2009 15/10/2009                                      ' 
prihdr['HISTORY']='     Based on SMOV and Cycle 17 data.----------------------------------- ' 
prihdr['HISTORY']=' BLEVCORR complete; bias level from overscan was subtracted.             ' 
prihdr['HISTORY']=' BLEVCORR includes correction for drift along lines.                     ' 
prihdr['HISTORY']='   Overscan region table:                                                ' 
prihdr['HISTORY']='   reference table iref$q911321oi_osc.fits                               ' 
prihdr['HISTORY']='     GROUND                                                              ' 
prihdr['HISTORY']='     WFC3 normal overscan CCD data compatible                            ' 
prihdr['HISTORY']='------------------------------------------------------------------------ ' 
prihdr['HISTORY']='OPUS_VER= HSTDP 2015_3  / OPUS software system version number  '
prihdr['HISTORY']='CSYS_VER= hstdp-2016.2 / Calibration software system version id'                                     
prihdr['HISTORY']=''
prihdr['HISTORY']='This file was generated using calwf3 Version 3.4 (28-Sep-2016)'         
prihdr['HISTORY']='with the following files:'                                      

files=glob.glob('/grp/hst/wfc3u/mmckay/2017biasfiles/nongrown_flts/*flt.fits')
for im in files:
    h=fits.open(im)
    prihdr['HISTORY']= '{}{}'.format(h[0].header['Rootname'],'_raw.fits')
