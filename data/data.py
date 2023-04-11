

panne_data={
    1: {'panne': "L'ordinateur ne démarre pas", 'composant': 'Alimentation', 'type_panne': 'Problème de démarrage', 'marque': 'Dell', 'solution': "Remplacement de l'alimentation", 'type_solution': 'Remplacement de composant'},
    2: {'panne': "L'ordinateur ne démarre pas", 'composant': 'Batterie CMOS', 'type_panne': 'Problème de démarrage', 'marque': 'HP', 'solution': 'Remplacement de la batterie CMOS', 'type_solution': 'Remplacement de composant'},
    3: {'panne': "L'ordinateur ne démarre pas", 'composant': 'Carte mère', 'type_panne': 'Problème de démarrage', 'marque': 'Asus', 'solution': 'Remplacement de la carte mère', 'type_solution': 'Remplacement de composant'},
    4: {'panne': "L'ordinateur est lent", 'composant': 'Disque dur', 'type_panne': 'Performance', 'marque': 'Lenovo', 'solution': 'Remplacement du disque dur par un disque SSD', 'type_solution': 'Mise à jour matérielle'},
    5: {'panne': "L'ordinateur est lent", 'composant': 'Mémoire vive', 'type_panne': 'Performance', 'marque': 'Dell', 'solution': 'Ajout de mémoire vive', 'type_solution': 'Mise à jour matérielle'},
    6: {'panne': "L'ordinateur ne détecte pas une clé USB", 'composant': 'Port USB', 'type_panne': 'Panne de périphérique', 'marque': 'HP', 'solution': 'Mise à jour du pilote USB', 'type_solution': 'Mise à jour logicielle'},
    7: {'panne': "L'écran est noir", 'composant': 'Carte graphique', 'type_panne': "Problème d'affichage", 'marque': 'Asus', 'solution': 'Remplacement de la carte graphique', 'type_solution': 'Remplacement de composant'},
    8: {'panne': "Le système d'exploitation ne démarre pas", 'composant': 'Disque dur', 'type_panne': 'Problème de démarrage', 'marque': 'Lenovo', 'solution': "Réinstallation du système d'exploitation", 'type_solution': 'Réinstallation logicielle'},
    9: {'panne': "Le système d'exploitation ne démarre pas", 'composant': 'Carte mère', 'type_panne': 'Problème de démarrage', 'marque': 'Dell', 'solution': 'Remplacement de la carte mère', 'type_solution': 'Remplacement de composant'},
    10: {'panne': "Le système d'exploitation ne démarre pas", 'composant': 'Disque dur', 'type_panne': 'Problème de démarrage', 'marque': 'HP', 'solution': 'Réparation du secteur de démarrage', 'type_solution': 'Réparation logicielle'},
    11: {'panne': "L'ordinateur chauffe anormalement", 'composant': 'Ventilateur', 'type_panne': 'Surchauffe', 'marque': 'Asus', 'solution': 'Nettoyage du ventilateur', 'type_solution': 'Entretien'},
    12: {'panne': "Le lecteur CD ne fonctionne pas", 'composant': 'Lecteur CD/DVD', 'type_panne': 'Panne de périphérique', 'marque': 'Lenovo', 'solution': 'Remplacement du lecteur CD/DVD', 'type_solution': 'Remplacement de composant'},
    13: {'panne': 'Le lecteur DVD ne fonctionne pas', 'composant': 'Lecteur CD/DVD', 'type_panne': 'Panne de périphérique', 'marque': 'Dell', 'solution': 'Mise à jour du pilote du lecteur CD/DVD', 'type_solution': 'Mise à jour logicielle'},
    14: {'panne': 'Le clavier ne fonctionne pas', 'composant': 'Clavier', 'type_panne': 'Panne de périphérique', 'marque': 'HP', 'solution': 'Remplacement du clavier', 'type_solution': 'Remplacement de composant'},
    15: {'panne': 'La souris ne fonctionne pas', 'composant': 'Souris', 'type_panne': 'Panne de périphérique', 'marque': 'Asus', 'solution': 'Mise à jour du pilote de la souris', 'type_solution': 'Mise à jour logicielle'},
    16: {'panne': 'Le ventilateur fait du bruit', 'composant': 'Ventilateur', 'type_panne': 'Bruits étranges', 'marque': 'Lenovo', 'solution': 'Remplacement du ventilateur', 'type_solution': 'Remplacement de composant'},
    17: {'panne': "L'écran clignote", 'composant': 'Carte graphique', 'type_panne': "Problème d'affichage", 'marque': 'Dell', 'solution': 'Mise à jour du pilote de la carte graphique', 'type_solution': 'Mise à jour logicielle'},
    18: {'panne': "Le disque dur émet un bruit étrange", 'composant': 'Disque dur', 'type_panne': 'Bruits étranges', 'marque': 'HP', 'solution': 'Remplacement du disque dur', 'type_solution': 'Remplacement de composant'},
    19: {'panne': "Le PC se fige régulièrement", 'composant': 'Mémoire vive', 'type_panne': 'Problème de stabilité', 'marque': 'Asus', 'solution': 'Test et remplacement des barrettes de mémoire vive défectueuses', 'type_solution': 'Remplacement de composant'},
    20: {'panne': 'Le PC se fige régulièrement', 'composant': 'Carte mère', 'type_panne': 'Problème de stabilité', 'marque': 'Lenovo', 'solution': 'Mise à jour du BIOS', 'type_solution': 'Mise à jour logicielle'},
    21: {'panne': "L'ordinateur ne démarre pas", 'composant': 'Alimentation', 'type_panne': 'Problème de démarrage', 'marque': 'Dell', 'solution': "Remplacement de l'alimentation", 'type_solution': 'Remplacement de composant'},
    22: {'panne': 'Le disque dur est plein', 'composant': 'Disque dur', 'type_panne': 'Espace de stockage insuffisant', 'marque': 'HP', 'solution': "Suppression de fichiers inutiles et/ou ajout d'un disque dur externe", 'type_solution': 'Entretien'},
    23: {'panne': "L'ordinateur ne détecte pas le périphérique USB", 'composant': 'Port USB', 'type_panne': 'Panne de périphérique', 'marque': 'Asus', 'solution': 'Mise à jour du pilote du port USB', 'type_solution': 'Mise à jour logicielle'},
    24: {'panne': "L'ordinateur ralentit", 'composant': 'Processeur', 'type_panne': 'Performances réduites', 'marque': 'Lenovo', 'solution': 'Nettoyage du ventilateur et/ou mise à jour du pilote du processeur', 'type_solution': 'Entretien/Mise à jour logicielle'},
    25: {'panne': "L'écran est noir", 'composant': 'Écran', 'type_panne': "Problème d'affichage", 'marque': 'Dell', 'solution': "Vérification des câbles de connexion et/ou remplacement de l'écran", 'type_solution': 'Remplacement de composant'},
    26: {'panne': "Le PC se bloque au démarrage", 'composant': 'Disque dur', 'type_panne': 'Problème de démarrage', 'marque': 'HP', 'solution': "Vérification de l'état du disque dur et/ou réinstallation du système d'exploitation", 'type_solution': 'Entretien/Mise à jour logicielle'},
    27: {'panne': "Le PC ne s'éteint pas", 'composant': "Système d'exploitation", 'type_panne': "Problème d'arrêt", 'marque': 'Asus', 'solution': "Mise à jour du système d'exploitation et/ou nettoyage du registre", 'type_solution': 'Mise à jour logicielle/Entretien'},
    28: {'panne': 'Le PC redémarre tout seul', 'composant': "Système d'exploitation", 'type_panne': 'Problème de redémarrage', 'marque': 'Lenovo', 'solution': "Vérification des températures et/ou mise à jour du système d'exploitation", 'type_solution': 'Entretien/Mise à jour logicielle'},
    29: {'panne': 'Le PC émet des bips au démarrage', 'composant': 'Carte mère', 'type_panne': 'Problème de démarrage', 'marque': 'Dell', 'solution': 'Vérification de la mémoire RAM et/ou remplacement de la carte mère', 'type_solution': 'Remplacement de composant'},
    30: {'panne': 'Le ventilateur est bruyant', 'composant': 'Ventilateur', 'type_panne': 'Bruits anormaux', 'marque': 'HP', 'solution': 'Nettoyage du ventilateur et/ou remplacement du ventilateur', 'type_solution': 'Entretien/Remplacement de composant'},
    31: {'panne': "L'ordinateur ne se connecte pas à Internet", 'composant': 'Carte réseau', 'type_panne': 'Problème de connexion', 'marque': 'Asus', 'solution': 'Vérification des pilotes de la carte réseau et/ou réinitialisation de la carte réseau', 'type_solution': 'Mise à jour logicielle/Entretien'},
    32: {'panne': "L'ordinateur plante régulièrement", 'composant': 'Mémoire RAM', 'type_panne': 'Problème de performances', 'marque': 'Lenovo', 'solution': 'Test de la mémoire RAM et/ou remplacement de la mémoire RAM', 'type_solution': 'Remplacement de composant'},
    33: {'panne': 'Le son ne fonctionne plus', 'composant': 'Carte son', 'type_panne': 'Problème audio', 'marque': 'Dell', 'solution': 'Mise à jour du pilote de la carte son et/ou remplacement de la carte son', 'type_solution': 'Mise à jour logicielle/Remplacement de composant'},
    34: {'panne': 'Le clavier ne fonctionne plus', 'composant': 'Clavier', 'type_panne': 'Problème de périphérique', 'marque': 'HP', 'solution': 'Vérification des connexions et/ou remplacement du clavier', 'type_solution': 'Remplacement de composant'},
    35: {'panne': 'La souris ne fonctionne plus', 'composant': 'Souris', 'type_panne': 'Problème de périphérique', 'marque': 'Asus', 'solution': 'Vérification des connexions et/ou remplacement de la souris', 'type_solution': 'Remplacement de composant'},
    36: {'panne': 'Le PC surchauffe', 'composant': 'Ventilateur', 'type_panne': 'Problème de surchauffe', 'marque': 'Lenovo', 'solution': 'Nettoyage du ventilateur et/ou vérification de la pâte thermique', 'type_solution': 'Entretien'},
    37: {'panne': "L'ordinateur affiche des pixels morts", 'composant': 'Écran', 'type_panne': "Problème d'affichage", 'marque': 'Dell', 'solution': "Vérification des pixels morts et/ou remplacement de l'écran", 'type_solution': 'Remplacement de composant'},
    38: {'panne': 'Le PC redémarre tout seul', 'composant': 'Alimentation', 'type_panne': "Problème d'alimentation", 'marque': 'HP', 'solution': "Test de l'alimentation et/ou remplacement de l'alimentation", 'type_solution': 'Remplacement de composant'},
    39: {'panne': "Le PC ne s'allume plus", 'composant': 'Alimentation', 'type_panne': "Problème d'alimentation", 'marque': 'Asus', 'solution': "Test de l'alimentation et/ou remplacement de l'alimentation", 'type_solution': 'Remplacement de composant'},
    40: {'panne': 'Le PC affiche un écran bleu', 'composant': 'Pilote', 'type_panne': 'Problème de logiciel', 'marque': 'Lenovo', 'solution': "Mise à jour des pilotes et/ou réinstallation du système d'exploitation", 'type_solution': 'Mise à jour logicielle/Réinstallation'},
    41: {'panne': 'Le PC ne détecte pas les périphériques USB', 'composant': 'Carte mère', 'type_panne': 'Problème de périphérique', 'marque': 'HP', 'solution': 'Mise à jour du BIOS et/ou remplacement de la carte mère', 'type_solution': 'Mise à jour logicielle/Remplacement de composant'},
    42: {'panne': 'Le PC affiche un écran noir', 'composant': 'Carte graphique', 'type_panne': "Problème d'affichage", 'marque': 'Dell', 'solution': 'Test de la carte graphique et/ou remplacement de la carte graphique', 'type_solution': 'Remplacement de composant'},
    43: {'panne': 'Le PC ne se connecte pas au Wi-Fi', 'composant': 'Carte réseau sans fil', 'type_panne': 'Problème de connexion', 'marque': 'Asus', 'solution': 'Vérification des pilotes de la carte réseau sans fil et/ou réinitialisation de la carte réseau', 'type_solution': 'Mise à jour logicielle/Entretien'},
    44: {'panne': 'Le PC ne se met pas en veille', 'composant': "Système d'exploitation", 'type_panne': 'Problème de logiciel', 'marque': 'Lenovo', 'solution': "Mise à jour du système d'exploitation et/ou réinitialisation des paramètres de veille", 'type_solution': 'Mise à jour logicielle/Entretien'},
    45: {'panne': "L'ordinateur est lent", 'composant': 'Disque dur', 'type_panne': 'Problème de performances', 'marque': 'HP', 'solution': "Optimisation du système d'exploitation et/ou remplacement du disque dur", 'type_solution': 'Mise à jour logicielle/Remplacement de composant'},
    46: {'panne': 'Le PC ne reconnaît pas les CD/DVD', 'composant': 'Lecteur de CD/DVD', 'type_panne': 'Problème de périphérique', 'marque': 'Dell', 'solution': 'Mise à jour des pilotes du lecteur et/ou remplacement du lecteur', 'type_solution': 'Mise à jour logicielle/Remplacement de composant'},
    47: {'panne': 'Le PC chauffe trop', 'composant': 'Ventilateur', 'type_panne': 'Problème de refroidissement', 'marque': 'Asus', 'solution': 'Nettoyage du ventilateur et/ou remplacement du ventilateur', 'type_solution': 'Entretien/Remplacement de composant'},
    48: {'panne': "Le PC n'émet pas de son", 'composant': 'Carte son', 'type_panne': 'Problème de son', 'marque': 'Lenovo', 'solution': 'Mise à jour des pilotes de la carte son et/ou remplacement de la carte son', 'type_solution': 'Mise à jour logicielle/Remplacement de composant'},
    49: {'panne': 'Le PC se fige', 'composant': 'Mémoire vive', 'type_panne': 'Problème de performances', 'marque': 'HP', 'solution': 'Test de la mémoire vive et/ou remplacement de la mémoire vive', 'type_solution': 'Remplacement de composant'},
    50: {'panne': 'Le PC ne charge pas la batterie', 'composant': 'Chargeur', 'type_panne': "Problème d'alimentation", 'marque': 'Dell', 'solution': 'Test du chargeur et/ou remplacement du chargeur', 'type_solution': 'Remplacement de composant'},
    51: {'panne': 'Le PC redémarre en boucle', 'composant': 'Carte mère', 'type_panne': 'Problème de démarrage', 'marque': 'Asus', 'solution': 'Test de la carte mère et/ou remplacement de la carte mère', 'type_solution': 'Remplacement de composant'},
    52: {'panne': 'Le PC affiche un écran bleu', 'composant': 'Carte graphique', 'type_panne': 'Problème d\'affichage', 'marque': 'HP', 'solution': 'Mise à jour des pilotes de la carte graphique et/ou remplacement de la carte graphique', 'type_solution': 'Mise à jour logicielle/Remplacement de composant'},
    53: {'panne': 'Le clavier ne fonctionne pas', 'composant': 'Clavier', 'type_panne': 'Problème de périphérique', 'marque': 'Lenovo', 'solution': 'Test du clavier et/ou remplacement du clavier', 'type_solution': 'Remplacement de composant'},
    54: {'panne': 'La souris ne fonctionne pas', 'composant': 'Souris', 'type_panne': 'Problème de périphérique', 'marque': 'Dell', 'solution': 'Test de la souris et/ou remplacement de la souris', 'type_solution': 'Remplacement de composant'},
    55: {'panne': 'Le PC ne se connecte pas à Internet', 'composant': 'Carte réseau', 'type_panne': 'Problème de connexion', 'marque': 'HP', 'solution': 'Mise à jour des pilotes de la carte réseau et/ou remplacement de la carte réseau', 'type_solution': 'Mise à jour logicielle/Remplacement de composant'},
    56: {'panne': 'Le PC ne démarre pas', 'composant': 'Alimentation', 'type_panne': 'Problème d\'alimentation', 'marque': 'Asus', 'solution': 'Test de l\'alimentation et/ou remplacement de l\'alimentation', 'type_solution': 'Remplacement de composant'},
    57: {'panne': 'Le PC affiche des lignes verticales sur l\'écran', 'composant': 'Carte graphique', 'type_panne': 'Problème d\'affichage', 'marque': 'Dell', 'solution': 'Mise à jour des pilotes de la carte graphique et/ou remplacement de la carte graphique', 'type_solution': 'Mise à jour logicielle/Remplacement de composant'},
    58: {'panne': 'Le PC émet des bruits inhabituels', 'composant': 'Ventilateur', 'type_panne': 'Problème de bruit', 'marque': 'HP', 'solution': 'Nettoyage du ventilateur et/ou remplacement du ventilateur', 'type_solution': 'Entretien/Remplacement de composant'},
    59: {'panne': 'Le PC ne détecte pas les périphériques USB', 'composant': 'Port USB', 'type_panne': 'Problème de périphérique', 'marque': 'Asus', 'solution': 'Mise à jour des pilotes du port USB et/ou remplacement du port USB', 'type_solution': 'Mise à jour logicielle/Remplacement de composant'},
    60: {'panne': 'Le PC ne détecte pas le disque dur', 'composant': 'Disque dur', 'type_panne': 'Problème de stockage', 'marque': 'Dell', 'solution': 'Test du disque dur et/ou remplacement du disque dur', 'type_solution': 'Remplacement de composant'},
    61: {'panne': 'Le PC ne détecte pas la carte graphique', 'composant': 'Carte graphique', 'type_panne': 'Problème d\'affichage', 'marque': 'HP', 'solution': 'Mise à jour des pilotes de la carte graphique et/ou remplacement de la carte graphique', 'type_solution': 'Mise à jour logicielle/Remplacement de composant'},
    62: {'panne': 'Le PC émet un bip au démarrage', 'composant': 'Carte mère', 'type_panne': 'Problème de démarrage', 'marque': 'Lenovo', 'solution': 'Vérification du BIOS et/ou remplacement de la carte mère', 'type_solution': 'Mise à jour logicielle/Remplacement de composant'},
    63: {'panne': 'Le PC ne s\'allume plus du tout', 'composant': 'Alimentation', 'type_panne': 'Problème d\'alimentation', 'marque': 'Asus', 'solution': 'Test de l\'alimentation et/ou remplacement de l\'alimentation', 'type_solution': 'Remplacement de composant'},
    64: {'panne': 'Le PC affiche une image déformée', 'composant': 'Carte graphique', 'type_panne': 'Problème d\'affichage', 'marque': 'Dell', 'solution': 'Mise à jour des pilotes de la carte graphique et/ou remplacement de la carte graphique', 'type_solution': 'Mise à jour logicielle/Remplacement de composant'},
    65: {'panne': 'Le PC émet des bips au démarrage', 'composant': 'Mémoire vive', 'type_panne': 'Problème de mémoire', 'marque': 'HP', 'solution': 'Test de la mémoire vive et/ou remplacement de la mémoire vive', 'type_solution': 'Remplacement de composant'},
    66: {'panne': 'Le PC ne s\'éteint pas complètement', 'composant': 'Système d\'exploitation', 'type_panne': 'Problème de logiciel', 'marque': 'Lenovo', 'solution': 'Mise à jour du système d\'exploitation et/ou réinstallation du système d\'exploitation', 'type_solution': 'Mise à jour logicielle/Réinstallation'},
    67: {'panne': 'Le PC ne détecte pas l\'imprimante', 'composant': 'Port USB', 'type_panne': 'Problème de périphérique', 'marque': 'Asus', 'solution': 'Vérification des pilotes de l\'imprimante et/ou remplacement du port USB', 'type_solution': 'Mise à jour logicielle/Remplacement de composant'},
    68: {'panne': 'Le PC affiche une erreur de mémoire', 'composant': 'Mémoire vive', 'type_panne': 'Problème de mémoire', 'marque': 'Dell', 'solution': 'Test de la mémoire vive et/ou remplacement de la mémoire vive', 'type_solution': 'Remplacement de composant'},
    69: {'panne': 'Le PC ne démarre pas après une mise à jour', 'composant': 'Système d\'exploitation', 'type_panne': 'Problème de logiciel', 'marque': 'HP', 'solution': 'Réparation ou réinstallation du système d\'exploitation', 'type_solution': 'Réinstallation/Mise à jour logicielle'},
    70: {'panne': 'Le PC ne détecte pas le clavier', 'composant': 'Port USB', 'type_panne': 'Problème de périphérique', 'marque': 'Lenovo', 'solution': 'Vérification des pilotes du clavier et/ou remplacement du port USB', 'type_solution': 'Mise à jour logicielle/Remplacement de composant'},
    71: {'panne': 'Le PC ne se connecte pas au Wi-Fi', 'composant': 'Carte réseau', 'type_panne': 'Problème de réseau', 'marque': 'Asus', 'solution': 'Vérification des pilotes de la carte réseau et/ou remplacement de la carte réseau', 'type_solution': 'Mise à jour logicielle/Remplacement de composant'},
    72: {'panne': 'Le PC ne détecte pas le moniteur', 'composant': 'Carte graphique', 'type_panne': 'Problème d\'affichage', 'marque': 'Dell', 'solution': 'Mise à jour des pilotes de la carte graphique et/ou remplacement de la carte graphique', 'type_solution': 'Mise à jour logicielle/Remplacement de composant'},
    73: {'panne': 'Le PC affiche un écran bleu au démarrage', 'composant': 'Système d\'exploitation', 'type_panne': 'Problème de logiciel', 'marque': 'HP', 'solution': 'Réparation ou réinstallation du système d\'exploitation', 'type_solution': 'Réinstallation/Mise à jour logicielle'},
    74: {'panne': 'Le PC ne détecte pas le disque dur externe', 'composant': 'Port USB', 'type_panne': 'Problème de périphérique', 'marque': 'Lenovo', 'solution': 'Vérification des pilotes du port USB et/ou remplacement du port USB', 'type_solution': 'Mise à jour logicielle/Remplacement de composant'},

}



