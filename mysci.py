# Column names
columns={'date': 0, 'time' : 1,  'tempout' : 2, 'windspeed': 7}
types={'tempout': float}
#Initialize my data variable
data= {'date':[],'time':[],'tempout':[]}
for column in columns:
    data[column]=[]
# Read the data file
filename="data/wxobs20170821.txt"
with open(filename,"r") as datafile:
    for _ in range(3):
       	datafile.readline()
    for line in datafile:
        datum = line.split()
#        data.append(datum)
        data['date'].append(datum[0])
        data['time'].append(datum[1])
        data['tempout'].append(float(datum[2]))
       # for column in columns:
       #     i=columns[column]
       #     t = types.get(column,str)
       #     value =t(datum[i])
       #     data[column].append(value)

#def estimate_windchill(t,v):
#    wci= t-0.7*v
#    return wci

#windchill=[]
#for temp, windspeed in zip(data['tempout'], data['windspeed']):
#    windchill.append(estimate_windchill(temp,windspeed))
