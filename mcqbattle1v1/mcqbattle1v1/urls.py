"""
URL configuration for mcqbattle1v1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from auth_app.views import RegisterView,LoginView,ProtectedView,GetView
from mcqs.views import McqListCreateView,McqRetrieveUpdateDestroyView ,GameListCreateView,GameRetrieveUpdateDestroyView

urlpatterns = [
    
    
    path('admin/', admin.site.urls),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('protected/', ProtectedView.as_view(), name='protected'),
    path('protected/', ProtectedView.as_view(), name='protected'),
    path('get/', GetView.as_view(), name='get'),
    path('mcqs/',McqListCreateView.as_view(),name='mcq-list-create'),
    path('mcqs/<uuid:pk>',McqRetrieveUpdateDestroyView.as_view(),name='mcq-detail'),
    path('games/', GameListCreateView.as_view(), name='game-list-create'),
    path('games/<uuid:pk>/', GameRetrieveUpdateDestroyView.as_view(), name='game-detail'),

]
