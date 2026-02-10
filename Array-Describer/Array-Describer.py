# import necessary elements
import numpy as np
# ----------------------------------------------------------------------------
# Array Describing Function:
def describe(a):
    '''Summarize the basic characteristics of an array.'''

    print(f"number of dimensions is {a.ndim}")
    print(f"shape is {a.shape}")
    print(f"the minimum value is {a.min()}")
    print(f"the maximum value is {a.max()}")
    print(f"the standard deviation is {np.std(a)}") #using numpy standard deviation command
    print(f"the 1st percentile is {np.percentile(a, 1)}")
    print(f"the 99.9th percentile is {np.percentile(a, 99.9)}")
