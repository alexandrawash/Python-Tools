def toSeconds(x, unit):
    '''Convert some length `x` into seconds,
        assuming it starts with units `unit`. 
    
    Parameters
    ----------
    x : float
        A number representing some length.
    unit : str
        A string saying the units in which that length is defined.
        
    Returns
    -------
    x_in_seconds: float
        The length converted to units of astronomical units.
    ''' 
    
    # 1 minute = 60 seconds
    # 1 minute in seconds:
    minute = 60
    
    # 1 hour = 60 minutes
    # 1 hour in seconds:
    hour = 60 * minute

    # 1 day = 24 hour
    # 1 day in seconds:
    day = 24 * hour

    # 1 year = 365.25 days
    # 1 year in seconds:
    year = 365.25 * day
    
    Sec_conv = {'minutes':minute, 'hours':hour, 'days':day, 'years':year} 
    # Calculate the conversion
    
    x_in_seconds = (x * Sec_conv[unit])
    # and return the product
    return x_in_seconds
