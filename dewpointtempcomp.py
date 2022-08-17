
from mysci.printing import print_comparison
from mysci.readdata import read_data
from mysci.computation import compute_dewpoint

#Column names column indices
columns={'date': 0, 'time' : 1,  'tempout' : 2, 'humout': 5, 'dewpt': 6}
types={'tempout': float, 'humout': float , 'dewpt' : float }
# Read the data file
data= read_data(columns, types=types)

# Compute dew point temperature
dewpointtemp=[compute_dewpoint(t,h) for t, h in zip(data['tempout'], data['humout'])]
# Output comparion of data
print_comparison('DEW PT',data['date'], data['time'], data['dewpt'], dewpointtemp)
