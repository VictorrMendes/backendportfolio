from rest_framework import serializers
from portfolio.models import Projects

class ProjectSerializer(serializers.ModelSerializer):
    tools = serializers.CharField(max_length=100, required=False, allow_blank=True, allow_null=True)
    title_back = serializers.CharField(max_length=100, required=False, allow_blank=True, allow_null=True)
    link_project = serializers.CharField(max_length=255, required=False, allow_blank=True, allow_null=True)

    class Meta:
        model = Projects
        fields = ['id', 'title', 'description', 'projetc_img', 'tools', 'title_back', 'link_project']