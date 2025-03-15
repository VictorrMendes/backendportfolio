from django.db import models

class Projects(models.Model):
    #titulo
    title = models.CharField(max_length=100, blank=True)
    
    #link da imagem
    projetc_img = models.ImageField(upload_to='projects/')  
    
    #ferramentas
    tools = models.CharField(max_length=100, blank=True)
    #Parte de trás
    title_back = models.CharField(max_length=100, blank=True)
    
    #descrição
    description = models.TextField()
    
    #link do projeto
    link_project = models.CharField(max_length=255, blank=True)
    
class Senha(models.Model):
    #Senha
    senha = models.CharField(max_length=10, blank=True)
