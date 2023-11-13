"""
template.py crea una struttura di directory e file di base per un progetto chiamato "textSummarizer".
Questo script esegue le seguenti operazioni:
1. Importa i moduli necessari:
   - `os`: Fornisce funzionalità per l'interazione con il sistema operativo.
   - `Path` dalla libreria `pathlib`: Fornisce un'interfaccia orientata agli oggetti per la manipolazione di percorsi e file.
   - `logging`: Gestisce la registrazione dei messaggi di log.
2. Configura la registrazione dei log:
   - Imposta il livello di registrazione su `INFO`, il che significa che verranno registrati messaggi di livello `INFO` e superiori.
   - Definisce un formato per i messaggi di log che include la data e l'ora `[%(asctime)s]` e il messaggio effettivo del log `%(message)s`.
3. Imposta il nome del progetto come "textSummarizer" e crea una lista di percorsi dei file che devono essere creati.
   Questi percorsi includono directory e file di inizializzazione per il progetto.
4. Itera attraverso la lista di percorsi e:
   - Converte ogni percorso in un oggetto `Path`.
   - Divide il percorso in directory (`filedir`) e nome del file (`filename`).
   - Verifica se la directory (`filedir`) esiste e, se non esiste, la crea in modo ricorsivo utilizzando `os.makedirs`.
   - Verifica se il file non esiste o ha dimensione zero e, in tal caso, crea un file vuoto utilizzando `open(filepath, 'w')`.

Inoltre, il codice registra messaggi di log informativi in base alle operazioni eseguite. Ad esempio, registra quando viene creata una directory o un file vuoto, o se il file esiste già.
Questo script è utile per inizializzare la struttura del progetto, creando le directory e i file in modo che il progetto sia pronto per l'uso.
È particolarmente utile quando si crea un nuovo progetto e si vuole organizzare la struttura delle directory e dei file in modo coerente.
"""

import os
from pathlib import Path
import logging

#configurazione di base (imposto il progetto in modo che in futuro possa essere rilasciato nel cloud per es. con AWS)
logging.basicConfig(level=logging.INFO,format = '[%(asctime)s]:%(message)s:')
project_name = "textSummarizer"
list_of_files = [
    "github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/conponents/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "test.py"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory:{filedir} for the file {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass
            logging.info(f"Creating empty file:{filepath}")
    else:
        logging.info(f"{filename} is already exists")

        