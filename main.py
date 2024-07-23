import numpy as np
import matplotlib.pyplot as plt

# Paramètres 
t = np.linspace(0, 2 * np.pi, 1000)
x = 16 * np.sin(t)**3
y = 13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t)

# Tracer la courbe
plt.figure(figsize=(6, 6))
plt.plot(x, y, color='red')
plt.title('Courbe en forme de cœur')
plt.xlabel('x')
plt.ylabel('y')
plt.axis('equal')
plt.grid(True)

# Afficher la courbe
plt.show()
