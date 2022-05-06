from django.urls import path
from .views import *

urlpatterns = [
    path('', home),
    # path('test/', test),
]

# urlpatterns = [
#     path('', views.project_index, name='project_index'),
#     path('<int:pk>/', views.project_detail, name='project_detail'),
# ]