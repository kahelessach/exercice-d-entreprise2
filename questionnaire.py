import json


# PROJET QUESTIONNAIRE V3 : POO
#
# - Pratiquer sur la POO
# - Travailler sur du code existant
# - Mener un raisonnement
#
# -> Définir les entitées (données, actions)
#
# Question
#    - titre       - str
#    - choix       - (str)
#    - bonne_reponse   - str
#
#    - poser()  -> bool
#
# Questionnaire
#    - questions      - (Question)
#
#    - lancer()
#

class Question:
    filename = "cinema_starwars_debutant.json"
    file = open(filename, "r")
    json_data = file.read()      
    file.close()
    questionnaire_data = json.loads(json_data)
        
    def __init__(self, titre, choix, bonne_reponse):
        self.titre = titre
        self.choix = choix
        self.bonne_reponse = bonne_reponse
        

   

    def FromData(data):
        # ....
        q = Question(data[2], data[0], data[1])
        return q

    def poser(self):
        #print(f"Categorie {self.questionaire_data['categorie']}")
        print("Catégorie: " + self.questionnaire_data['categorie'])
        print ("Titre: " + self.questionnaire_data['titre'])
        print("  " + self.titre)
        for i in range(len(self.choix)):
            print("  ", i+1, "-", self.choix[i])

        print()
        resultat_response_correcte = False
        reponse_int = Question.demander_reponse_numerique_utlisateur(1, len(self.choix))
        if self.choix[reponse_int-1].lower() == self.bonne_reponse.lower():
            print("Bonne réponse")
            resultat_response_correcte = True
        else:
            print("Mauvaise réponse")
            
        print()
        return resultat_response_correcte

    def demander_reponse_numerique_utlisateur(min, max):
        reponse_str = input("Votre réponse (entre " + str(min) + " et " + str(max) + ") :")
        try:
            reponse_int = int(reponse_str)
            if min <= reponse_int <= max:
                return reponse_int

            print("ERREUR : Vous devez rentrer un nombre entre", min, "et", max)
        except:
            print("ERREUR : Veuillez rentrer uniquement des chiffres")
        return Question.demander_reponse_numerique_utlisateur(min, max)
    
class Questionnaire:
    def __init__(self, questions):
        self.questions = questions

    def lancer(self):
        score = 0
        for question in self.questions:
            if question.poser():
                score += 1
        print("Score final :", score, "sur", len(self.questions))
        return score

"""
questionnaire = (
    ("Quelle est la capitale de la France ?", ("Marseille", "Nice", "Paris", "Nantes", "Lille"), "Paris"), 
    ("Quelle est la capitale de l'Italie ?", ("Rome", "Venise", "Pise", "Florence"), "Rome"),
    ("Quelle est la capitale de la Belgique ?", ("Anvers", "Bruxelles", "Bruges", "Liège"), "Bruxelles")
                )

lancer_questionnaire(questionnaire)

# q1 = Question("Quelle est la capitale de la France ?", ("Marseille", "Nice", "Paris", "Nantes", "Lille"), "Paris")
# q1.poser()

# data = (("Marseille", "Nice", "Paris", "Nantes", "Lille"), "Paris", "Quelle est la capitale de la France ?")
# q = Question.FromData(data)
# print(q.__dict__)

Questionnaire(
    (
    
    Question("Quelle est la capitale de la France ?", ("Marseille", "Nice", "Paris", "Nantes", "Lille"), "Paris"), 
    Question("Quelle est la capitale de l'Italie ?", ("Rome", "Venise", "Pise", "Florence"), "Rome"),
    Question("Quelle est la capitale de la Belgique ?", ("Anvers", "Bruxelles", "Bruges", "Liège"), "Bruxelles")
    )
).lancer()
"""
filename = "cinema_starwars_debutant.json"
file = open(filename, "r")
json_data = file.read()      
file.close()
questionnaire_data = json.loads(json_data)
#print(questionnaire_data['categorie'])
#recuperation des titres

titles = [ques['titre'] for ques in questionnaire_data['questions']]
#print(len(titles))
def recuperation_question():
    liste_question = []
    indice_titles = 0
    for i in range(len(titles)):
        liste_question.append(titles[indice_titles])
        indice_titles +=1
    return liste_question

rep = recuperation_question()
print(rep[1])

#recuperation des choix reponse str et la solution

def gestion_reponse(type, reponse_str):
    choix = [ques['choix'] for ques in questionnaire_data['questions']]
    choix_reponse = [reponse[type] for reponse in choix[reponse_str]]

 
    #print(choix_reponse)

type_reponse_str = 0#type(true/false = 1), str(reponse pour utilisateur = 0)
indice_reponse = 0#indice de defilement des reponses
for i in range(len(titles)):        
    gestion_reponse(type_reponse_str, indice_reponse)
    indice_reponse +=1