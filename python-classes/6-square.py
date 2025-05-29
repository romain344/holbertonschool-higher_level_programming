#!/usr/bin/python3
"""Définit une classe Square avec getter, setter, area et my_print."""


class Square:
    """Classe qui représente un carré avec contrôle d'accès à size."""

    def __init__(self, size=0):
        """Initialise la taille du carré (par défaut 0)."""
        self.size = size  # Utilise le setter pour validation

    @property
    def size(self):
        """Getter pour récupérer la taille du carré."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter pour définir la taille du carré avec vérification."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Retourne l'aire du carré."""
        return self.__size ** 2

    def my_print(self):
        """Affiche le carré avec des '#' dans stdout.

        Si size est 0, affiche une ligne vide.
        """
        if self.__size == 0:
            print()
            return

        for _ in range(self.__size):
            print("#" * self.__size)