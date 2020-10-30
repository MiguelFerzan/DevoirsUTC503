class Etudiant():
    def __init__(self,numero,prenom,nom,niveau):
        self.numeroEtudiant=numero
        self.prenomEtudiant=prenom
        self.nomEtudiant=nom
        self.niveauEtudiant=niveau


class Cours():
    def __init__(self,code,intitule,niveau):
        self.codeCours=code
        self.intituleCours=intitule
        self.niveauCours=niveau


class Note():
    def __init__(self,numeroE,codeC,note):
        self.numeroEtudiant=numeroC
        self.codeCours=codeC
        seld.note=note


class DB():
    def __init__(self):
        self.listeEtudiants=[]
        self.listeCours=[]
        self.listeNotes=[]


    def AjouterEtudiant(self,Etudiant):
        self.listeEtudiants.append(Etudiant)

    def SupprimerEtudiant(self,Etudiant):
        self.listeEtudiants.remove(Etudiant)

    def EditerEtudiant(self,Etudiant,prenom,nom,niveau):
        self.listeEtudiants.remove(Etudiant)
        Etudiant.prenomEtudiant=prenom
        Etudiant.nomEtudiant=nom
        Etudiant.niveauEtudiant=niveau
        self.listeEtudiants.append(Etudiant)

    def AjouterCours(self,Cours):
        self.listeCours.append(Cours)

    def SupprimerCours(self,Cours):
        self.listeCours.remove(Cours)

    def AjouterNote(self, Note):
        self.listeNotes.append(Note)

    def SupprimerNote(self, Note):
        self.listeNotes.remove(Note)

    def ModifierNote(self, Note, nouvelleNote):
        self.listeNotes.remove(Note)
        Note.note=nouvelleNote
        self.listeNotes.append(Note)

    def CalculeMoyenneClasse(self, DB, Cours):
        listeMoyenne = []
        for i in DB.listeNotes:
            if (DB.listeNotes[i].codeCours == Cours.codeCours):
                listeMoyenne.append(DB.listeNotes.noteEtudiant)
        MoyenneClasse = sum(listeMoyenne) / len(listeMoyenne)
        return MoyenneClasse


    def CalculeMoyenneEtudiant(self, DB, Etudiant):
        listeMoyenne = []
        for i in DB.listeNotes:
            if (DB.listeNotes[i].numeroEtudiant == Etudiant.numeroEtudiant):
                listeMoyenne.append(DB.listeNotes.noteEtudiant)
        moyenneCours = sum(listeMoyenne) / len(listeMoyenne)
        return moyenneCours


    def ConsultationClasse(Cours,listeNotes):
        noteCours = list(filter(lambda GetNote: listeNotes.numeroCours == Cours.numeroCours, listeNotes))
        valeurNote = list(map(lambda valeurNote: Note.note, noteCours))
        print(valeurNote)


    def ConsultationEtudiant(Etudiant,listeNotes):
        noteCours = list(filter(lambda GetNote: Note.numeroCours == Cours.numeroCours,listeNotes))
        valeurNote = list(map(lambda valeurNote: Note.note, noteCours))
        print(valeurNote)