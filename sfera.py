#Calcolo superficie e volume
#di una sfera

import math

radius = input( "Enter radius : ")
radius = int( radius )   #cast esplicito

area = 4.0 * math.pi * radius * radius
volume = 4.0/3.0 * math.pi * radius * radius * radius

print( "Area is : ", area )
print( "Volume is : ", volume )
