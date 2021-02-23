# Utilizzando il linguaggio Python, si scriva un programma
# che chieda all'utente di inserire un importo (intero)
# in dollari e poi mostri come pagarlo utilizzando
# il minor numero di biglietti da 20, 10, 5 e 1.
# Il programma tenga conto di eventuali input negativi.
# In tal caso stampi un opportuno messaggio di errore.

importo = input( "importo ( dollari ) : " )
importo = int( importo )

print( "" )

if importo >= 0 :

    banconota20 = importo / 20
    banconota20 = int( banconota20 )

    importo = importo % 20
    banconota10 = importo / 10
    banconota10 = int( banconota10 )

    importo = importo % 10
    banconota5 = importo / 5
    banconota5 = int( banconota5 )

    importo = importo % 5
    banconota1 = importo / 1
    banconota1 = int( banconota1 )

    print( "Biglietti da $20 : ", banconota20 )
    print( "Biglietti da $10 : ", banconota10 )
    print( "Biglietti da $5  : ", banconota5 )
    print( "Biglietti da $1  : ", banconota1 )

else :
    print( "L'importo non puo' essere negativo" )
