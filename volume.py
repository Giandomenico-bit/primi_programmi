# implementazione del costrutto
# selettivo if-else

import math

print( "Calcolo del volume di un cubo o di una sfera" )

print( "1 - cubo, 2 - sfera" )
choice = input( "? " )

choice = int( choice )
if choice == 1 :
    side = input( "Lato del cubo : ")
    side = float( side )
    
    volume = side * side * side
    print( "Il cubo di lato", side, "ha volume", volume )

elif choice == 2 :
    radius = input( "Raggio della sfera : ")

    radius = float( radius )
    volume = 4.0/3.0 * math.pi * radius * radius * radius

    print( "La sfera di raggio", radius, "ha volume", volume )

else :
    print( "Numero non valido" )
