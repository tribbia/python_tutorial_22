
import math

def estimate_windchill(t,v):
    """ 
    Estimate the windchill factor given the temperature and windspeed

    NOTE: this computation is only valid for temperatures between -45F and +45F
          and for windspeeds between 3mph and 60mph

    Parameters:
        t: The temperature in units of F (float)
        v: The windspeed in units of mph (float)
    """

    wci= t-0.7*v
    return wci




def compute_heatindex(t,hum):
    """
    Compute the heat index given temperature and humidity
    Parameters:
        t: The temperature in units of F (float)
        hum: The relativie humidity in units of % (float)
    """
    a=-42.379
    b=2.04901523
    c=10.14333127
    d=-0.22475541
    e=-6.83783E-3
    f=-5.481717E-2
    g=1.22874E-3
    h=8.5282E-4
    i=-1.99E-6

    rh=hum/100

    hi = (a+(b*t) + (c*rh) + (d*t*rh) + \
         (e*t**2) + (f*rh**2) + (g*t**2 * rh) + \
          (h*t*rh**2) + (i*t**2 * rh**2))
    return hi

#def compute_dewpoint(t,h):
#    """
    
#    Compute the dewpoint temperature given the temperature and humidity

#    """
#    tempC= (t-32)*5/9
#    rh=h/100
#    b=18.678
#    c=257.14

#    gamma=math.log(rh)+(b*tempC)/ (c+tempC)
#    tdp=c*gamma/(b-gamma)
