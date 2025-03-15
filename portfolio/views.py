from rest_framework import views, response, status
from portfolio.models import Projects, Senha
from django.conf import settings
from .serializers import ProjectSerializer  # Importe o serializer


class ProjectsViews(views.APIView):
    def get(self, request):
        projects = Projects.objects.all()

        if not projects.exists():
            return response.Response({"message": "Nenhum projeto encontrado"}, status=status.HTTP_404_NOT_FOUND)

        projects_data = []
        for project in projects:
            image_url = request.build_absolute_uri(project.projetc_img.url)

            projects_data.append({
                "id": project.id,
                "title": project.title,
                "projetc_img": image_url,
                "tools": project.tools,
                "title_back": project.title_back,
                "description": project.description,
                "link_project": project.link_project
            })

        return response.Response(projects_data)

    def post(self, request):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        try:
            project = Projects.objects.get(pk=pk)
        except Projects.DoesNotExist:
            return response.Response({"message": "Projeto não encontrado"}, status=status.HTTP_404_NOT_FOUND)

        serializer = ProjectSerializer(project, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            project = Projects.objects.get(pk=pk)
        except Projects.DoesNotExist:
            return response.Response({"message": "Projeto não encontrado"}, status=status.HTTP_404_NOT_FOUND)

        project.delete()
        return response.Response(status=status.HTTP_204_NO_CONTENT)


class SenhaViews(views.APIView):
    def get(self, request):
        senha = Senha.objects.last()

        if senha is None:
            return response.Response({"message": "Nenhuma senha cadastrada"}, status=status.HTTP_404_NOT_FOUND)

        senha_data = {
            "senha": senha.senha,
        }

        return response.Response(senha_data)