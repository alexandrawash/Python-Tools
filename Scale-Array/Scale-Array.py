def ScaleArray(array, scale):
    '''Scales an array.
        If you want to scale UP: enter a real number.
        If you want to scale DOWN: enter a fraction.
    
    Parameters
    ----------
        masses: 1D array
        An array of the values you want scaled.
        scale: float
        The factor by which you want your array scaled
    Returns
    -------
        np.ndarray: 1D array
        Array of the scaled values.
    '''
    scaled_array = array * scale
    return scaled_array
