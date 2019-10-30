# Risoluzione equazione secondo grado
# attraverso l'utilizzo del discriminante

from math import sqrt

print( "Equazione : ax^2 + bx + c = 0" )
print( "" )

a = input( "Inserisci il valore di a : ")
b = input( "Inserisci il valore di b : ")
c = input( "Inserisci il valore di c : ")

a = float( a )
b = float( b )
c = float( c )

delta = b * b - ( 4.0 * a * c )
print( "" )

if delta > 0 :

    x1 = ( -b + sqrt( delta ) ) /  2.0 * a
    x2 = ( -b - sqrt( delta ) ) /  2.0 * a
    print( "Soluzioni : x1 =",x1,"e x2 =",x2 )

elif delta == 0 :

        x = -( b / 2.0 * a )
        print( "Soluzioni : x1 = x2 =",x )

else :

    print( "L'equazione non ha soluzioni reali" )
