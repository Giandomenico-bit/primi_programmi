# Si scriva un programma che calcoli il volume
# di un cubo o di una sfera in base ad una
# scelta effettuata dall'utente. Se l'utente sceglie di
# calcolare il volume di un cubo, il programma
# chiederà l'input del relativo lato,
# altrimenti chiederà il raggio della sfera.

import math

print( "Calcolo del volume di un cubo o di una sfera" )

print( "1 - cubo, 2 - sfera" )
scelta = input( "? " )

scelta = int( scelta ) # cast esplicito

if scelta == 1 :
    lato = input( "Lato del cubo : ")
    lato = int( lato )

    volume = lato**3
    print( "Il cubo di lato", lato, "ha volume", volume )

elif scelta == 2 :
    raggio = input( "Raggio della sfera : ")

    raggio = int( raggio ) #cast esplicito
    volume = 4.0 / 3.0 * math.pi * raggio**3

    print( "La sfera di raggio", raggio, "ha volume", volume )

else :
    print( "Numero non valido" )
