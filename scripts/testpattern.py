#!/usr/bin/env python
# create an observation centered at the north ecliptic pole (midlatitude)
from SPyFFI.Observation import Observation, default

# start from the default settings
inputs = default

inputs['camera']['label'] = 'newtest'
inputs['catalog']['name'] = 'testpattern'
inputs['camera']['subarray'] = 4000
inputs['expose']['jitterscale'] = 100.0
inputs['expose']['skipcosmics'] = True
inputs['catalog']['testpatternkw']['randomizemagnitudes'] = True
inputs['observation']['cadencestodo'] = {1800:9}#, 120:16, 1800:16}
o = Observation(inputs)

#o.create()
