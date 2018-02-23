![arteco][1]
***


# 8.1.4 UDINE

## FEATURE: DC_ADS_FILTERSEARCH
- __Active Directory__: E' stata introdotta la possibilità di effettuare ricerche filtrate sui gruppi di dominio di Active Directory in modo da:
    1. Poter lavorare su una lista ridotta di gruppi.
    2. Gestire le query sui server di dominio in cui sono configurati più di 1000 gruppi e utenti, in quanto 1000 è il numero massimo di oggetti che possono essere ritornati da una query AD.

## BUGFIXES
- __Active Directory__: Corretto (forse) bug che poteva causare un crash nel next durante la navigazione delle pagine dei gruppi di dominio di server diversi.
***

# 8.1.3 TRAPANI

## FEATURE: DC_TEST_PLAY
- __Next__: In monoplay viene aumentata a 8x la velocità limite per la riproduzione avanti/indietro di TUTTI i frames di uno stream archiviato. Superato questo limite vengono riprodotti solo i key-frames. Fanno eccezione, come sempre, gli streams non strutturati (es. MJPEG).
***

# 8.1.2 (TORNA A) SORRENTO

## FEATURE: DC_PERIPHERALS_ON_LAYOUT
- __Next__ : Implementata la seconda parte del progetto di indagine evoluta: "Drag&Drop di Periferiche sul Layout". Le periferiche possono ora essere trascinate negli slot di un layout in ambiente Live al pari delle telecamere e delle mappe. La vista contiene l' icona  standard associata al dispositivo e la sua descrizione, le funzionalità sono analoghe a quelle delle icone inserite in una mappa. Per ulteriori dettagli si rimanda alla documentazione del relativo progetto.
- __Next__ : Implementata la possibilità di cambiare runtime l'icona delle periferiche di I/O nelle viste di tipo security.

## BUGFIXES
- __Next__ : Modificata la gestione della lista dei dispositivi nel pannello delle proprietà dei layouts: la precedente gestione causava un'errata visualizzazione della lista e della griglia in caso di associazioni molto numerose (>20).
- __Next__ : Gestione della retrocompatibilità quando le periferiche vengono trascinate su layout remoti appartenenti a server di versioni precedenti.
- __Next__ : Gestione del caricamento di periferiche a layout tramite il reticolo del videowall.
- __Next__ : Gestione del menu contestuale sulle viste con periferiche.
- __Next__ : Inserita voce di menu "Modifica layout" nel menu contestuale dei layout remoti appartenenti a server di versioni precedenti.
- __Next__ : Corretto Bug che non allineava in configurazione i layout aggiunti o rimossi con quelli del server a cui ci si collega.
- __Next__ : Corretto Bug che non caricava i layout alla connessione di un server in caso questi fossero spostati su un frame secondario non più attivo.
- __Next__ : Impostato attivo di default il flag populate del nodo layout in configurazione che sposta il fuoco all'ultimo tab a dx quando ci si collega ad un server.
***

# 8.1.1 SORRENTO

## FEATURE: DC_ADV_INVEST
- __Next & Server__ : Implementate le funzionalità descritte nel progetto "Indagine Evoluta". Di seguito la feature principali:
    1. Possibilità di associare a un dispositivo (telecamera, periferica, server) uno e un solo layout in modo che quest'ultimo  si possa richiamare dal menu contestuale del dispositivo stesso, dal menu contestuale di una riga del log eventi, da un pulsante del pannello eventi e dalle viste che visualizzano il live delle telecamere.
    2. L'associazione viene effettuata utilizzando la finestra di dialogo per la creazione di un layout nella quale è stato aggiunto un albero contenente i dispositivi che è possibile associare al layout in creazione/modifica. L'associazione viene effettuata spuntando direttamente i dispositivi sull'albero.
    3. Quando sull'albero principale è selezionato un layout che possiede dispositivi associati, questi ultimi vengono elencati nel pannello delle proprietà del layout.
  
  Per ulteriori dettagli si rimanda alla documentazione del relativo progetto.

## FEATURE: PB_OCFONTSIZE
- __Open Connector__ : aggiunti i campi "displacement x e y" per gestire lo spostamento dell'etichetta dell'OSD relativamente all'angolo in alto a sinistra. questi valori sono da intendersi come percentuali rispetto ad altezza e larghezza dell'immagine.
- __Open Connector__ : aggiunta il campo font-size per gestire la dimensione del carattere OSD, Ora la stringa OSD gestisce anche il fine riga.

## FEATURE: ANDROID
- __Mobile__ : Viene spedito anche il timestamp del frame all'interno di un header HTTP.
- __Android__ : Abbozzati i controlli "base" per la gestione di interruzione\ripresa flusso MJPEG.
- __Android__ : Viene recepito il timestamp del frame spedito da Arteco Mobile.
- __Android__ : Rifatta da zero la parte di visualizzazione a schermo delle immagini ottenute da Arteco Mobile.
- __Android__ : Spostamento componente joystick in apposità Activity dedicata al brandeggio PTZ -> il componente, lato XML, è stato inglobato fra i Basic Player Controls.
- __Android__ : Migliorata la gestione dei Cookies: ora il Cookie Store ragiona per HOST, quindi ogni server avrà i propri cookies associati (vale, ad oggi, solo per i SessionId).
- __Android__ : Ottimizzazione threading per brandeggio PTZ.
- __Android__ : Rimossa la Splash Screen.
- __Android__ : Aggiunta gestione barra dei pulsanti per: accedere alle registrazioni, visualizzare \ nascondere pannello controlli PTZ, visualizzare \ nascondere layout I/O e sharing delle immagini con altre app.
- __Android__ : Implementazione fullscreen LIVE e REC.
- __Android__ : Implementata selezione \ deselezione di tutte le telecamere di un server.
- __Android__ : Aggiunta pagina "About".
- __Android__ : Aggiunta la pagina "Settings".
- __Android__ : Aggiunta la possibilità di scegliere la porta HTTP dell'Arteco Mobile cui connettersi.
- __Android__ : E' possibile configurare i timeout di rete tramite la pagina "Settings".
- __Android__ : E' possibile inibire \ disinibire la ricezione delle notifiche server per server.
- __Android__ : E' possibile visualizzare \ nascondere il timestamp dei frame nella visualizzazione LIVE e REC.
- __Android__ : E' possibile effettuare il play di una nuova registrazione direttamente da visualizzazione REC.
- __Android__ : Si può scegliere l'intervallo di tempo da decurtare quando viene presentata la scelta della DATA e dell'ORA utilizzata per il play delle registrazioni.
- __Android__ : Ora si può scegliere la qualità delle immagini in streaming e la velocità di brandeggio PTZ.
- __Android__ : Viene gestita la conversione dei timestamp e del tempo iniziale del playback del registrato da e verso UTC.
- __Android__ : Adesso si può specificare l'immagine da associare ad un layout, sia essa ottenuta dallo storage del dispositivo oppure dalla fotocamera.
- __Android__ : Viene utilizzata la libreria "Glide" per la manipolazione delle immagini (utile specialmente per l'immagine da associare ai layout).

## BUGFIXES
- __Android__ : Migliorata login verso i server Arteco. Ora viene recuperata anche la lista delle tlc contenstualmente al login.
- __Android__ : Pulizia codice delle nuove activity: questo migliora e corregge alcune problematiche inerenti al funzionamento delle tile dei server e delle telecamere.
- __Android__ : Fix sulle notifiche FCM.
- __Android__ : Migliorata la gestione del PagerAdapter nell'activity dedicata alla griglia TLC.
- __Android__ : Corretto il comportamento in fase di editing di un layout che causava doppioni e perdita di TLC associate al layout originale (e dunque NO telecamere nemmeno per quello editato).
- __Android__ : Incrementati i Frames Per Second: da 1 di default a 25. Per ora è tutto hard-coded: in futuro il valore sarà configurabile.
- __Android__ : La "condivisione" dei frames LIVE e\o REC fra apps è ora implementata.
- __Next__ : Mappe con link ad altre mappe: fix errata cancellazione dei link a mappe presenti.
- __Server__ : Corretto sistema di notifica degli stati dei pins degli EveryWhere usati come IO-Devices.

***
# 8.1.0 RAVENNA
## FEATURE: MHM_SAVE_MY_WINDOWS
- __Next__ : Entra il ripristino dei layouts remoti dopo un login nelle finestre principale e secondarie d'origine.  
Resta sempre valida la funzionalità del flag caricamento al login, ovvero i layout remoti saranno visualizzati dov'erano solo se il suddetto flag è abilitato. Introdotto un sotto nodo <layout> nel file di configurazione con la mappatura dei layouts remoti dato dal ID della finestra, il codename del server e l'handle del layout.

        <layouts>
            <workspace path="C:\Arteco\vision\develop\_work\ArtecoLogic\x64\xlayouts"/>
            <layout>
            <layout idframe="-1" rl-code="eda0c3fbe1941a039ba4bcc58bf357c" rl-node="63"/>
            ...
            ...
            </layout>
        </layouts>
  
  Le funzionalità introdotte sono le seguenti:
    1. Al login, si popola ricavando l'IdFrame dalla mappa presente nel file di configurazione. Se non esiste alcuna mappatuta per un dato HSERVER, allora si aggiorna la mappa con tutti i layout remoti che hanno il flag visualizza al login abilitato indirizzandole solo sulla finestra principale.
    2. Al logout, la mappa di IdFrame non si modifica.
    3. Quando si crea un layout remoto, con il flag caricamento al login abilitato, siaggiorna la mappa di IdFrame.
    4. Quando si rimuove un layout remoto dall'albero dei dispositivi, si aggiorna la mappadi IdFrame.
    5. Quando si chiude un layout remoto dall'area dei layout, la mappa di IdFrame non si modifica.
    6. Quando si sposta un layout remoto tra finestre, si aggiorna la mappa di IdFrame.
    7. Quando si modifica il flag caricamento al login, si aggiorna la mappa di IdFrame.
  
  Dopo il login, si attiva l'ultimo layout nell'area dei layouts delle finestre secondarie impostanto il flag populate="1" nel nodo /layouts/layout del file di configurazione

***
# 7.4.2 QUEBEC_2

## FEATURE: DC_SNAPSHOTS
- __Next e Server__ : Implementato lo streaming delle snapshots generate in seguito ad eventi di analisi, eventi LPR, ed input allarmanti.  
Lo streaming si attiva impostando il corrispondente profilo live come profilo di default sulla tabella dei profili di rete o direttamente sulle viste dei layouts dal menu contestuale. Per maggiori chiarimenti su tutte le features implementate fare riferimanto alle specifiche definite nel relativo progetto.
- __Next e Server__ : Gestione del profilo live "snapshots" in multiselezione.
- __Next e Server__ : Accordata la geometria dei controlli nella pagina di configurazione dei profili live.
- __Next e Server__ : Rinominate le funzioni DDX_XXXX(), DDV_XXXX() utilizzate in multiselezione nel DataEcxhange per distinguerle dalle corrispondenti funzioni native MFC.
- __Next__ : SETUP telecamera: modificati alcuni testi nella maschera di impostazione parametri del Plugin/Input-Output/Input Disabilitanti.

## BUGFIXES
- __Next e Server__ : Bugfixes vari nella gestione del TabControl dei profili live in multiselezione.
- __Next e Server__ : Corretto errore che impediva di scegliere la sorgente video nei canali Wisenet.
- __Next e Server__ : Aggiunto il supporto al modello Wisenet "PNM-9081VQ".
- __Next e Server__ : Corretto [bug 4139](http://bugzilla.arteco.it/show_bug.cgi?id=4139) "Layout non caricati al login". Aggiunta gestione layout corrotti o inesistenti:  Sono stati identificati 2 casi in cui il bug può presentarsi:
    1. Uno dei layout caricati è danneggiato e il caricamento di questi è sospeso.  In tal caso il Logic ora si accorge di questa anomalia e comunica al server di eliminare il Layout incriminato per poi proseguire il caricamento.
    2. Nel BaseConfig è presente un layout che nel filesystem non c'è.  Ora il server al caricamento della configurazione controlla l'effettiva esistenza del layout su filesystem, il client quando ne trova uno di questo tipo lo scarta e prosegue il caricamento. 
- __Next__ : Corretti problemi sull'inversione dei piani colore per alcune snapshots.
- __Next__ : Risolti alcuni piccoli memory leaks.
- __Next__ : Corretto un problema di retrocompatibilità nella pagina di configurazione dei profili live.
- __Next__ : Risolti alcuni memory leaks.
- __Next__ : Risolto un problema per cui il pannello di proprietà degli eventi veniva ripulito nel caso in cui venisse cancellata la relativa riga sul log degli eventi. Questo diventava un problema nel caso in cui gli eventi venivano ordinati per data crescente ( il più vecchio in alto ), perché l'autocancellazione degli eventi del log pteva comportare lo sbiancamento di un evento appena aperto.
- __Next__ : Mappe con link ad altre mappe: fix errata cancellazione dei link a mappe presenti.
- __Onvif__ : miglioria grafica alla pagina di configurazione, ora se il canale secondario è disabilitato, non viene più mostrato il tab corrispondente al secondario tra i profili live.
- __Open Connector__ : Risolto problema che poteva impedire l'accesso alle immagini tramite protocollo HTTPS nel caso in cui il server remoto richieda certificati SSL. risolve il caso di Selea: [bug 4183](http://bugzilla.arteco.it/show_bug.cgi?id=4183 ).  
_NOTA_: la risoluzione è consistita nell'ignorare la richiesta di certificati da parte di un server SSL, questa soluzione è lecita, ma parziale, perché se è vero che il server può richiedere un certificato SSL, ma accettare il fatto che tu non ne fornirai uno, secondo il protocollo per i server remoti è altrettanto lecito non proseguire con l'autenticazione.  
_NOTA 2_: Questa risuluzione potrebbe non funzionare se il client dovesse essere installato su Windows XP.
- __Server__ : Corretto errore introdotto con il ramo TREE_MULTISELECT che poteva ripristinare i default alle configurazioni di filezilla all'avvio del server.
- __Server__ : Corretto errore che poteva impedire la corretta visualizzazione della sorgente numero 4 dei canali Wisenet.
- __Server__ : Corretti problemi aggiornamento stato dei pin di input e di output dei dispositivi Everywhere usati come IODevice.
- __Server__ : Corretto problema salvataggio mask-flag notifica eventi pin di input dei dispositivi Everywhere usati come Peripheral, se si disabilitava e successivamente si riabilitava il pin il flag non si ripristinava correttamente.
- __Server__ : Corretto sistema di notifica degli stati dei pins degli EveryWhere usati come IO-Devices.
- __Server__ : Corretta errore che impediva il controllo di IO controller IBASE (sostituita la .dll).
- __Onvif__  : Corretto problema che poteva portare ad una cattiva interpretazione dell'elenco delle sorgenti video.
- __Onvif__  : migliorata compatibilità con alcune chiamate per la descrizione delle opzioni delle sorgenti video e degli encoder. [bug 4167](http://bugzilla.arteco.it/show_bug.cgi?id=4167)
- __Onvif__  : corretto errore che impediva la corretta gestione dell'attributo di modifica nei campi "profilo" e "sorgente" dei canali Onvif , poteva impedire il corretto salvataggio di questi dati. [bug 4167](http://bugzilla.arteco.it/show_bug.cgi?id=4167)
- __Onvif__ : Corretto bug introdotto con il TREE_MULTISELECT che impediva ad un canale Onvif di partire automaticamente dopo la creazione, non riuscendo a selezionare in automatico la sorgente. [bug 4167](http://bugzilla.arteco.it/show_bug.cgi?id=4167)
- __Server__ : Corretto bug che impediva ai canali di tipo AXIS e WISENET id patire con i corretti default sulla sorgente da utilizzare. [bug 4167](http://bugzilla.arteco.it/show_bug.cgi?id=4167)
- __Onvif__ : Corretto bug presente da sempre ( ma peggiorato con il TREE_MULTISELECT ) che poteva impedire in alcune situazioni di salvare il corretto profilo in modalità "automatica".[bug 4167](http://bugzilla.arteco.it/show_bug.cgi?id=4167)
- __Input Disabilitanti (Plugin delle telecamere)__: i Pins di Input delle IO Peripheral abilitano/disabilitano correttamente la generazione degli eventi correlati della telecamera. [bug 4178](http://bugzilla.arteco.it/show_bug.cgi?id=4178).  
- __Onvif__ : corretto bug che portava il secondario a partire sempre come disabilitato sul canale secondario.
- __Mobile__ : Corretto bug introdotto con la build [1768] che impediva la corretta rigenerazione di alcune parti della configurazione del mobile quando questo dovesse risultare assente. [bug 4180](http://bugzilla.arteco.it/show_bug.cgi?id=4180).  




[1]: https://www.arteco-global.com/i/arteco-logo-bianco.png
