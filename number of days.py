# Find out the number of days between the two given dates.

import pandas as pd
import numpy as np
from datetime import datetime

x=pd.to_datetime('22-02-2019',format='%d-%m-%Y')
y=pd.to_datetime('3-09-2016',format='%d-%m-%Y')
z = x-y
print(z)
