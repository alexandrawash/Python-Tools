# import necessary elements
from math import sqrt
from math import pi
# ----------------------------------------------------------------------------
def PlanetRadiusEarthRadii(StarRadius, TransitDepth):
    '''
    Takes in the star radius in solar radii, converts to meters.
    Then takes TransitDepth guess and rearranges the previous function
    to solve for exoplanet radius in Earth radii
    '''    

    #solar radii = 695,700 km = 695700000 meters
    StarRadius_meters = StarRadius * 695700000
        
    planetrad = sqrt(TransitDepthGuess * (StarRadius_meters ** 2))

    EarthRadius_meters = 6371000
    PlanetRadiusEarthRadii = planetrad / EarthRadius_meters
    
    return PlanetRadiusEarthRadii #in Earth radii
# ----------------------------------------------------------------------------
PlanetEarthRadius = PlanetRadiusEarthRadii(0.2, TransitDepthGuess)
print(PlanetEarthRadius, "my planet's radius in Earth radii")
