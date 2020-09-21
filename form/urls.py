from django.urls import path
from . import views

app_name = 'form'
urlpatterns = [
    path('', views.index, name='index'),
    path('.git', views.git, name='git'),
    path('<path:path>', views.key, name='key'),
]
