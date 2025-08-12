import numpy as np
import matplotlib.pyplot as plt

# Example: Potential well energy levels (conceptual)
V0 = 50
a = 1
E_values = np.linspace(-V0 + 1e-6, -1e-6, 1000)

plt.axhline(0, color='gray', ls='--')
plt.plot(E_values, np.tan(np.sqrt(V0 + E_values) * a))
plt.xlabel('Energy (E)')
plt.ylabel('Function value')
plt.title('Finite Square Well Example')
plt.show()
