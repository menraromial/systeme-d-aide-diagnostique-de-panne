from rdflib import Graph, Namespace, RDF, RDFS, OWL, Literal
import re
from data.data import panne_data
from rdflib.tools.rdf2dot import rdf2dot
import graphviz

def to_camel_case(string):
    # Remove all special French characters from the string
    string = re.sub('[^a-zA-Z0-9_]+', ' ', string)
    # Convert string to title case and remove spaces
    string = string.title().replace(' ', '')
    # Lowercase the first character
    string = string[0].lower() + string[1:]
    return string


# Création du namespace pour notre ontologie
ns = Namespace("http://example.com/ontologie/pannes#")

# Création du graph RDF
g = Graph()

# Ajout des classes OWL à l'ontologie
g.add((ns.Panne, RDF.type, OWL.Class))
g.add((ns.Composant, RDF.type, OWL.Class))
g.add((ns.Solution, RDF.type, OWL.Class))
g.add((ns.TypeDePanne, RDF.type, OWL.Class))
g.add((ns.TypeDeSolution, RDF.type, OWL.Class))
g.add((ns.MarqueDOrdinateur, RDF.type, OWL.Class))

# Ajout des propriétés OWL à l'ontologie
g.add((ns.aPourComposant, RDF.type, OWL.ObjectProperty))
g.add((ns.aPourSolution, RDF.type, OWL.ObjectProperty))
g.add((ns.aPourType, RDF.type, OWL.ObjectProperty))
g.add((ns.estAssocieALaMarque, RDF.type, OWL.ObjectProperty))

# Ajout des sous-classes et des domaines/ranges pour les propriétés
g.add((ns.Panne, RDFS.subClassOf, OWL.Thing))
g.add((ns.Composant, RDFS.subClassOf, OWL.Thing))
g.add((ns.Solution, RDFS.subClassOf, OWL.Thing))
g.add((ns.TypeDePanne, RDFS.subClassOf, OWL.Thing))
g.add((ns.TypeDeSolution, RDFS.subClassOf, OWL.Thing))
g.add((ns.MarqueDOrdinateur, RDFS.subClassOf, OWL.Thing))

g.add((ns.aPourComposant, RDFS.domain, ns.Panne))
g.add((ns.aPourComposant, RDFS.range, ns.Composant))
g.add((ns.aPourSolution, RDFS.domain, ns.Panne))
g.add((ns.aPourSolution, RDFS.range, ns.Solution))
g.add((ns.aPourType, RDFS.domain, ns.Panne))
g.add((ns.aPourType, RDFS.range, ns.TypeDePanne))
g.add((ns.aPourType, RDFS.domain, ns.Solution))
g.add((ns.aPourType, RDFS.range, ns.TypeDeSolution))
g.add((ns.estAssocieALaMarque, RDFS.domain, ns.Composant))
g.add((ns.estAssocieALaMarque, RDFS.range, ns.MarqueDOrdinateur))
g.add((ns.estAssocieALaMarque, RDFS.domain, ns.Solution))
g.add((ns.estAssocieALaMarque, RDFS.range, ns.MarqueDOrdinateur))

# Ajout de labels pour une meilleure compréhension de l'ontologie


g.add((ns.Panne, RDFS.label, Literal("Panne")))

g.add((ns.Composant, RDFS.label, Literal("Composant")))
g.add((ns.Solution, RDFS.label, Literal("Solution")))
g.add((ns.TypeDePanne, RDFS.label, Literal("Type de panne")))
g.add((ns.TypeDeSolution, RDFS.label, Literal("Type de solution")))
g.add((ns.MarqueDOrdinateur, RDFS.label, Literal("Marque d'ordinateur")))
g.add((ns.aPourComposant, RDFS.label, Literal("a pour composant")))
g.add((ns.aPourSolution, RDFS.label, Literal("a pour solution")))
g.add((ns.aPourType, RDFS.label, Literal("a pour type")))
g.add((ns.estAssocieALaMarque, RDFS.label, Literal("est associé à la marque")))


# Création des individus

for key, value in panne_data.items():

    composant = to_camel_case(panne_data[key]['composant'])
    typeP = to_camel_case(panne_data[key]['type_panne'])
    typeSol = to_camel_case(panne_data[key]['type_solution'])
    marque = to_camel_case(panne_data[key]['marque'])
    p = to_camel_case(panne_data[key]['panne'])
    sol = to_camel_case(panne_data[key]['solution'])


    panne_name = f"panne{key}"
    #panne_uri = ns[panne_name]
    panne_uri = ns[p]

    composant_uri = ns[composant]

    #solution_name = f"solution{key}"
    solution_uri = ns[sol]

    marque_uri = ns[marque]

    typePane_uri = ns[typeP]

    typeSolution_uri = ns[typeSol]

    # Ajout de données à notre graphe RDF
    g.add((panne_uri, RDF.type, ns.Panne))
    g.add((composant_uri, RDF.type, ns.Composant))
    g.add((solution_uri, RDF.type, ns.Solution))
    g.add((typePane_uri, RDF.type, ns.TypeDePanne))
    g.add((typeSolution_uri, RDF.type, ns.TypeDeSolution))
    g.add((marque_uri, RDF.type, ns.MarqueDOrdinateur))

    # Ajout des propriétés pour lier les individus
    g.add((panne_uri, ns.aPourComposant, composant_uri))
    g.add((panne_uri, ns.aPourSolution, solution_uri))
    g.add((panne_uri, ns.aPourType, typePane_uri))
    g.add((solution_uri, ns.aPourType, typeSolution_uri))
    g.add((composant_uri, ns.estAssocieALaMarque, marque_uri))
    g.add((solution_uri, ns.estAssocieALaMarque, marque_uri))

    #Ajout des labels
    g.add((panne_uri, RDFS.label, Literal(panne_data[key]['panne'])))
    g.add((composant_uri, RDFS.label, Literal(panne_data[key]['composant'])))
    g.add((solution_uri, RDFS.label, Literal(panne_data[key]['solution'])))
    g.add((typePane_uri, RDFS.label, Literal(panne_data[key]['type_panne'])))
    g.add((typeSolution_uri, RDFS.label, Literal(panne_data[key]['type_solution'])))
    g.add((marque_uri, RDFS.label, Literal(panne_data[key]['marque'])))

# Écriture de l'ontologie dans un fichier OWL

g.serialize("pannes.owl", format="xml")
