from sympy import symbols, diff, sqrt, Piecewise, Abs, cos, plotting

x, y = symbols('x y', real=True)
def surfaceStep(center):
    a = Piecewise((1, Abs(x-center[0]) < 1/(0.64*center[2])), (0, True))
    b = Piecewise((1, Abs(y-center[1]) < 1/(0.64*center[3])), (0, True))
    return a*b

def objectSpaceWave(center):
    return cos(center[2]*(x-center[0])) * cos(center[3]*(y-center[1]))

def expoDecayCorner(w, h, m):
    a2 = Piecewise((1/Abs(x+0.000001), (w - m/2 < Abs(x))), (1, True))
    a3 = Piecewise((1/Abs(w-x+0.000001), (Abs(x) < m/2)), (1, True))

    b2 = Piecewise((1/Abs(y+0.000001), (h - m/2 < Abs(y))), (1, True))
    b3 = Piecewise((1/Abs(w-y+0.000001), (Abs(y) < m/2)), (1, True))

    return a2 * a3 * b2 * b3

def world(w, h, m):
    a = Piecewise((1, (0 < Abs(x)) & (Abs(x) < w)), (0, True))
    b = Piecewise((1, (0 < Abs(y)) & (Abs(y) < h)), (0, True))

    return a * b * expoDecayCorner(w, h, m)

def objectsGraph(objects):
    objectsMap = 0

    for obj in objects:
        objectsMap += (objectSpaceWave(obj) * surfaceStep(obj))

    return objectsMap

def pointScoreMSQD(objects, ds = 0):
    f = 0
    for obj in objects:
        f += sqrt((x - obj[0] + ds)**2 + (y - obj[1]+ds)**2)
    return 10-f

def negRan(st, si):
    return [st + i for i in range(si)]
    

#  Not useful, too much recursion 
def fitting(world, size):
    f = 0
    for i in negRan(-int(size/2), size):
        for j in negRan(-int(size/2), size):
            f += world.evalf(subs={x:x+i,y:y+j})
    return f


objFit = 2
objs = [[5,5, 1 + 0.64 - 1/objFit, 1 + 0.64 - 1/objFit]]
obj = objectsGraph(objs)
score = pointScoreMSQD(objs)
worldObjectMap = world(10, 10, objFit) - obj

plotting.plot3d(worldObjectMap*score, (x, 0, 10), (y, 0, 10))
# plotting.plot3d(worldObjectMap, (x, 0, 10), (y, 0, 10))

# plotting.plot3d(world()), (x, -5, 5), (y, -5, 5)