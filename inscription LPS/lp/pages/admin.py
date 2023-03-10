from django.contrib import admin

from .models import TypeBac, Specialite, BacMention, Ville, Lycee, Academie, DiplomeBacPlus2, EtablissementDipBacPlus2, Departement, LPs, Candidat, ResponsableLPs, LPsDiplomeBacPlus2, LPsBac, Test


class CandidatAdmin(admin.ModelAdmin):
    list_display = ('cin_passeport','cne_massar', 'nom', 'prenom', 'email', 'dateNaissance',)
    ordering = ('cin_passeport',)
    search_fields = ('nom', 'cin_passeport',)

# class TypeBacAdmin(admin.ModelAdmin):
#     list_display = ('code', 'nom', 'lp', 'autre',)
#     ordering = ('code',)
#     search_fields = ('nom',)

class SpecialiteAdmin(admin.ModelAdmin):
    list_display = ('specialite',)
    ordering = ('specialite',)
    search_fields = ('specialite',)

class BacMentionAdmin(admin.ModelAdmin):
    list_display = ('mention',)
    ordering = ('mention',)
    search_fields = ('mention',)
    
class VilleAdmin(admin.ModelAdmin):
    list_display = ('ville',)

class AcademieAdmin(admin.ModelAdmin):
    list_display = ('academie','ville',)

class LyceeAdmin(admin.ModelAdmin):
    list_display = ('code','nom','academie',)


class DiplomeBacPlus2Admin(admin.ModelAdmin):
    list_display = ('code', 'nom', 'nature',)

class EtablissementDipBacPlus2Admin(admin.ModelAdmin):
    list_display = ('code', 'etablissement', 'ville',)

class DepartementAdmin(admin.ModelAdmin):
    list_display = ('code', 'nom', )

class ResponsableLPsAdmin(admin.ModelAdmin):
    list_display = ('code', 'nom', 'prenom',)

    
class LPsAdmin(admin.ModelAdmin):
    list_display = ('code', 'nom', 'codeDept','codeResponsableDept',)


class LPsBacAdmin(admin.ModelAdmin):
    list_display = ('codeLP', 'codeBac',)


class LPsDiplomeBacPlus2Admin(admin.ModelAdmin):
    list_display = ('codeLP', 'codeDiplomeBacPlus2',)

class LPsDiplomeBacPlus2Admin(admin.ModelAdmin):
    list_display = ('codeLP', 'codeDiplomeBacPlus2',)


class LPsBacAdmin(admin.ModelAdmin):
    list_display = ('codeLP', 'codeBac',)




admin.site.register(Candidat, CandidatAdmin)
admin.site.register(ResponsableLPs,ResponsableLPsAdmin)
admin.site.register(LPsDiplomeBacPlus2,LPsDiplomeBacPlus2Admin)
admin.site.register(TypeBac)
admin.site.register(Specialite,SpecialiteAdmin)
admin.site.register(BacMention,BacMentionAdmin)
admin.site.register(Ville,VilleAdmin)
admin.site.register(Lycee,LyceeAdmin)
admin.site.register(Academie,AcademieAdmin)
admin.site.register(DiplomeBacPlus2,DiplomeBacPlus2Admin)
admin.site.register(EtablissementDipBacPlus2,EtablissementDipBacPlus2Admin)
admin.site.register(Departement,DepartementAdmin)
admin.site.register(LPs,LPsAdmin)
admin.site.register(LPsBac, LPsBacAdmin)
