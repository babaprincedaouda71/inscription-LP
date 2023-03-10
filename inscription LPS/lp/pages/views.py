from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse

from .forms import AccueilForm, InscriptionForm
from .forms import LoginForm

from .models import Lycee, Candidat


from django.contrib.auth.decorators import login_required
from .forms import UserRegistration, UserEditForm, CheckmailForm
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate
from django.contrib.auth import login, authenticate, logout
from .models import Ville, LPs, DiplomeBacPlus2, EtablissementDipBacPlus2, TypeBac, BacMention
from .models import Academie, Lycee, Test, Specialite


def index(request):
    return render(request, "base.html")


def login_view(request):
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                u = form.cleaned_data['username']
                p = form.cleaned_data['password']
                user = authenticate(username=u, password=p)
                if user is not None:
                    if user.is_active:
                        login(request, user)
                        return redirect('pages:printInfos')

                    else:
                        return render(request, 'pages/login.html', {'error1': 'error1', 'form': form})
                else:
                    return render(request, 'pages/login.html', {'error2': 'error2', 'form': form})
        else:
            form = LoginForm()
            return render(request, 'pages/login.html', {'form': form})





def checkmail(request):
    if request.method == 'POST':
        form = CheckmailForm(request.POST)
        if form.is_valid():
            nom = form.cleaned_data['nom']
            prenom = form.cleaned_data['prenom']
            datenais = form.cleaned_data['datenais']
            email = form.cleaned_data['email']
            if Candidat.objects.get(nom = nom, prenom = prenom, dateNaissance = datenais, email = email):
                check = Candidat.objects.get(nom = nom, prenom = prenom, dateNaissance = datenais, email = email)
                cin = check.cin_passeport
                candidat = Candidat.objects.get(cin_passeport = cin)
                return render(request, 'pages/printInfos.html', {'candidat' : candidat})

            else:
                return redirect('pages:checkmail')


    else:
        form = CheckmailForm()
        return render(request, 'pages/checkmail.html', {'form': form})






# def login_view(request):
#         if request.method == 'POST':
#             form = LoginForm(request.POST)
#             if form.is_valid():
#                 u = form.cleaned_data['username']
#                 p = form.cleaned_data['password']
#                 user = authenticate(username=u, password=p)
#                 if user is not None:
#                     if user.is_active:
#                         login(request, user)
#                         return redirect('pages:printInfos')

#                     else:
#                         return render(request, 'pages/login.html', {'error1': 'error1', 'form': form})
#                 else:
#                     return render(request, 'pages/login.html', {'error2': 'error2', 'form': form})
#         else:
#             form = LoginForm()
#             return render(request, 'pages/login.html', {'form': form})






def printInfos(request):
    candidat = Candidat.objects.get(cin_passeport = request.user.username)
    return render(request, "pages/printInfos.html", {'candidat' : candidat})





def inscription(request):
    if request.method == 'POST':
        form = InscriptionForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data 
            user1=form.save(commit=False)
            user1.password = make_password(user1.password)
            user1.save()
            usernam = form.cleaned_data['cin_passeport']
            membre = User()
            membre.username = usernam
            membre.password = user1.password
            membre.save()
            form.save()
            return redirect('pages:login_view')

    else:
        form2 = InscriptionForm()
    return render(request, "pages/inscription.html", {'form' : form})



# @login_required()
# def modiferInscription(request):
#     candidat = Candidat.objects.get(cin_passeport = request.user.username)
#     cities = Ville.objects.all()
#     lps = LPs.objects.all()
#     bacs = TypeBac.objects.all()
#     mentions = BacMention.objects.all()
#     academies = Academie.objects.all()
#     lycees = Lycee.objects.all()
#     diplomes = DiplomeBacPlus2.objects.all()
#     etablissements = EtablissementDipBacPlus2.objects.all()
#     return render(request, "pages/modiferInscription.html", {'candidat' : candidat, 'cities' : cities,
#         'lps' : lps, 'bacs' : bacs, 'mentions' : mentions, 'academies' : academies,
#             'lycees' : lycees, 'diplomes' : diplomes, 'etablissements' : etablissements})






@login_required()
def modiferInscription(request, candidat_id):
    if request.method == 'POST':
        cin = request.POST['cin']
        cne = request.POST['cne']
        nom = request.POST['nom']
        prenom = request.POST['prenom']
        datenais = request.POST['datenais']
        nationalite = request.POST['nationalite']
        email = request.POST['email']
        tel1 = request.POST['tel1']
        # tel2 = request.POST['tel2']
        adr = request.POST['adr']
        residence = request.POST['residence']
        lp = request.POST['lp']
        bac = request.POST['bac']
        anneebac = request.POST['anneebac']
        mentionbac = request.POST['mentionbac']
        academie = request.POST['academie']
        lycee = request.POST['lycee']
        bacplus2 = request.POST['bacplus2']
        etabacplus2 = request.POST['etabacplus2']
        anneebacplus2 = request.POST['anneebacplus2']
        annee1ere = request.POST['annee1ere']
        spdip = request.POST['spdip']
        domdip = request.POST['domdip']
        villedipbacplus2 = request.POST['villedipbacplus2']
        print(villedipbacplus2)
        dureedip = request.POST['dureedip']
        note1ereannee = request.POST['note1ereannee']
        note2emeannee = request.POST['note2emeannee']
        noteobtentiondip = request.POST['noteobtentiondip']
        sem1 = request.POST['sem1']
        sem2 = request.POST['sem2']
        sem3 = request.POST['sem3']
        sem4 = request.POST['sem4']
        # user = request.user.username
        candidat = Candidat.objects.get(cin_passeport = candidat_id)
        print(candidat.cin_passeport)
        candidat.cin_passeport = cin
        candidat.cne_massar = cne
        candidat.nom = nom
        candidat.prenom = prenom
        candidat.dateNaissance = datenais
        candidat.nationalite = nationalite
        candidat.email = email
        candidat.telephone1 = tel1
        # candidat.telephone2 = tel2-
        candidat.addresse = adr
        candidat.ville = residence
        lps = LPs.objects.get(code = lp)
        candidat.codeLPChoisie = lps
        bacs = TypeBac.objects.get(code = bac)
        candidat.codeBac = bacs
        candidat.annee_obtenetion_bac = anneebac
        mentionbacs = BacMention.objects.get(mention = mentionbac)
        candidat.mentionBac = mentionbacs
        academies = Academie.objects.get(academie = academie)
        candidat.academie = academies
        lycees = Lycee.objects.get(nom = lycee)
        candidat.lycee = lycees
        bacplus2s = DiplomeBacPlus2.objects.get(code = bacplus2)
        candidat.diplomeBacPlus2 = bacplus2s
        etabacplus2s = EtablissementDipBacPlus2.objects.get(etablissement = etabacplus2)
        candidat.etablissementDiplomeBacPlus2 = etabacplus2s
        candidat.anneeObtentionDiplomeBacPlus2 = anneebacplus2
        candidat.anneeObtention1ereAnnee = annee1ere
        spdips = Specialite.objects.get(specialite = spdip)
        candidat.specialiteDiplome = spdips
        candidat.dominanceDiplome = domdip
        villedipbacplus2s = Ville.objects.get(ville = villedipbacplus2)
        candidat.villeDiplomeBacPlus2 = villedipbacplus2s
        candidat.dureeObtentionDiplome = dureedip
        candidat.note1ereAnneeDiplome = note1ereannee
        candidat.note2ereAnneeDiplome = note2emeannee
        candidat.noteObtentionDiplome = noteobtentiondip
        candidat.noteSemestre1 = sem1
        candidat.noteSemestre2 = sem2
        candidat.noteSemestre3 = sem3
        candidat.noteSemestre4 = sem4
        member = User.objects.get(username = candidat_id)
        member.username = cin
        candidat.save()
        member.save()
        return redirect('pages:login_view')

    else:
        if request.user.is_active:
            candidat = Candidat.objects.get(cin_passeport = candidat_id)
            cities = Ville.objects.all()
            lps = LPs.objects.all()
            bacs = TypeBac.objects.all()
            mentions = BacMention.objects.all()
            academies = Academie.objects.all()
            lycees = Lycee.objects.all()
            diplomes = DiplomeBacPlus2.objects.all()
            etablissements = EtablissementDipBacPlus2.objects.all()
            specialites = Specialite.objects.all()
            return render(request, "pages/modiferInscription.html", {'candidat' : candidat, 'cities' : cities,
            'lps' : lps, 'bacs' : bacs, 'mentions' : mentions, 'academies' : academies,
            'lycees' : lycees, 'diplomes' : diplomes, 'etablissements' : etablissements, 'specialites' : specialites})










# @login_required()
# def modiferInscription(request, id_dip):
#     if request.user.is_authenticated:
#         dip = Candidat.objects.get(cin_passeport=id_dip)
#         form = ModifierCandidatForm(request.POST or None, instance=dip)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect()
#         else:
#             return render(request, 'pages/modiferInscription.html', {'form': form, 'dip': dip})
#         return render(request, 'pages/modiferInscription.html', {'form': form, 'dip': dip})

#     else:
#         return render(request, 'pages/login.html')



# def modifier_diplome(request, id_dip):
#     if request.user.is_authenticated:
#         dip = DiplomesDuCandidat.objects.get(id=id_dip)
#         form = ModifierDiplomeForm(request.POST or None, instance=dip)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('/diplome')
#         else:
#             return render(request, 'pfe/modifier_diplome.html', {'form': form, 'dip': dip})
#         return render(request, 'pfe/modifier_diplome.html', {'form': form, 'dip': dip})




def test(request):
    if request.method == 'POST':
        cin = request.POST['cin']
        nom = request.POST['nom']
        test = Test()
        test.cin = cin
        test.nom = nom
        test.save()
        return render(request, 'base.html')
    
    else:
        return render(request, "pages/test.html")


def test1(request):
    return render(request, "pages/test1.html")


# AJAX
def load_lycees(request):
    academie_id = request.GET.get('academie_id')
    # codeLPChoisie_id = request.GET.get('codeLPChoisie_id')
    lycees = Lycee.objects.filter(academie_id=academie_id).all()
    # bacs = TypeBac.objects.filter(codeLPChoisie_id=codeLPChoisie_id)
    return render(request, 'pages/lycee_dropdown_list_options.html', {'lycees': lycees})
    # print(list(Lycee.values('id', 'nom')))
    # return JsonResponse(list(Lycee.values('id', 'nom')), safe=False)





# # AJAX
def get_lp_data(request):
    lp_id = request.GET.get('lp_id')
    bacs = TypeBac.objects.filter(lp=lp_id).all
    return render(request, 'pages/get_lp_data.html', {'bacs': bacs})





# # AJAX
def get_dip_data(request):
    lp_id = request.GET.get('lp_id')
    dips = DiplomeBacPlus2.objects.filter(lp=lp_id).all
    return render(request, 'pages/get_dip_data.html', {'dips': dips})





# # AJAX
def get_eta_data(request):
    ville_id = request.GET.get('ville_id')
    etas = EtablissementDipBacPlus2.objects.filter(ville=ville_id).all
    return render(request, 'pages/get_eta_data.html', {'etas': etas})











# test inscription avec {{form.}}
def inscription1(request):
    if request.method == 'POST':
        form2 = InscriptionForm(request.POST)
        if form2.is_valid():
            autrebac = request.POST['autre']
            codebac = request.POST['codeBac']
            print(autrebac)
            print(codebac)
            cd = form2.cleaned_data 
            user1=form2.save(commit=False)
            user1.password = make_password(user1.password)
            user1.save()
            usernam = form2.cleaned_data['cin_passeport']
            email = form2.cleaned_data['email']
            nom = form2.cleaned_data['nom']
            prenom = form2.cleaned_data['prenom']
            membre = User()
            membre.username = usernam
            membre.password = user1.password
            membre.email = email
            membre.save()
            form2.save()
            typebac = TypeBac.objects.get(code = codebac)
            typebac.autre = autrebac
            typebac.save()
            print(typebac.autre)
            print(typebac.autre)
            print(typebac.autre)
            return redirect('pages:login_view')
        else:
            return render(request, "pages/inscription1.html", {'form2' : form2})

    else:
        form2 = InscriptionForm()
        return render(request, "pages/inscription1.html", {'form2' : form2})






# # test inscription avec {{form.}}
# def inscription1(request):
#     if request.method == 'POST':
#         form2 = InscriptionForm(request.POST)
#         if form2.is_valid():
#             cd = form2.cleaned_data 
#             user1=form2.save(commit=False)
#             user1.password = make_password(user1.password)
#             user1.save()
#             usernam = form2.cleaned_data['cin_passeport']
#             membre = User()
#             membre.username = usernam
#             membre.password = user1.password
#             membre.save()
#             form2.save()
#             return redirect('pages:login_view')
#         else:
#             return render(request, "pages/inscription1.html", {'form2' : form2})

#     else:
#         form2 = InscriptionForm()
#         return render(request, "pages/inscription1.html", {'form2' : form2})


















# def register(request):
#     if request.method == 'POST':
#         form = UserRegistration(request.POST or None)
#         if form.is_valid():
#             new_user = form.save(commit=False)
#             new_user.set_password(
#                 form.cleaned_data.get('password')
#             )
#             new_user.save()
#             return render(request, 'authapp/register_done.html')
#     else:
#         form = UserRegistration()

#     context = {
#         "form": form
#     }

#     return render(request, 'pages/register.html', context=context)


# @login_required
# def edit(request):
#     if request.method == 'POST':
#         user_form = UserEditForm(instance=request.user,
#                                  data=request.POST)
#         if user_form.is_valid():
#             user_form.save()
#     else:
#         user_form = UserEditForm(instance=request.user)
#     context = {
#         'form': user_form,
#     }
#     return render(request, 'authapp/edit.html', context=context)










# from django.http import HttpResponse
# from django.views.generic import View

# from lp.utils import render_to_pdf #created in step 4
# import datetime

# class GeneratePdf(View):
#     def get(self, request, *args, **kwargs):
#         data = {
#              'today': datetime.date.today(), 
#              'amount': 39.99,
#             'customer_name': 'Cooper Mann',
#             'order_id': 1233434,
#         }
#         pdf = render_to_pdf('pdf/invoice.html', data)
#         return HttpResponse(pdf, content_type='application/pdf')