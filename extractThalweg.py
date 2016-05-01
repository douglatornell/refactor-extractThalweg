# input T-grid model output and extract data from along Thalweg
# output to file ending in _Thw.nc
import os
from sys import argv

import netCDF4 as nc
import numpy as np

from salishsea_tools import geo_tools


fname = argv[1]
f = nc.Dataset(fname, 'r')
z_var = [
    k for k in f.variables
    if k.startswith('depth') and not k.endswith('bounds')][0]
z = f.variables[z_var][:]
t = f.variables['time_counter'][:]

thw2 = np.loadtxt(
    '/ocean/eolson/MEOPAR/tools/bathymetry/thalweg_working.txt',
    delimiter=" ", dtype=int)
lons = f.variables['nav_lon'][:]
lats = f.variables['nav_lat'][:]
lons_thal = lons[thw2[:, 0], thw2[:, 1]]
lats_thal = lats[thw2[:, 0], thw2[:, 1]]
cdist = geo_tools.distance_along_curve(lons_thal, lats_thal)


# fname2 = fname[:-3] + '_Thw.nc'
fname2 = os.path.basename(fname)[:-3] + '_Thw.nc'
f2 = nc.Dataset(fname2, 'w')
f2.createDimension('time_counter', None)
f2.createDimension(z_var, f.dimensions[z_var].size)
f2.createDimension('distance', thw2.shape[0])

vars_4d = (var for var in f.variables if f.variables[var].ndim == 4)
var_dims = ('time_counter', 'deptht', 'distance')
print('starting loop')
for var in vars_4d:
    f2var = f2.createVariable(var, f.variables[var].datatype, var_dims)
    print(var)
    ivar = f.variables[var][:]
    f2var[:] = ivar[..., thw2[:, 0], thw2[:, 1]]
    print(f2var[0, 5, :10])

new_tc = f2.createVariable('time_counter', float, ('time_counter'))
new_tc[:] = t
new_z = f2.createVariable('deptht', float, ('deptht'))
new_z[:] = z
new_dist = f2.createVariable('distance', float, ('distance'))
new_dist[:] = cdist
f2.close()
f.close()
