# import necessary elements
import numpy as np
# ----------------------------------------------------------------------------
def spherevolume(r):
    
    if (r > 0):    
        volume = ((np.pi)*(4/3)*(r*r*r));
        print(volume)

    if (r < 0):
        print(f"You gave me the value {r}, I can't deal with negative values.")
        r = "None"
        print(r)
