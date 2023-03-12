import numpy as np


## np.eye(3) Identidad n = 3
class SimplexP:
    #TODO
    def __init__(self, c, A, b):
        # Debo buscar una solución básica factible
        self.__z = 0
        self.__A = A #Coeficientes de las variables en las resticciones
        self.__c = c #Coeficientes de las variables en la solución
        self.__b = b #Terminos independientes de las restricciones
        self.__B = 0 #Matriz de coeficientes de las variables en las restricciones que forman la base
        self.__N = 0 #Matriz de coeficientes de las variables en las restricciones que no forman la base
        self.__m, self.__n = A.shape #num restricciones, num variables
        self.__theta = 0
        self.__direct = 0

    def do_simplex(self):
        self.__first_phase()
        self.__second_phase()
    #TODO
    def __first_phase(self):
        ## Afegir variables artificials
        self.__Af = self.__A
        for x in range self.__m:
            column = np.zeros(self.__m)
            column[x] = 1
            np.c_[ self.__Af, column]
    #TODO
    def __second_phase(self):
        pass