def toMeters(x, unit):
    '''Convert some length `x` into meters,
        assuming it starts with units `unit`. 
    
    Parameters
    ----------
    x : float
        A number representing some length.
    unit : str
        A string saying the units in which that length is defined.
        
    Returns
    -------
    x_in_AU: float
        The length converted to units of meters.
    '''
    # 1 centimeter in meters: 
    cm_m = 1 / 100
    
    # 1 meter in meters:
    m = 1
    
    # 1 kilometer in meters: 
    km_m = 1000

    # 1 AU in meters:
    # 150 million km = 1 AU
    AU_m = 150e6 * km_m
    
    m_conv = {'cm':cm_m, 'm':m, 'km':km_m, 'AU':AU_m} 
    # Calculate the conversion
    
    x_in_m = (x * m_conv[unit])
    # and return the product
    return x_in_m
