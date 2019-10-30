# Calcolo  della durata massima di volo
# di un aeroplano dati in input la quantità
# di carburante (in galloni) e il consumo orario (in galloni/h).

carburante = input( "Carburante ( in galloni ) : ")
consumo = input( "Consumo orario ( in galloni/h ) : ")

carburante = float( carburante )
consumo = float( consumo )

ore = carburante / consumo

hour = int( ore )
resto = ore - hour
minuti = 60 * resto

min = int( minuti )
resto = minuti - min

secondi = 60 * resto
sec = int( secondi )

print( "Tempo di volo : ", hour ,"h", min , "min", sec ,"sec" )
