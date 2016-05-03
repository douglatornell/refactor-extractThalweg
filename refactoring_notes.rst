*****
Notes
*****

conda env:

* ipython
* python3.5
* matplotlib
* netCDF4
* numpy
* pandas
* pytz
* requests
* scipy
* pip:

  * angles
  * arrow
  * autopep8
  * ipdb

autopep8 cleanup

change output to pwd to avoid lack of write permission


Initial run timing on salish::

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


Simplify thalweg grid point indices loading::

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

  real  0m41.936s
  user  0m30.783s
  sys 0m10.246s

Ran again after a couple of hours break to to errands and got::

  $ !499
  time python extractThalweg.py /data/eolson/MEOPAR/SS36runs/OrcinusRuns/SMELT10feb16Base/SalishSea_1h_20160210_20160211_grid_T.nc
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

  real  1m2.800s
  user  0m29.554s
  sys 0m32.739s

and then::

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

  real  0m44.554s
  user  0m29.449s
  sys 0m14.762s

So, there is a file buffer caching effect.


Move output dataset code closer to where it is used::

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

  real  0m42.327s
  user  0m29.690s
  sys 0m12.297s


Comment out the thalweg cummulative distance calc loop until we're ready to actually use its result::

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

  real  0m41.760s
  user  0m29.259s
  sys 0m12.178s


Get rid of if-statment in varibles thalweg extraction loop::

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

  real  0m43.461s
  user  0m28.521s
  sys 0m14.405s


Factor thalweg variable dimension tuple out of loop::

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

  real  0m46.607s
  user  0m30.108s
  sys 0m16.169s


Transfer the name of the depth variable from input to output dataset::

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

  real  0m46.516s
  user  0m28.948s
  sys 0m17.230s


  Use shape property rather than len() to get sizes of NumPy arrays along a dimension::

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

    real  0m54.742s
    user  0m31.828s
    sys 0m22.551s


Factor thalweg variable array creation out of loop::

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

  real  0m48.106s
  user  0m29.987s
  sys 0m17.777s


Use size property of netCDF variable's dimension instead of len()::

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

  real  0m55.645s
  user  0m30.233s
  sys 0m25.002s


Don't copy the ndarray part of the netCDF variable twice::

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

  real  0m47.246s
  user  0m27.425s
  sys 0m19.428s

`f.variables[var][:]` creates a copy of the ndarray part of the netCDF variable object, effectively separating the numbers from the metadata.
`np.copy(f.variables[var][:]` makes a copy of the copy.


Replace Python loop with NumPy indexing::

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

  real  0m48.931s
  user  0m27.334s
  sys 0m21.235s


Eliminate unneeded intermediate variable::

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

  real  0m42.678s
  user  0m26.229s
  sys 0m16.108s


Replace distance along thalweg calc loop w/ geo_tools.diatance_along_curve()::

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

  real  0m34.752s
  user  0m24.730s
  sys 0m9.870s


The resulting extractThalweg.py script has, I think, all the things that can be pushed to C code done.
The speed-up is almost a factor of 2.

The other question is:
Is it worth calculating a thalweg file for every time step of a bunch of results files?

If you simply want to plot contour thalweg sections of an arbitrary variable at an arbitrary time step, the code is pretty simple::

  import netCDF4 as nc
  import matplotlib.pyplot as plt

  from salishsea_tools import (
      tidetools,
      visualisations,
  )


  %matplotlib inline


  mesh_mask = nc.Dataset('../NEMO-forcing/grid/mesh_mask_downbyone.nc')
  grid_B = nc.Dataset('../NEMO-forcing/grid/bathy_downonegrid.nc')
  grid_hr = nc.Dataset('SalishSea_1h_20160210_20160211_grid_T.nc')

  time_step = 7
  var_name = 'vosaline'

  bathy, lons, lats = tidetools.get_bathy_data(grid_B)
  var = grid_hr.variables[var_name][time_step, ...]

  fig, ax = plt.subplots(1, 1, figsize=(15, 5))
  visualisations.contour_thalweg(
      ax, var, bathy, lons, lats, mesh_mask, 'gdept_0', clevels='salinity')
  ax.set_ylim([450,0])

The mesh mask depth variable name
(`gdept_0` above)
needs to be appropriate to the `[tuvw]` grid that the variable you are plotting is on.

If the variable you are plotting is other than salinity or temperature,
provide a NumPy array of contour colour levels for the `clevels` argument.

`visualisations.contour_thalweg()` could probably be improved to include the `ax.set_ylim([450,0])` statement that flips the y-axis to make the depth orientation correct.
