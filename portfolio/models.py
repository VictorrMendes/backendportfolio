from django.db import models

class Projects(models.Model):
    # Título
    title = models.CharField(max_length=100, blank=True)
    
    # Imagem do projeto (armazena o caminho do arquivo)
    projetc_img = models.ImageField(upload_to='projects/', blank=True, null=True)  
        
    # Ferramentas usadas
    tools = models.CharField(max_length=100, blank=True)
    
    # Parte de trás
    title_back = models.CharField(max_length=100, blank=True)
    
    # Descrição do projeto
    description = models.TextField()
    
    # Link do projeto
    link_project = models.CharField(max_length=255, blank=True)
    
class Senha(models.Model):
    # Senha
    senha = models.CharField(max_length=10, blank=True)
