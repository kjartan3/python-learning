# modules allow us to import pre-written Python code

import mod2  # importing the mod2 module
import data2 # importing the data2 module 
import data3 as nn 
from mod2 import myName # importing the myName variable from mod2 module

mod2.welcome(myName['first'], myName['last'])
mod2.welcome(data2.myName['first'], data2.myName['last'])
mod2.welcome(nn.myName['first'], nn.myName['last'])  # Using nn as an alias for data3 module


total = mod2.adder(3, 5)
print(total)