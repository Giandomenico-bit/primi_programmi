# Si scriva un programma che trovi la soluzione a equazioni di primo grado
# nella forma ax + b = 0, con a e b interi.
# Il programma dovrebbe tener conto dei casi
# particolari: a, b o entrambi nulli.

print( "Equazione ax + b = 0" )

a = input( "Inserisci un valore per a : ")
print( a, "x + b = 0" )
b = input( "Inserisci un valore per b : ")
print( a, "x +", b, "= 0" )

a = int( a )
b = int( b )

if a == 0 and b == 0 :
    print( "L'equazione ammette infinite soluzioni" )
elif a == 0 :
    print( "Equazione impossibile" )
else :
    x = -( float( b ) / float( a ) )
    print( "Il valore di x e' : ", x )
