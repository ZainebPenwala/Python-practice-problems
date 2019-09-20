# From the given date find the day of on that date.
# { %A = day , %d = date, %b = month, %y = year}


import pandas as pd 
import numpy as np
from datetime import datetime

date = "20Sept1959"
a=pd.to_datetime(date)
print(a)
b=a.strftime("%A %d %B %Y")
print(b)
