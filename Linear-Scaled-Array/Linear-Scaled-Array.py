# import necessary elements
import numpy as np
# ----------------------------------------------------------------------------
def LinearScale(masses, scale=1.0):
    '''Scales an array of values linearly.
    
    Parameters
    ----------
        masses: 1D array
        An array of the values you want scaled.
        scale: float

    Returns
    -------
        np.ndarray: 1D array
        Array of the scaled values.
    '''
    # Set the masses to an array if they aren't already
    Masses = np.array(masses) 

    # Scale
    scaled_array = (Masses / np.max(Masses) * 100 * scale)
    
    return scaled_array
