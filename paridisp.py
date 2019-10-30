# Numero pari o dispari

value = input( "Enter a value : ")
value = int( value ) #cast esplicito

if value & 1 :
    print( "Il numero e' dispari" )
else :
    print( "Il nuemro e' pari" )
