# import necessary elements
import numpy as np
# ----------------------------------------------------------------------------
def spherevolume(r):
    
    if (r > 0):    
        volume = ((np.pi)*(4/3)*(r*r*r));
        return(volume)

    if (r < 0):
        print(f"You gave me a radius of {r}, I can't deal with negative values.")
        volume = "None"
        return(volume)
