# input T-grid model output and extract data from along Thalweg
# output to file ending in _Thw.nc
import os
from sys import argv

import netCDF4 as nc
import numpy as np


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

# idist = np.zeros((len(thw2), 1))
# cdist = np.zeros((len(thw2), 1))
# for kk in range(0, len(thw2)):
#     jj = thw2[kk][0]
#     ii = thw2[kk][1]
#     lat = f.variables['nav_lat'][jj, ii]
#     lon = f.variables['nav_lon'][jj, ii]
#     if kk == 0:
#         idist[kk] = 0
#         cdist[kk] = 0
#     else:
#         jj = thw2[kk][0]
#         ii = thw2[kk][1]
#         # idist[kk] = great_circle((lat0, lon0), (lat, lon)).km  # km
#         # gsw.distance([lon0,lon],[lat0,lat])/1000 # km
#         cdist[kk] = idist[kk] + cdist[kk - 1]
#     lat0 = lat
#     lon0 = lon

# fname2 = fname[:-3] + '_Thw.nc'
fname2 = os.path.basename(fname)[:-3] + '_Thw.nc'
f2 = nc.Dataset(fname2, 'w')
f2.createDimension('time_counter', None)
f2.createDimension('deptht', len(f.dimensions['deptht']))
f2.createDimension('distance', len(thw2))

print('starting loop')
vars_4d = (var for var in f.variables if f.variables[var].ndim == 4)
for var in vars_4d:
    f2var = f2.createVariable(var, f.variables[var].datatype,
                              ('time_counter', 'deptht', 'distance'))
    print(var)
    thwvar = np.empty((len(t), len(z), len(thw2)))
    ivar = np.copy(f.variables[var][:, :, :, :])
    for kk in range(len(thw2)):
        thwvar[:, :, kk] = ivar[:, :, thw2[kk][0], thw2[kk][1]]
    print(thwvar[0, 5, :10])
    f2var[:, :, :] = thwvar

new_tc = f2.createVariable('time_counter', float, ('time_counter'))
new_tc[:] = t
new_z = f2.createVariable('deptht', float, ('deptht'))
new_z[:] = z
# new_dist = f2.createVariable('distance', float, ('distance'))
# new_dist[:] = cdist
f2.close()
f.close()
