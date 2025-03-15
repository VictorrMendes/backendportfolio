from django.contrib import admin
from portfolio.models import Projects, Senha


@admin.register(Projects)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'title','description','projetc_img','tools','title_back','link_project',)

@admin.register(Senha)
class SenhaAdmin(admin.ModelAdmin):
    list_display = ('senha',)   