# import necessary elements
import numpy as np
# ----------------------------------------------------------------------------
def estimateRGB(wavelengths, fluxes):
    """
    This function estimates the RGB color of an object, from its spectrum.
    It calculates the integrals the flux over wavelength ranges
    that correspond roughly to the red, green, and blue colors
    displayed on computer monitors.
    
    Arguments:
    wavelengths = a numpy array of wavelengths, in nanometers
    fluxes = a numpy array of fluxes, corresponding to w
    
    Returns:
    an RGB color, expressed as a three-element array,
    with R as the first element, G the second, B the third

    """
    
    #integrate the color areas
    RedArea = integrateSpectrum(wavelengths, fluxes, 565, 660)
    GreenArea = integrateSpectrum(wavelengths, fluxes, 485, 570)
    BlueArea = integrateSpectrum(wavelengths, fluxes, 400, 490)
    
    #Put all of our RGB areas into a numpy array
    RGB = np.array([RedArea, GreenArea, BlueArea])
    
    maximum = np.max(RGB)
    
    return RGB / maximum
