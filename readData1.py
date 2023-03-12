import numpy as np

c = []
A = []
b = []

with open(f'./Data/S1.txt', 'r', encoding = 'UTF-8') as f:
    f.readline()
    content = f.readline().split()
    c = [eval(i) for i in content]
    content = f.readline()
    while content[0] != "A":
            content = f.readline()
    content = f.readline()
    while content[0] != "\n":
        A += [[eval(i) for i in content.split()]]
        content = f.readline()
    f.readline()
    content = f.readline()
    b = [eval(i) for i in content.split()]

c = np.array(c) #Coeficientes de las variables en la solución
A = np.array(A) #Coeficientes de las variables en las resticciones
b = np.array(b) #Terminos independientes de las restricciones
column = np.zeros(4)
column[1] = 1
print(column)