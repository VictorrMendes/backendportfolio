from django.urls import path
from django.http import JsonResponse
from portfolio.views import ProjectsViews
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("projects/", ProjectsViews.as_view()),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
