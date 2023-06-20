import matplotlib.pyplot as plt
import numpy as np

# Plage de valeurs de n
n = np.arange(0, 21)


# Calcul des valeurs de 2^n
y = 2**n

# Tracer le graphique
plt.plot(n, y, "o-")

# Ajouter des étiquettes aux axes
plt.xlabel("n")
plt.ylabel("2^n")

# Afficher la grille
plt.grid(True)

# Afficher le graphique
plt.show()
