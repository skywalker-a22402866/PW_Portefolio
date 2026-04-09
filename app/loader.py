from app.models import *
import json

with open('app/data/tfcs.json') as f:

    tfcs = json.load(f)

    for tfc in tfcs:
        print(f"titulo: {tfc['titulo']} | Resumo: {tfc['resumo']}")
        break
    