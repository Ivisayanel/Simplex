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
notbasic = [1,4,5]
An = A[0:,notbasic[0]]
for x in notbasic[1:]:
    An = np.c_[An, A[0:, x]]
cn = []
for x in notbasic:
     cn += [c[x]]
cn = np.array(cn)

Binv = np.eye(3)
cn = np.array([0,0])
cb = np.array([-1, -2])
Binv = np.array([[1, -1], [-1, 2]])
An = np.array([[1,0], [0,1]])

r = cn - cb @ Binv @ An
#print(r)
print(A)
print()
print(A[0:,3])
# An[0,0] = 9999
# print()
# print(A)
# print(An)
# cI = np.array([0 for x in range(5)])
# cI = np.c_[cI, np.array([1 for x in range(5)])]
