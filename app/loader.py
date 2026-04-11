from app.models import *
import json

with open('app/data/tfcs.json') as f:

    Tecnologia.objects.all().delete()
    Docente.objects.all().delete()
    TFC.objects.all().delete()

    tfcs = json.load(f)
    tecnologias = set()
    orientadores = set()
    tfcs_lidos = set()

    for tfc in tfcs:
        if tfc.get('tecnologias') and tfc.get('tipo')=="TFC":
            for tecnologia in tfc['tecnologias']:
                tecnologias.add(tecnologia)          

        if tfc.get('orientador') and tfc.get('tipo')=="TFC":
            for orientador in tfc['orientador']:
                orientadores.add(orientador)

    #print(f"titulo: {tfc['titulo']} | Resumo: {tfc['resumo']} | Tecnologias {tfc['tecnologias']}")
    #print (orientadores)
    for tecnologia in tecnologias:
        Tecnologia.objects.create(nome=tecnologia)
    for orientador in orientadores:
        Docente.objects.create(nome=orientador)

    for tfc in tfcs:
         prof=""
         if tfc.get('tipo')=="TFC" and tfc.get('tecnologias'):
            orientadores = tfc.get('orientador')
            prof = Docente.objects.get(nome=orientadores[0])
            

            bd = TFC.objects.create(nome=tfc['titulo'],
                                    resumo=tfc['resumo'],      
                                    docente=prof)

            for tecnologia in tfc['tecnologias']:
                #tecnologias = tfc.get('tecnologias') or []
                print (tfc['titulo'],tecnologia)
                tec = Tecnologia.objects.get(nome=tecnologia)
                #tech_objs = Tecnologia.objects.filter(nome__in=tecnologias)
                #bd.tecnologias.set(tech_objs)
                bd.tecnologias.add(tec)
