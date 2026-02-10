def toDay(x, unit):
    '''Convert some length `x` into days,
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
        The length converted to units of days.
    '''
    # 1 year = 365.25 days
    # 1 year in days:
    year = 365.25

    # 1 day:
    day = 1
    
    # 1 hour = 1/24 day
    # 1 hour in days:
    hour = day / 24

    # 1 minute = 1/60 hour
    # 1 minute in days:
    minute = 1 / hour

    # 1 second = 1/60 minute
    # 1 minute in days:
    second = 1 / minute
    
    Dayconv = {'seconds':second, 'minutes':minute, 'hours':hour, 'days':day, 'years':year} 
    # Calculate the conversion
    
    x_in_days = (x * Dayconv[unit])
    # and return the product
    return x_in_days
