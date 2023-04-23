import astropy.constants.iau2015 as aconst
import astropy.constants.codata2018 as coconst
import numpy as np


'''
[Package to scale units to natural units](https://en.wikipedia.org/wiki/Natural_units).

Planck Units
------------
`l_p`: Length.
`m_p`: Mass.
`t_p`: Time.
'''
l_p = np.sqrt((coconst.hbar.value*coconst.G.value)/((coconst.c.value)**3))
m_p = np.sqrt((coconst.hbar.value*coconst.c.value)/coconst.G.value)
t_p = np.sqrt((coconst.hbar.value*coconst.G.value)/((coconst.c.value)**5))