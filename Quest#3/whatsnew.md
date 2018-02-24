## BUGFIXES
- __Active Directory__: Corretto (forse) bug che poteva causare un crash nel next durante la navigazione delle pagine dei gruppi di dominio di server diversi.
- __Next__ : Implementata la possibilità di cambiare runtime l'icona delle periferiche di I/O nelle viste di tipo security.
- __Next__ : Corretto Bug che non allineava in configurazione i layout aggiunti o rimossi con quelli del server a cui ci si collega.
- __Next__ : Corretto Bug che non caricava i layout alla connessione di un server in caso questi fossero spostati su un frame secondario non più attivo.
- __Next__ : Impostato attivo di default il flag populate del nodo layout in configurazione che sposta il fuoco all'ultimo tab a dx quando ci si collega ad un server.
- __Mobile__ : Viene spedito anche il timestamp del frame all'interno di un header HTTP.
- __Android__ : Rimossa la Splash Screen.
- __Android__ : E' possibile configurare i timeout di rete tramite la pagina "Settings".
- __Android__ : E' possibile effettuare il play di una nuova registrazione direttamente da visualizzazione REC.
- __Next e Server__ : Corretto [bug 4139](http://bugzilla.arteco.it/show_bug.cgi?id=4139) "Layout non caricati al login". Aggiunta gestione layout corrotti o inesistenti:  Sono stati identificati 2 casi in cui il bug può presentarsi:
    1. Uno dei layout caricati è danneggiato e il caricamento di questi è sospeso.  In tal caso il Logic ora si accorge di questa anomalia e comunica al server di eliminare il Layout incriminato per poi proseguire il caricamento.
    2. Nel BaseConfig è presente un layout che nel filesystem non c'è.  Ora il server al caricamento della configurazione controlla l'effettiva esistenza del layout su filesystem, il client quando ne trova uno di questo tipo lo scarta e prosegue il caricamento. 
- __Open Connector__ : Risolto problema che poteva impedire l'accesso alle immagini tramite protocollo HTTPS nel caso in cui il server remoto richieda certificati SSL. risolve il caso di Selea: [bug 4183](http://bugzilla.arteco.it/show_bug.cgi?id=4183 ).  
_NOTA_: la risoluzione è consistita nell'ignorare la richiesta di certificati da parte di un server SSL, questa soluzione è lecita, ma parziale, perché se è vero che il server può richiedere un certificato SSL, ma accettare il fatto che tu non ne fornirai uno, secondo il protocollo per i server remoti è altrettanto lecito non proseguire con l'autenticazione.  
_NOTA 2_: Questa risuluzione potrebbe non funzionare se il client dovesse essere installato su Windows XP.
- __Onvif__ : Corretto bug presente da sempre ( ma peggiorato con il TREE_MULTISELECT ) che poteva impedire in alcune situazioni di salvare il corretto profilo in modalità "automatica".[bug 4167](http://bugzilla.arteco.it/show_bug.cgi?id=4167)
