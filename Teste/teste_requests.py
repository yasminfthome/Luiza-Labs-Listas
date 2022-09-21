import requests
import logging

logging.basicConfig(level=logging.ERROR, filename="Teste/logs_example_requests.log")

try:
    r = requests.get('https://www.google.com/nothere')
    r.raise_for_status()
    print("Acessado com sucesso!")
    
except requests.exceptions.HTTPError as Err:
    raise SystemExit(Err)
