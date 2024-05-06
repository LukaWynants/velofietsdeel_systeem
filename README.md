# verslag

## programma starten
Clone de repository met:

    git clone https://github.com/LukaWynants/velofietsdeel_systeem.git

Start het programma starten met:

    python main.py

nu krijg je dit menu:

    $ python main.py 
    [NOTE] choose Load existing data set if you want to use your simulated data from the simulation mode

                1: create new data set
                2: Load existing data set
                3: Start Simulation mode
        :
Hier kun je kiezen tussen het aanmaken van een nieuwe dataset, het laden van een dataset vanuit users.pkl, stations.pkl en bikes.pkl, of het starten van de simulatie.

## simulatie modus

De simulatiemodus laat voor een bepaald aantal seconden willekeurige gebruikers een fiets lenen en terugbrengen naar een willekeurig slot in een willekeurig station.
Je kunt de simulatiemodus starten via het menu of met:

    python main.py -s

Nu krijg moet je ingeven hoelang de simulatie moet uitvoeren:

    $ python main.py -s
    [NOTE] The data simulated will be saved automatically and used until you create a new data set

    Input for how long you want to run the simulation (in seconds):
Voer hier het aantal seconden in dat de simulatie moet duren.

## Fiets lenen/ontlenen

