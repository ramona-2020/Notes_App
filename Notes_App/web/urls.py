from django.urls import path
from Notes_App.web import views

"""
    Routes:
    • http://localhost:8000/ - home page
    • http://localhost:8000/add - add note page
    • http://localhost:8000/edit/:id - edit note page
    • http://localhost:8000/delete/:id - delete note page
    • http://localhost:8000/details/:id - note details page
    • http://localhost:8000/profile - profile page
"""

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('profile/', views.profile, name='profile'),
    path('profile/create/', views.create_profile, name='profile create'),
    path('profile/delete/', views.delete_profile, name='profile delete'),
    path('add/', views.add_note, name='add note'),
    path('edit/<int:pk>/', views.edit_note, name='edit note'),
    path('delete/<int:pk>/', views.delete_note, name='delete note'),
    path('details/<int:pk>/', views.note_details, name='note details'),
]
