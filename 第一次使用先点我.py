import numpy as np
list = [
    'Green scan time:', 0,
    'Yellow scan time:', 0,
    'Red scan time:', 0
    ]
m = np.array(list)
np.save('number', m)