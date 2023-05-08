"""
This file contains the urls of notes applications
"""
from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path
from notes import views


urlpatterns = [
	path('notes/', views.NoteList.as_view()),
    path('notes/<int:pk>/', views.NoteDetail.as_view()),
    path('users/', views.UserView.as_view()),
    path('login/', views.Login.as_view()),
]


urlpatterns = format_suffix_patterns(urlpatterns)