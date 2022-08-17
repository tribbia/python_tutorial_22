
from printing import print_comparison
from readdata import read_data
from computation import estimate_windchill


#Column names column indices
columns={'date': 0, 'time' : 1,  'tempout' : 2, 'windspeed': 7, 'windchill': 12}
types={'tempout': float, 'windspeed': float , 'windchill' : float }
# Read the data file
data= read_data(columns, types=types)

# Estimate windchill
windchill=[estimate_windchill(t,v) for t, v in zip(data['tempout'], data['windspeed'])]
# Output comparion of data
print_comparison('WINDCHILL',data['date'], data['time'], data['windchill'], windchill)
