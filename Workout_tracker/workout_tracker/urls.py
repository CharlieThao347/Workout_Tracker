"""workout_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from core import views as core_views
from progress import views as progress_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', core_views.home, name='home'),
    path('core/add/', core_views.add),
    path('core/complete/<int:id>/', core_views.complete),
    path('core/view/<int:id>/', core_views.view),
    path('core/view/<int:id>/add_exercise/', core_views.add_exercise),
    path('core/view/<int:id>/edit_exercise/<int:num>/', core_views.edit_exercise),
    path('core/completed_workouts/', core_views.completed_workouts),
    path('core/completed_workouts/completed_view/<int:id>/', core_views.completed_view),
    path('join/', core_views.join),
    path('login/', core_views.user_login),
    path('logout/', core_views.user_logout),
    path('progress/', progress_views.progress),
    path('progress/add/', progress_views.add),
    path('progress/add_entry/', progress_views.add_entry),
]
