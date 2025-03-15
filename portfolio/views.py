from rest_framework import views, response, serializers
from portfolio.models import Projects, Senha
from django.conf import settings  


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ('id', 'title','description','projetc_img','tools','title_back','link_project',)

class ProjectsViews(views.APIView):
    def get(self, request):
        projects = Projects.objects.all()

        if not projects.exists():
            return response.Response({"message": "Nenhum projeto encontrado"}, status=404)

        projects_data = []
        for project in projects:
            image_url = request.build_absolute_uri(project.projetc_img.url) if project.projetc_img else None

            projects_data.append({
                "title": project.title,
                "projetc_img": image_url,  
                "tools": project.tools,
                "title_back": project.title_back,
                "description": project.description,
                "link_project": project.link_project
            })

        return response.Response(projects_data)
    

    def post(self, request):
        data = request.data
        serializer = ProjectSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response({"message": "projeto criado com sucesso"})


    
    
class SenhaViews(views.APIView):
    def get(self, request):
        senha = Senha.objects.last()

        if senha is None:
            return response.Response({"message": "Nenhuma senha cadastrada"}, status=404)

        senha_data = {
                "senha": senha.senha,
            }

        return response.Response(senha_data)
    

