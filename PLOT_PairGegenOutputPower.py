import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

Eff_numb_Bragg77  = pd.read_csv('Eff_numb_Bragg77.7nm.txt',sep='\t',header=None)
Eff_numb_Bragg77 = pd.DataFrame(Eff_numb_Bragg77)

eff1 = Eff_numb_Bragg77[1]


Eff_numb_Bragg130nm = pd.read_csv('Eff_numb_Bragg130nm.txt',sep='\t',header=None)
Eff_numb_Bragg130nm = pd.DataFrame(Eff_numb_Bragg130nm)

eff2 = Eff_numb_Bragg130nm[1]

plt.xticks(np.arange(0, 20, step=1))
plt.xlabel("Number of Bragg pairs")
plt.ylabel("Output Power (fraction)")
plt.plot(Eff_numb_Bragg77[0], Eff_numb_Bragg77[1],'b.')
plt.plot(Eff_numb_Bragg130nm[0], Eff_numb_Bragg130nm[1],'g.')
plt.axhline(eff1.loc[eff1.idxmax()], color='r', linestyle='--')
plt.axhline(eff2.loc[eff2.idxmax()], color='r', linestyle='--')
plt.savefig('Number_of_Bragg_pairs.png')
