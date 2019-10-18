from graph import *

# (230,230,230) - grey color
# (0,255,255) - sky color
# (170,255,255) - sun color
# (230,230,230) - bear color


def elipsfill(x,y, x0, y0, a, b)  :
    if ( (x-x0)**2/(a**2) + (y-y0)**2/(b**2) <= 1):
        return True
    else :
        return False
    
def elipsboard (x,y, x0, y0, a, b):
    e = 0.2
    if ( (x-x0)**2/(a**2) + (y-y0)**2/(b**2) <= 1+e
         and
         (x-x0)**2/(a**2) + (y-y0)**2/(b**2) >= 1-e) :
        return True
    else :
        return False
    
def contur_elips(x0,y0, a, b):
    for x in range(x0-a,x0+a):
        for  y in range(y0-b,y0+b):
            if elipsboard (x,y, x0, y0, a, b):
                 point (x,y,"black")           
def elips(x0, y0, a, b, color):
    for x in range(x0-a,x0+a):
        for  y in range(y0-b,y0+b):
            if elipsfill(x,y, x0, y0, a, b):
                point(x,y,color)

windowSize(420,600)
canvasSize(420,600)
brushColor(159,199,247)
rectangle(0, 0, 420, 90 )
brushColor(200,171,55)
rectangle(0, 90, 420, 340 )
brushColor(55,200,113)
rectangle(0, 340, 420, 600 )
for i in range(15):
    line(28+i*28,90, 28+i*28,340)
brushColor(200,171,55)
polygon([(340, 480), (340,380), (270,360), (270,450)])
polygon([(340, 480), (340,380), (365,360), (365,435)])
brushColor(212,160,0)
polygon([ (340,380), (270,360), (310,315)])
polygon([ (340,380), (365,360),(335,300), (310,315)])
elips(305,415,20,25,  (0,0,0))
for i in range(10):
    contur_elips(285-i*5,435+i*5, 5+7*(i%2),5+7*((i+1)%2) )
for j in range(3):
    contur_elips(235-j*6,475+j*3, 5+7*(j%2),5+7*((j+1)%2) )
contur_elips(200,480, 20, 10)

elips(90,460,45,30,  (108,103,83))
elips(144,447,25,19,  (108,103,83))
elips(124,440,13,12,  (108,103,83))
elips(100,503,15,30,  (108,103,83))
elips(50,490,15,30,  (108,103,83))
elips(160,463,15,20,  (108,103,83))
elips(172,490,5,20,  (108,103,83))
elips(136,475,5,20,  (108,103,83))
elips(47,522,14,6,  (108,103,83))
elips(95,535,14,6,  (108,103,83))
elips(132,495,10,4,  (108,103,83))
elips(169,509,10,4,  (108,103,83))

brushColor(108,103,83)
rectangle(43,415,100,476)

circle(98,426,10)
circle(42,426,10)


elips(60,439,5,2,  (255,255,255))
elips(78,439,5,2,  (255,255,255))
contur_elips(60,439, 6, 2)
contur_elips(78,439, 6, 2)
brushColor(0,0,0)
circle(60,439,2)
circle(78,439,2)

points = [53,468],[55,464],[59,460], [66,458],[72,458],[79,460],[84,464],[86,468],      
polyline(points)
brushColor(255,255,255)
polygon([ (55,464), (59,460),(57,454)])
polygon([ (84,464), (79,460),(83,454)])
run()
