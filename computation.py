
import math

def estimate_windchill(t,v):
    wci= t-0.7*v
    return wci




# Compute heatindex
def compute_heatindex(t,hum):
    a=-42.379
    b=2.04901523
    c=10.14333127
    d=-0.22475541
    e=-0.00683783
    f=-0.05481717
    g=0.0012874
    h=0.0085282
    i=-0.0000199

    rh=hum/100

    hi = (a+(b*t) + (c*rh) + (d*t*rh) + \
         (e*t**2) + (f*rh**2) + (g*t**2*rh) + \
          (h*t*rh**2) + (i*t**2*rh**2))
    return hi

def compute_dewpoint(t,h)
     """
    
     Comput the dewpoint temperature given the temperature ans humidity



     """
    tempC= (t-32)*5/9
    rh=h/100
    b=18.678
    c=257.14

gamma=math.log(rh)+(b*tempC)/ (c+tempC)
    tdp=c*gamma/(b-gamma)
