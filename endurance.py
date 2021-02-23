# Utilizzando il linguaggio Python, determinare
# la durata massima di volo di un aeroplano dati
# in input la quantità di carburante (in galloni)
# e il consumo orario (in galloni/h).

# Il programma tenga conto di eventuali
# input negativi. In tal caso stampi un
# opportuno messaggio di errore.

carburante = input( "Carburante ( in galloni ) : ")
consumo = input( "Consumo orario ( in galloni/h ) : ")

carburante = float( carburante )
consumo = float( consumo )

if carburante < 0 or consumo < 0 :
    print( "L'input non puo' essere negativo" )

else :
    ore = carburante / consumo

    resto = ore - int( ore )
    minuti = 60 * resto

    resto = minuti - int( minuti )
    secondi = 60 * resto

print( "Tempo di volo : ", int( ore ) ,"h", int( minuti ) , "min", int( secondi ) ,"sec" )
