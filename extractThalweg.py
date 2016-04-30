# input T-grid model output and extract data from along Thalweg
# output to file ending in _Thw.nc
import os
import re
from sys import argv

# from geopy.distance import great_circle
import netCDF4 as nc
import numpy as np


fname = argv[1]

# fname2 = fname[:-3] + '_Thw.nc'
fname2 = os.path.basename(fname)[:-3] + '_Thw.nc'
f = nc.Dataset(fname, 'r')
f2 = nc.Dataset(fname2, 'w')
fkeys = f.variables.keys()
for ik in fkeys:
    match = re.search(r'depth.', ik)
    if match:
        zkey = match.group(0)
z = f.variables[zkey][:]
t = f.variables['time_counter'][:]

thw0 = np.loadtxt(
    '/ocean/eolson/MEOPAR/tools/bathymetry/thalweg_working.txt',
    delimiter=" ", unpack=False)
thw2 = [tuple((int(k[0]), int(k[1]))) for k in thw0]

f2.createDimension('time_counter', None)
f2.createDimension('deptht', len(f.dimensions['deptht']))
f2.createDimension('distance', len(thw2))

idist = np.zeros((len(thw2), 1))
cdist = np.zeros((len(thw2), 1))
for kk in range(0, len(thw2)):
    jj = thw2[kk][0]
    ii = thw2[kk][1]
    lat = f.variables['nav_lat'][jj, ii]
    lon = f.variables['nav_lon'][jj, ii]
    if kk == 0:
        idist[kk] = 0
        cdist[kk] = 0
    else:
        jj = thw2[kk][0]
        ii = thw2[kk][1]
        # idist[kk] = great_circle((lat0, lon0), (lat, lon)).km  # km
        # gsw.distance([lon0,lon],[lat0,lat])/1000 # km
        cdist[kk] = idist[kk] + cdist[kk - 1]
    lat0 = lat
    lon0 = lon

print('starting loop')
for ik in fkeys:
    if np.size(f.variables[ik].shape) == 4:
        f2var = f2.createVariable(ik, f.variables[ik].datatype,
                                  ('time_counter', 'deptht', 'distance'))
        print(ik)
        thwvar = np.empty((len(t), len(z), len(thw2)))
        ivar = np.copy(f.variables[ik][:, :, :, :])
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
