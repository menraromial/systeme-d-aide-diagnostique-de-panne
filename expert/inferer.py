from rdflib import Graph, Namespace, RDF, RDFS, OWL, Literal


def get_solution(panne_label):

    # Chargement de l'ontologie depuis un fichier RDF
    g = Graph()
    g.parse("static/data/pannes.owl", format="xml")

    # Création du namespace pour notre ontologie
    ns = Namespace("http://example.com/ontologie/pannes#")

    # Récupération du label de panne saisi par l'utilisateur
    label_panne = panne_label

    solutions_labels=[]
    marques_labels=[]
    composant_labels=[]
    types_solution_labels=[]
    types_panne_labels=[]
    # Recherche de la panne correspondante dans l'ontologie
    pannes = set(g.subjects(RDF.type, ns.Panne))
    panne = None
    for p in pannes:
        label = g.value(p, RDFS.label)
        if label is not None and label.lower() == label_panne.lower():
            panne = p
            break

    if panne is not None:
        # Inférence des solutions associées à la panne
        solutions = set(g.objects(panne, ns.aPourSolution))
        #solutions_labels = set()
        marques = set()
        #marques_labels = set()
        for s in solutions:
            label = g.value(s, RDFS.label)
            marque = g.value(s, ns.estAssocieALaMarque)
            if label is not None:
                solutions_labels.append("{}".format(label))
            if marque is not None:
                #marques.add(marque)
                label = g.value(marque, RDFS.label)
                if label is not None:
                    marques_labels.append("{}".format(label))
        
        # Inférence des composant associées aux pannes liés à la panne
        composants = set(g.objects(panne, ns.aPourComposant))
        #composant_labels=set()
        for c in composants:
            label = g.value(c, RDFS.label)
            if label is not None:
                composant_labels.append("{}".format(label))
        # Inférence des types de solutions associés à la panne
        types_solution = set()
        #types_solution_labels = set()
        for s in solutions:
            type_solution = g.value(s, ns.aPourType)
            if type_solution is not None:
                types_solution.add(type_solution)
                label = g.value(type_solution, RDFS.label)
                if label is not None:
                    types_solution_labels.append("{}".format(label))

        # Inférence des types de pannes associés à la panne
        types_panne = set(g.objects(panne, ns.aPourType))
        #types_panne_labels = set()
        for tp in types_panne:
            label = g.value(tp, RDFS.label)
            if label is not None:
                types_panne_labels.append("{}".format(label))
    
    context={
        'solutions': solutions_labels,
        'marques': marques_labels,
        'composant': composant_labels
    }

    return context
