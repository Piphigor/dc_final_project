"""django_dc_final_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

from .views import (
    IndexView,
    StudentCreateView, StudentUpdateView, StudentDeleteView,
    SubjectCreateView, SubjectUpdateView, SubjectDeleteView,
    ScoreCreateView, ScoreUpdateView, ScoreDeleteView
)

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('admin/', admin.site.urls, name='admin'),
    path('student/add/', StudentCreateView.as_view(), name='student_add'),
    path('student/<int:pk>/edit/', StudentUpdateView.as_view(), name='student_edit'),
    path('student/<int:pk>/delete/', StudentDeleteView.as_view(), name='student_delete'),
    path('subject/add/', SubjectCreateView.as_view(), name='subject_add'),
    path('subject/<int:pk>/edit/', SubjectUpdateView.as_view(), name='subject_edit'),
    path('subject/<int:pk>/delete/', SubjectDeleteView.as_view(), name='subject_delete'),
    path('score/add/', ScoreCreateView.as_view(), name='score_add'),
    path('score/<int:pk>/edit/', ScoreUpdateView.as_view(), name='score_edit'),
    path('score/<int:pk>/delete/', ScoreDeleteView.as_view(), name='score_delete'),
]
