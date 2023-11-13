"""
configuriamo il sistema di registrazione dei log utilizzando il modulo `logging` in Python.
Ecco una spiegazione del codice:

1. `logging_str`: Questa variabile contiene una stringa di formato che specifica come i messaggi di log devono essere formattati. La stringa contiene segnaposto tra parentesi quadre come `%(asctime)s`, `%(levelname)s`, e `%(message)s` che verranno sostituiti con i valori effettivi quando vengono registrati i messaggi.
Questa stringa definisce il formato dei messaggi di log e include la data e l'ora (`asctime`), il livello di log (`levelname`) e il messaggio stesso (`message`).

2. `log_dir`: Questa variabile specifica il percorso della directory in cui verranno archiviati i file di log. Questa directory deve essere creata se non esiste.

3. `log_filepath`: Questa variabile contiene il percorso completo del file di log. Combina il percorso della directory dei log (`log_dir`) con il nome del file (`running_logs.log`) utilizzando `os.path.join()`.

4. `os.makedirs(log_dir, exist_ok=True)`: Questa istruzione crea la directory dei log (`log_dir`) se non esiste già. Il parametro `exist_ok=True` garantisce che non venga generato un errore se la directory esiste già.

5. `logging.basicConfig()`: Questa funzione configura il sistema di registrazione dei log in Python. Accetta vari argomenti:
   - `level=logging.INFO`: Imposta il livello di registrazione al livello `INFO`, il che significa che verranno registrati messaggi di log di livello `INFO` e superiori. È possibile modificare il livello a seconda delle proprie esigenze.
   - `format=logging_str`: Specifica il formato dei messaggi di log utilizzando la stringa di formato definita in `logging_str`.
   - `handlers`: Specifica i gestori di log da utilizzare. In questo caso, vengono utilizzati due gestori:
     - `logging.FileHandler(log_filepath)`: Questo gestore registra i messaggi di log in un file specificato da `log_filepath`.
     - `logging.StreamHandler(sys.stdout)`: Questo gestore invia i messaggi di log al flusso standard di output (console).

6. `logger = logging.getLogger("textSummarizerLogger")`: Questa istruzione crea un oggetto logger personalizzato chiamato "textSummarizerLogger" utilizzando il modulo `logging`. Questo logger personalizzato può essere utilizzato per registrare messaggi di log specifici per il progetto "textSummarizer". È possibile utilizzare questo logger nei vari componenti del progetto per registrare messaggi di log con il formato specificato in `logging_str`.

In sintesi, questo codice imposta un sistema di registrazione dei log per il progetto "textSummarizer". Definisce il formato dei messaggi di log, crea una directory per i file di log, imposta due gestori per la registrazione su file e su console, e crea un logger personalizzato chiamato "textSummarizerLogger" che può essere utilizzato per registrare messaggi di log in tutto il progetto.

"""
import os
import sys
import logging

logging_str = "[%(asctime)s: %(levelname)s: %(message)s]"
log_dir = "logs"
log_filepath = os.path.join(log_dir,"running_logs.log")
os.makedirs(log_dir,exist_ok = True)

logging.basicConfig(level = logging.INFO,
                    format = logging_str,
                    handlers = [logging.FileHandler(log_filepath),logging.StreamHandler(sys.stdout)]
                    )
logger = logging.getLogger("textSummarizerLogger")
