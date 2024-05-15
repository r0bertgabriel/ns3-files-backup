#%%
import matplotlib.pyplot as plt
import numpy as np
#%%
x = np.arange(0,101,10)
y = np.full_like(x, 65.0099)
plt.plot(x, y)
plt.xlabel('x')
plt.xticks(range(0, 101, 10))
plt.ylabel('y')
plt.legend()
plt.show()
# %%
