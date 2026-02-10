# import necessary elements
import numpy as np
# ----------------------------------------------------------------------------
# establish constant numbers
c=2.99792458e8   # speed of light constant, (m/s)
h=6.62607015e-34   # Planck constant, (J*s)
k=1.380649e-23   # Boltzmann constant, (J/K)
b=2.897771955e-3   # Wien's constant (m*K)
T=5800 #Temperature
# ----------------------------------------------------------------------------
def B(w):
    '''
    Planck function
    --------------------
    Input: wavelengths, array, (m)
    Return: intensity at each wavelength, array, (W/m^3)
    '''
    return (2*h*c**2) / ( (w**5) * (np.e** ((h*c) / (k*T*w)) - 1 ))   # the Planck function, (W/m^3), array 
