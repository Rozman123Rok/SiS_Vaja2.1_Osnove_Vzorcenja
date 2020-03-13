# SiS_Vaja2.1_Osnove_Vzorcenja
## Navodila:
Osnove vzorčenja

Demonstrirajte osnovna znanja vzorčenja signalov z implemetacijo generatorja tonov.

Pripravite Python skripto ki ima definirane (vsebuje) naslednje funkcije:

### def generiraj_ton_mono(cas, vzorcevalna_frekvenca, bitna_locljivost, frekvenca_tona):

funkcija prejme 4 parametre
čas v sekundah, ki pove dolžino generiranega signala
vzorčevalno frekvenco v hercih, ki pove koliko vzorcev na sekundo je v signalu
bitno ločljivost v bitih, ki pove maksimalno natančnost posameznega vzorca
frekvenco tona v hercih, ki pove frekvenco generiranega tona
funkcija vrne vektor (tipa numpy array oblike (x, 1))
vrnjen vektor naj bo pravega tipa (int8, int16, int32, ali int64)
velikosti generiranih vzorcev naj bodo med
MAX(2^bitna_ločljivost)/2 - 1
-MAX(2^bitna_ločljivost)/2
ton ja bo generiran v obliki sinusuide
začnite z vrednostjo 0 (ignorirajte fazo)
(5 točk)
Pripravite še odsek kode katero lahko lahko samostojno zaženete kot demo:

if __name__ == '__main__':

pripravite demo katerega lahko poženete
generirate ton
čas 1 sekunda
vzorčevalna frekvenca 10 Hz
bitna ločljivost 8 bitov
frekvenca tona 5 Hz
izpiši generiran vektor
 

Zahtevano implementacijo oddajte v datoteki generiraj.py.
