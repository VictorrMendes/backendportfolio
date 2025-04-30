# portfolio/serializers.py
from rest_framework import serializers
from portfolio.models import Projects

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ['title', 'description', 'projetc_img', 'tools', 'title_back', 'link_project']  # Campos do formulário