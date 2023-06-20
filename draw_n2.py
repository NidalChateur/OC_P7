import matplotlib.pyplot as plt


def plot_function():
    x = range(21)  # Plage de valeurs de n (0 à 9)
    y = [n**2 for n in x]  # Calcul des valeurs de la fonction n^2

    plt.plot(x, y)  # Tracé de la courbe
    plt.xlabel("n")  # Légende de l'axe x
    plt.ylabel("n^2")  # Légende de l'axe y
    plt.title("Tracé de la fonction n^2")  # Titre du graphique
    plt.grid(True)
    plt.show()  # Affichage du graphique


plot_function()
