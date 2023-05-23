import numpy as np
from math import pi, sqrt


def evaluate(degree, x, y):
    return [1] + [x**i for i in range(1, degree + 1)] + [y**i for i in range(1, degree + 1)]



def approximate(degree, samples, rMax, rDiff, thetaDiff, breakingR):
    coeffLst = []
    resultLst = []

    currentR = 0
    resultApproximater = 0

    while currentR < rMax:
        currentTheta = 0
        while currentTheta < 2*pi:
            x = currentR/2
            y = sqrt(3)*currentR/2
            coeffLst.append(evaluate(degree, x, y))
            resultLst.append(min(max(0, resultApproximater), 1))

            if (currentR > breakingR):
                resultApproximater -= 1/breakingR
            else:
                resultApproximater += 1/breakingR
            
            currentTheta += thetaDiff
        
        currentR += rDiff


    coeffMat = np.matrix(coeffLst)
    resultMat = np.matrix(resultLst)

    return np.linalg.inv(coeffMat.transpose()*coeffMat)*(coeffMat.transpose()*resultMat.transpose())


a = approximate(10, 0, 100, 0.01, 0.1, 50)
a2 = (list(a.flat))
equ = ""
for i in range(len(a2)):
    if i == 0:
        equ += str(a2[i])
    elif i < 11:
        equ += "+" + str(a2[i]) + "*x^" + str(i)
    else:
        equ += "+" + str(a2[i]) + "*y^" + str(i-10)

print(equ)