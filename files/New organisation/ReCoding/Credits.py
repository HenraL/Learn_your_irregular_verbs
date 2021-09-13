class credits:
    def __init__(self):
        self.metaData=[
            {"element":"German words","target":"TheAudioDB","link":"https://www.theaudiodb.com/"},
            {"element":"Definition de mots Français","target":"CNRTL","link":"cnrtl.fr"},
            {"element":"Définition de 'mal comprendre'","target":"Le Parisien","link":"http://dictionnaire.sensagent.leparisien.fr/mal%20comprendre/fr-fr/"},
            {"element":"Phrase d'exemple pour la définition du mot 'contrebalancer'","target":"Word Hippo","link":"https://fr.wordhippo.com/fr/phrases-avec-le-mot/625e802346e3136df4cdb0bf922133544c1063c6.html"},
            {"element":"Search Button Icon","target":"Flaticon","link":"https://www.flaticon.com/free-icon/magnifying-glass_46389?term=magnifing%20glass&page=1&position=6&page=1&position=6&related_id=46389&origin=search"}
            ]
        self.Author={"Surname":"Henry","name":"Letellier","Social":{"Official Website":"http://hanra-latalliar.unaux.com/","Programs Webpage":""}}
    def ressources(self):
        for i in range(len(self.metaData)):
            print(f"{self.metaData[i]['element']}:{self.metaData[i]['target']} ({self.metaData[i]['link']})")
    def TheAuthor(self):
        for i in self.Author:
            if type(self.Author[i])!=type({}):
                print(f"{i}:{self.Author[i]}")
            else:
                print(f"{i}:")
            try:
                for b in self.Author[i]:
                    print(f"\t{b}:{self.Author[i][b]}")
            except:
                pass