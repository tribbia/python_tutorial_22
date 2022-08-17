
from readdata import read_data
from printing import print_comparison
from computation import compute_heatindex

#Column names column indices

columns={'date': 0, 'time' : 1,  'tempout' : 2, 'humout': 5, 'heatindex': 13}
types={'tempout': float, 'humout': float , 'heatindex' : float }
# Read the data file
data= read_data(columns, types=types)

# Compute heatindex

heatindex = [compute_heatindex(t,h) for t, h in zip(data['tempout'], data['humout'])]

# Output comparion of data
print_comparison('HEATINDEX',data['date'], data['time'], data['heatindex'],heatindex)
