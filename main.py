import sys
import os
# Ottieni il percorso assoluto di main.py
script_path = os.path.abspath(__file__)

# Costruisci il percorso della cartella "src" dal percorso di main.py
src_path = os.path.join(os.path.dirname(script_path), 'src')

# Aggiungi il percorso della cartella "src" al sys.path
sys.path.append(src_path)

from textSummarizer.logging import logger

logger.info("Welcome to out custom logging")