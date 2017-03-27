import os
from numpy import *
S0=100.
K=105.
T=1.0
r=0.05
sigma=0.2
I=100000
Z=random.standard_normal(I)
ST=S0*exp((r - 0.5 *sigma ** 2) *T+sigma*sqrt(T) * Z)
hT=maximum(ST -K,0)
C0=exp(-r*T) * sum(hT) /I
print(C0)