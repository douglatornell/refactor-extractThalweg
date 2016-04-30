*****
Notes
*****

conda env:

* python3.5
* netCDF4
* ipython
* pip:

  * autopep8
  * ipdb

autopep8 cleanup

change output to pwd to avoid lack of write permission

Initial run timing::

  $ time python extractThalweg.py /data/eolson/MEOPAR/SS36runs/OrcinusRuns/SMELT10feb16Base/SalishSea_1h_20160210_20160211_grid_T.nc
  starting loop
  buoy_n2
  [ 0.00076488  0.00074984  0.00072764  0.00046132  0.00081759  0.00104725
    0.00169606  0.00207344  0.0021249   0.00142109]
  vosaline
  [ 29.91957855  29.89844894  29.93364716  30.05670357  29.76695442
    29.7635498   30.01867294  30.14416313  30.3995018   30.45392227]
  votemper
  [ 8.97643089  8.95770168  8.95432854  8.97372341  8.90650558  8.9015398
    8.97531414  9.05134106  9.07783318  8.99243546]

  real  0m58.385s
  user  0m29.218s
  sys 0m27.244s

Make depth variable detection more Pythonic::

  $ time python extractThalweg.py /data/eolson/MEOPAR/SS36runs/OrcinusRuns/SMELT10feb16Base/SalishSea_1h_20160210_20160211_grid_T.nc
  starting loop
  buoy_n2
  [ 0.00076488  0.00074984  0.00072764  0.00046132  0.00081759  0.00104725
    0.00169606  0.00207344  0.0021249   0.00142109]
  vosaline
  [ 29.91957855  29.89844894  29.93364716  30.05670357  29.76695442
    29.7635498   30.01867294  30.14416313  30.3995018   30.45392227]
  votemper
  [ 8.97643089  8.95770168  8.95432854  8.97372341  8.90650558  8.9015398
    8.97531414  9.05134106  9.07783318  8.99243546]

  real  0m43.038s
  user  0m31.574s
  sys 0m10.956s