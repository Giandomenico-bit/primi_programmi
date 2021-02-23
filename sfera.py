# Creare un programma sfera.py che stampi
# superficie e volume di una sfera dato il raggio (intero).

# Per portare a termine il compito è
# necessaria la costante pi greco. Si può
# utilizzare il valore già definito nella
# libreria matematica: import math

import math

raggio = input( "Inserisci raggio : ")
raggio = int( raggio )   # cast esplicito

area = 4.0 * math.pi * float( raggio**2 )
volume = 4.0 / 3.0 * math.pi * float( raggio**3 )

print( "Area : ", area )
print( "Volume : ", volume )
