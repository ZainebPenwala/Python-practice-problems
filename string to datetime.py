from datetime import datetime
from datetime import date
from datetime import tim

import pandas as pd 
import numpy as np

a = pd.to_datetime('Jan 1 2014 2:43PM')
print(a)


## to convert unix timestamp string to readable datetime format

b = pd.Timestamp(1284105682,unit='s')
print("expected output = ", b)
