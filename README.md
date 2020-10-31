# OISISI-Projekat-Python
Potreban Interpreter: Python 3.7    
Program pretstavlja search engine za izabran skup html fajlova.

Prilikom pokretanja programa ponudjene su 4 opcije:     
1 - Parsiranje datoteka    
2 - Pretraga    
3 - Prikaz rezultata    
0 - Izlaz

1. Parsiranje datoteka: Vrsi parsiranje html datoteka nad odabranim korenskim direktorijumom.
Program nudi nadovezivanje na treutnu putanju: 
    - 'y': korisnik treba da unese relativnu putanju u odnosu na trenutnu (ili '.' za trenutni)
    - 'n': ukoliko zeli unos apsolutne putanje.     
HINT: Putanja mora biti postojeca i mora pretstavljati direktorijum!        
2. Pretraga: Izbacuje podmeni koji nudi opcije:     
   2.1. - Standardna pretraga: [rec1 rec2 rec3 ...]: Pretraga unosom 1 ili vise reci    
   2.2. - Logicka pretraga:    [rec1 OP rec2]  *OP = {AND, OR, NOT}:
            Pretraga pomocu logickih upita. Moguce je uvezati samo 2 reci.
            U ovom slucaju reci and, or, not (case-insensitive) pretstavljaju logicke operatore:    
            - AND - Pretraga stranica koje sadrze obe reci        
            - OR - Pretraga stranica koje sadrze barem jednu od reci      
            - NOT - Pretraga stranica koje sadrze prvu a ne sadrze drugu rec  
   2.0. - Napusti opciju : Povratak u glavni meni    
3. Prikaz rezultata: Prikazuje rezultate na vise stranica.
    Promena broja linkova po stranici se menjaju unosom 'N' karakteraz a zatim i zeljeni broj prikaza po stranici
    Setanje kroz rezultate moguce je:
    - prostim unosom rednog broja stranice
    - next: prelazak na sledecu stranu
    - prev: prelazak na prethodnu stranu    
    HINT: Najbolji rezultati su prikazani na pocetku!
0. Izlaz: Zatvaranje aplikacije
    
Autori:         
Stefan Kitanovic RA192/2017        
Gojko Novcic RA208/2017