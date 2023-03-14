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
        self.__basic = 0
        self.__theta = 0
        self.__direct = 0

    def do_simplex(self):
        z = self.__first_phase()
        if z == 0:
            print("primera fase z es 0")
            self.__second_phase()
    #TODO
    def __first_phase(self):
        ## Afegir variables artificials
        self.__AI = self.__A.copy()
        for x in range (self.__m):
            column = np.zeros(self.__m)
            column[x] = 1
            np.c_[ self.__AI, column]
        Im, In = self.__AI.shape
        self.__cI = np.array([0 for x in range(self.__n)])
        self.__cI = np.r_[self.__cI, np.array([1 for x in range(ix)])]
        self.__Ibasic = [x for x in range(self.__n, ix)] #Variables básicas de la primera fase
        self.__Inotbasic = [x for x in range(self.__n)] #Varialbes no básicas de la primera fase
        self.__IB = np.eye(ix - self.__n)
        self.__IBinv = np.eye(ix - self.__n)
        self.__IN = self.__A.copy()
        self.__Ix = np.r_[np.array([0 for x in range(self.__n)]), self.__b]
        z = self.__second_phase(self.__AI, self.__cI, self.__IB, self.__IBinv, self.__Ibasic, self.__Inotbasic, self.__b, In)
        if z > 0:
            print("Problema no factible")
        return z
    #TODO
    def __second_phase(self, A, c, B, Binv, basic, notbasic, b, n, iter = 0):
        #Se debe actualizar bien B y Binv para que funcione.
        ######## Primera etapa
        xN = np.array([0 for x in range(len(notbasic))])
        xb = np.matmul(Binv, b)
        An = A[[notbasic]]
        cb = c[[basic]]
        cn = c[[notbasic]]
        z = np.matmul(cb, xb)
        ######## Fin primera etapa
        ######## Segunda etapa
        r = cn - cb @ Binv @ An
        lst = []
        i = 0
        for x in r:
            lst += [(x, notbasic[i])]
            i += 1
        q = min(lst)[1]