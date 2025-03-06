from django.contrib import admin
from portfolio.models import Projects


@admin.register(Projects)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'title','description','projetc_img','tools','title_back','link_project')
    