# Risoluzione equazione secondo grado
# attraverso l'utilizzo del discriminante

from math import sqrt

print( "Equazione : ax^2 + bx + c = 0" )

a = input( "Inserisci il valore di a : ")
b = input( "Inserisci il valore di b : ")
c = input( "Inserisci il valore di c : ")

a = int( a )
b = int( b )
c = int( c )

if a == 0 and b == 0 and c == 0 :
    print( "L'equazione ammette infinite soluzioni" )

elif a == 0 and b == 0 :
    print( "L'equazione non ammette soluzioni" )

elif a == 0 :
    x = -( b / c  )
    print( "Soluzione :",x )

else :

delta = b * b - ( 4.0 * a * c )

    if delta > 0 :

        x1 = ( -b + sqrt( delta ) ) /  2.0 * a
        x2 = ( -b - sqrt( delta ) ) /  2.0 * a
        print( "L'equazione ha fornito le seguenti soluzioni : x1 =",x1,"e x2 =",x2 )

    elif delta == 0  :
        x = -( b / 2.0 * a )
        print( "L'equazione ha fornito la seguente soluzione : x1 = x2 =",x )

    else :
        print( "L'equazione non ha soluzioni reali" )
