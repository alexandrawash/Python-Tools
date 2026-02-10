def toAU(x, unit):
    '''Convert some length `x` into astronomical units,
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
        The length converted to units of astronomical units.
    '''
    # 1 AU = 1.5e11 meters
    # 1 meter in AU:
    m_AU = 1 / 1.5e11
    
    # 1 AU in km: 1.5e8
    # 1 km in AU:
    km_AU = 1 / 1.5e8
    
    AU_conv = {'m':m_AU, 'km':km_AU} 
    # Calculate the conversion
    
    x_in_AU = (x * AU_conv[unit])
    # and return the product
    return x_in_AU
