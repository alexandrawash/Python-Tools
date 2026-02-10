# import necessary elements
import numpy as np
# ----------------------------------------------------------------------------
def centralDerivative(f, x, h): 
    """
    Estimate the numerical derivative of
    function f at positions x using a step size of h
    using the central difference method.
    Parameters
    ----------
    f : func
    the function you want to differentiate
    
    x : np.array
    an array of x positions at which you want the derivative
    
    h : float 
    the stepsize to use for the numerical derivative
    """ 
    return ((f(x+h))-(f(x-h)))/(2*h)
