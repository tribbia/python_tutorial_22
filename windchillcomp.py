
from printing import print_comparison
from readdata import read_data

#Column names column indices
columns={'date': 0, 'time' : 1,  'tempout' : 2, 'windspeed': 7, 'windchill': 12}
types={'tempout': float, 'windspeed': float , 'windchill' : float }
# Read the data file
data= read_data(columns, types=types)
def estimate_windchill(t,v):
    wci= t-0.7*v
    return wci

windchill=[]
for temp, windspeed in zip(data['tempout'], data['windspeed']):
    windchill.append(estimate_windchill(temp,windspeed))
# Output comparion of data
print_comparison('WINDCHILL',data['date'], data['time'], data['windchill'], windchill)
