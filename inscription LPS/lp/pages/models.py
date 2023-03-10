from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField
from django.forms.fields import FileField


class Departement(models.Model):
    code = models.CharField(max_length = 2, primary_key = True)
    nom = models.CharField(max_length = 120)

    def __str__(self):
        return "%s" %(self.code)


class ResponsableLPs(models.Model):
    code = models.CharField(max_length = 10, primary_key = True)
    nom = models.CharField(max_length = 60, default="")
    prenom = models.CharField(max_length = 60, default="")
    email = models.EmailField()
    telephone = PhoneNumberField(blank=True)

    def __str__(self):
        return "%s" %(self.nom)




class Specialite(models.Model):
    specialite = models.CharField(max_length = 120, unique = True)

    def __str__(self):
        return "%s" %(self.specialite)



class LPs(models.Model):
    code = models.CharField(max_length = 10, primary_key = True)
    nom = models.CharField(max_length = 120, default="")
    codeDept = models.ForeignKey(Departement, on_delete=models.CASCADE)
    codeResponsableDept = models.ForeignKey(ResponsableLPs , on_delete=models.CASCADE)

    def __str__(self):
        return "%s" %(self.code)





class TypeBac(models.Model):
    code = models.CharField(max_length = 20, primary_key=True)
    nom = models.CharField(max_length = 60, unique=True)
    lp = models.ManyToManyField(LPs)
    autre = models.CharField(max_length = 300, default = "", blank = True)

    def __str__(self):
        return "%s" %(self.code)



class BacMention(models.Model):
    mention = models.CharField(max_length = 20, primary_key =True)

    def __str__(self):
        return "%s" %(self.mention)


LYCEE_CHOICES = (
    ('My IDRIS', 'My IDRIS'),
    ('My Abdellah', 'My Abdellah'),
    ('Med V', 'Med V'),
    ('My Youssef', 'My Youssef'),
)

VILLE_CHOICES = (
    ('Agadir','Agadir'),
    ('Beni Mellal','Beni Mellal'),
    ('Casablanca','Casablanca'),
    ('Dakhla','Dakhla'),
    ('El Jadida','El Jadida'),
    ('Fes','Fes'),
    ('Kenitra','Kenitra'),
    ('Khenifra','Khenifra'),
    ('Laayoune','Laayoune'),
    ('Larache','Larache'),
    ('Marrakech','Marrakech'),
    ('Martil','Martil'),
    ('Meknes','Meknes'),
    ('Mohammedia','Mohammedia'),
    ('Oujda','Oujda'),
    ('Rabat','Rabat'),
    ('Sale','Sale'),
    ('Tanger','Tanger'),
    ('Tetouan','Tetouan'),
    ('Dakhla', 'Dakhla'),
    ('Laayoune', 'Laayoune'),
    ('Guelmim', 'Guelmim'),
    ('Tafilalet', 'Tafilalet'),
    ('Souss', 'Souss')

)

ANNEEBAC_CHOICES = (
    ("2010", "2010"),
    ("2011", "2011"),
    ("2012", "2012"),
    ("2013", "2013"),
    ("2014", "2014"),
    ("2015", "2015"),
    ("2016", "2016"),
    ("2017", "2017"),
    ("2018", "2018"),
    ("2019", "2019"),
    ("2020", "2020"),
)


class Ville(models.Model):
    ville = models.CharField(max_length = 50, primary_key = True)

    def __str__(self):
        return "%s" %(self.ville)

class EtablissementDipBacPlus2(models.Model):
    code = models.AutoField(db_column='BID', primary_key = True)
    etablissement = models.CharField(max_length = 180)
    ville = models.ForeignKey(Ville, on_delete=models.CASCADE, default="")

    def __str__(self):
        return "%s" %(self.etablissement)




class Academie(models.Model):
    academie = models.CharField(max_length = 100)
    ville = models.ForeignKey(Ville, on_delete=models.CASCADE)

    def __str__(self):
        return "%s" %(self.academie)


class Lycee(models.Model):
    code = models.AutoField(db_column='BID', primary_key = True)
    nom = models.CharField(max_length = 100)
    academie = models.ForeignKey(Academie, on_delete=models.CASCADE)

    def __str__(self):
        return "%s" %(self.nom)

    



class DiplomeBacPlus2(models.Model):
    code = models.CharField(max_length = 10, primary_key=True)
    nom = models.CharField(max_length = 120)
    nature = models.CharField(max_length = 120, blank=True)
    lp = models.ManyToManyField(LPs)

    def __str__(self):
        return "%s" %(self.code)




class LPsBac(models.Model):
    codeLP = models.ForeignKey(LPs, on_delete=models.CASCADE)
    codeBac = models.ForeignKey(TypeBac, on_delete=models.CASCADE)
    class Meta:
        unique_together = ('codeLP', 'codeBac')

    # def _str_(self):
    #     return self.codeBac
    def __str__(self):
        return "%s %s" %(self.codeLP.nom, self.codeBac.nom)



class LPsDiplomeBacPlus2(models.Model):
    codeLP = models.ForeignKey(LPs, on_delete=models.CASCADE)
    codeDiplomeBacPlus2 = models.ForeignKey(DiplomeBacPlus2, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('codeLP', 'codeDiplomeBacPlus2')

    def __str__(self):
        return "%s" %(self.codeLP)


class Candidat(models.Model):
    cin_passeport = models.CharField(max_length = 10, unique = True)
    cne_massar = models.CharField(max_length = 10, null = False)
    nom = models.CharField(max_length = 20)
    prenom = models.CharField(max_length = 60)
    password = models.CharField(max_length = 20)
    dateNaissance = models.DateField()
    nationalite = CountryField(blank_label ='(Sélectionner un pays)')
    email = models.EmailField(unique = True)
    telephone1 = PhoneNumberField(blank=False)
    telephone2 = PhoneNumberField(blank=True)
    addresse = models.CharField(max_length=200, blank=True)
    ville = models.CharField(max_length = 60, choices=VILLE_CHOICES)
    codeBac = models.ForeignKey(TypeBac, on_delete=models.CASCADE)
    annee_obtenetion_bac = models.CharField(max_length = 5, choices = ANNEEBAC_CHOICES, default = "2018")
    mentionBac = models.ForeignKey(BacMention, on_delete=models.CASCADE)
    academie = models.ForeignKey(Academie, on_delete=models.CASCADE)
    lycee = models.ForeignKey(Lycee, on_delete=models.CASCADE)
    diplomeBacPlus2 = models.ForeignKey(DiplomeBacPlus2, on_delete=models.CASCADE)
    etablissementDiplomeBacPlus2 = models.ForeignKey(EtablissementDipBacPlus2, on_delete=models.CASCADE)
    anneeObtentionDiplomeBacPlus2 = models.CharField(max_length = 4, choices = ANNEEBAC_CHOICES, default = "2020")
    anneeObtention1ereAnnee = models.CharField(max_length = 4, choices = ANNEEBAC_CHOICES, default = "2019")
    specialiteDiplome = models.ForeignKey(Specialite, on_delete=models.CASCADE, default="")
    dominanceDiplome = models.CharField(max_length = 60, null = True, blank = True)
    villeDiplomeBacPlus2 = models.ForeignKey(Ville, on_delete=models.CASCADE)
    dureeObtentionDiplome = models.CharField(max_length = 1)
    note1ereAnneeDiplome = models.CharField(max_length = 6, blank = True)
    note2ereAnneeDiplome = models.CharField(max_length = 6, blank = True)
    noteObtentionDiplome = models.CharField(max_length = 6, blank = True)
    noteSemestre1 = models.CharField(max_length = 6, blank = True)
    noteSemestre2 = models.CharField(max_length = 6, blank = True)
    noteSemestre3 = models.CharField(max_length = 6, blank = True)
    noteSemestre4 = models.CharField(max_length = 6, blank = True)
    codeLPChoisie = models.ForeignKey(LPs, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom



class Test(models.Model):
    cin_passeport = models.CharField(max_length = 10, primary_key = True)
    nom = models.CharField(max_length = 10, null = False)

    def __str__(self):
        return "%s" %(self.nom)


