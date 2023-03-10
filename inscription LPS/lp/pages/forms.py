from django import forms
from django.contrib.auth.models import User
from phonenumber_field.formfields import PhoneNumberField
from django_countries.fields import CountryField
from .models import TypeBac, BacMention, Ville, Lycee, Academie, DiplomeBacPlus2, EtablissementDipBacPlus2, Departement, LPs, Candidat, ResponsableLPs, LPsDiplomeBacPlus2, LPsBac, Test
from django.forms.widgets import DateInput
from django.contrib.auth.forms import UserChangeForm

class dateInput(forms.DateInput):
    input_type = 'date'

class AccueilForm(forms.Form):
    inscription = forms.ChoiceField(choices=[("inscrire", "S'inscrire"), ('modifier', "Modification d'anciennes informations")], widget = forms.RadioSelect(), label = "")


# class InscriptionForm(forms.Form):
#     cin_passeport = forms.CharField(max_length = 10, label = 'CIN ou Passeport')
#     cne_massar = forms.CharField(max_length = 10, label = 'CNE ou Massar')
#     nom = forms.CharField(max_length = 20)
#     prenom = forms.CharField(max_length = 60)
#     password = forms.CharField(max_length = 20, widget = forms.PasswordInput)
#     confirmPassword = forms.CharField(max_length = 20, widget = forms.PasswordInput)
#     dateNaissance = forms.DateTimeField(widget = dateInput)
#     nationalite = CountryField(blank_label ='(Sélectionner un pays)').formfield()
#     email = forms.EmailField()
#     telephone1 = forms.CharField(max_length = 15, label = "Téléphone")
#     telephone2 = forms.CharField(max_length = 15, label = "Téléphone")
#     adresse = forms.CharField(max_length=200)
#     ville = forms.CharField(max_length = 60)
#     codeLPChoisie = forms.ModelChoiceField(queryset= LPs.objects.all())
#     codeBac = forms.ModelChoiceField(queryset= TypeBac.objects.all())
#     lp = forms.ModelChoiceField(queryset=LPs.objects.all())
#     mentionBac = forms.ModelChoiceField(queryset= BacMention.objects.all())
#     annee_obtention_bac = forms.DateTimeField(widget = dateInput)
#     academie = forms.ModelChoiceField(queryset = Academie.objects.all())
#     lycee = forms.ModelChoiceField(queryset = Lycee.objects.all())
#     diplomeBacPlus2 = forms.ModelChoiceField(queryset = DiplomeBacPlus2.objects.all())
#     etablissementDiplomeBacPlus2 = forms.ModelChoiceField(queryset = EtablissementDipBacPlus2.objects.all())
#     anneeObtentionDiplômeBacPlus2 = forms.DateTimeField(widget = dateInput)
#     dominanceDiplome = forms.CharField(max_length = 60)
#     villeDiplomeBacPlus2 = forms.CharField(label = "Ville Diplome")
#     anneeObtention1ereAnnee = forms.DecimalField()
#     specialiteDiplome = forms.CharField(label = "Spécialité")
#     note1ereAnneeDiplome = forms.DecimalField()
#     note2ereAnneeDiplome = forms.DecimalField()
#     noteObtentionDiplome = forms.DecimalField()
#     noteSemestre1 = forms.DecimalField()
#     noteSemestre2 = forms.DecimalField()
#     noteSemestre3 = forms.DecimalField()
#     noteSemestre4 = forms.DecimalField()

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['lycee'].queryset = Lycee.objects.none()


    
# class InscriptionForm(forms.ModelForm):
#     class Meta:
#         model = Candidat
#         fields = ('cin_passeport', 'cne_massar', 'nom', 'prenom', 'password', 'dateNaissance', 'nationalite', 'email', 'telephone1', 'telephone2', 'addresse', 'ville', 'codeBac', 'annee_obtenetion_bac', 'mentionBac', 'lyceeAcademie', 'DiplomeBacPlus2', 'dominanceDiplome', 'etablissementDiplomeBacPlus2', 'anneeObtention1ereAnnee', 'note1ereAnneeDiplome', 'note2ereAnneeDiplome', 'noteObtentionDiplome', 'noteSemestre1', 'noteSemestre2', 'noteSemestre3', 'noteSemestre4', 'codeLPChoisie', 'documentJustificatif')
#         widgets = {
#       'password': forms.PasswordInput(),
#       'dateNaissance': forms.DateInput(attrs={'type': 'date'})
#          }



class InscriptionForm(forms.ModelForm):
    class Meta:
        model = Candidat
        fields = ('cin_passeport', 'cne_massar', 'nom', 'prenom', 'password', 
        'dateNaissance', 'nationalite', 'email', 'telephone1', 'telephone2',
         'addresse', 'ville', 'codeLPChoisie', 'codeBac', 'annee_obtenetion_bac',
          'mentionBac', 'academie', 'lycee', 'diplomeBacPlus2',
           'etablissementDiplomeBacPlus2', 'anneeObtentionDiplomeBacPlus2',
            'anneeObtention1ereAnnee', 'specialiteDiplome', 'dominanceDiplome',
             'villeDiplomeBacPlus2', 'dureeObtentionDiplome',
              'note1ereAnneeDiplome', 'note2ereAnneeDiplome', 'noteObtentionDiplome',
               'noteSemestre1', 'noteSemestre2', 'noteSemestre3', 'noteSemestre4')
        widgets = {
      'password': forms.PasswordInput(),
      'dateNaissance': forms.DateInput(attrs={'type': 'date'})
         }

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['lycee'].queryset = Lycee.objects.none()


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label="CIN")
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))



class CheckmailForm(forms.Form):
    nom = forms.CharField(max_length=60, label = "Nom")
    prenom = forms.CharField(max_length=60, label = "Prénom")
    datenais = forms.DateTimeField(widget = dateInput, label = "Date de naissance")
    email = forms.EmailField(max_length=60, label = "Email")
        



class UserRegistration(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Repeat Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

        def clean_password2(self):
            cd = self.cleaned_data
            if cd['password'] != cd['password2']:
                raise forms.ValidationError('Passwords don\'t match.')
            return cd['password2']


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


# class ModifierCandidatForm(UserChangeForm):
#     cin_passeport = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ex: 2015/2016'}))
#     cne_massar = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ex: 2015/2016'}))
#     nom = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ex: 2015/2016'}))
#     prenom = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ex: 2015/2016'}))
#     dateNaissance =  CountryField(blank_label ='()').formfield()
#     nationalite = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ex: 2015/2016'}))
#     email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ex: 2015/2016'}))
#     telephone1 = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ex: 2015/2016'}))
#     telephone2 = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ex: 2015/2016'}))
#     addresse = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ex: 2015/2016'}))
#     ville = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ex: 2015/2016'}))
#     codeLPChoisie = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ex: 2015/2016'}))
#     codeBac = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ex: 2015/2016'}))
#     annee_obtenetion_bac = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ex: 2015/2016'}))
#     mentionBac = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ex: 2015/2016'}))
#     academie = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ex: 2015/2016'}))
#     lycee = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ex: 2015/2016'}))
#     diplomeBacPlus2 = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ex: 2015/2016'}))
#     etablissementDiplomeBacPlus2 = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ex: 2015/2016'}))
#     anneeObtentionDiplomeBacPlus2 = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ex: 2015/2016'}))
#     anneeObtention1ereAnnee = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ex: 2015/2016'}))
#     specialiteDiplome = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ex: 2015/2016'}))
#     dominanceDiplome = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ex: 2015/2016'}))
#     villeDiplomeBacPlus2 = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ex: 2015/2016'}))
#     dureeObtentionDiplome = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ex: 2015/2016'}))
#     note1ereAnneeDiplome = forms.DecimalField(max_length = 200)
#     note2ereAnneeDiplome = forms.DecimalField(max_length = 200)
#     noteObtentionDiplome = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ex: 2015/2016'}))
#     noteSemestre1 = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ex: 2015/2016'}))
#     noteSemestre2 = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ex: 2015/2016'}))
#     noteSemestre3 = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ex: 2015/2016'}))
#     noteSemestre4 = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ex: 2015/2016'}))


    class Meta:
        model = Candidat
        fields = ['cin_passeport','cne_massar', 'nom', 'prenom', 'dateNaissance', 'nationalite', 'email',
                  'telephone1', 'telephone2', 'addresse', 'ville', 'codeLPChoisie', 'codeBac', 'annee_obtenetion_bac', 
                  'mentionBac', 'academie', 'lycee', 'diplomeBacPlus2', 'etablissementDiplomeBacPlus2', 
                  'anneeObtentionDiplomeBacPlus2', 'anneeObtention1ereAnnee', 'specialiteDiplome', 'dominanceDiplome',
                  'villeDiplomeBacPlus2', 'dureeObtentionDiplome', 'note1ereAnneeDiplome', 'note2ereAnneeDiplome',
                   'noteObtentionDiplome', 'noteSemestre1', 'noteSemestre2', 'noteSemestre3', 'noteSemestre4']

