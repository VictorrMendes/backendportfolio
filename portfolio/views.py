from rest_framework import views, response
from portfolio.models import Projects
from django.conf import settings  

class ProjectsViews(views.APIView):
    def get(self, request):
        project = Projects.objects.last()

        if project is None:
            return response.Response({"message": "Nenhum projeto encontrado"}, status=404)

        
        image_url = request.build_absolute_uri(project.projetc_img.url) 

        return response.Response({
            "title": project.title,
            "projetc_img": image_url,  
            "tools": project.tools,
            "title_back": project.title_back,
            "description": project.description,
            "link_project": project.link_project
        })