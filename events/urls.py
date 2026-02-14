from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('events/', views.event_list, name='event_list'),
    path('events/<int:id>/', views.event_detail, name='event_detail'),
    path('events/create/', views.event_create, name='event_create'),
    path('events/<int:id>/edit/', views.event_edit, name='event_edit'),
    path('events/<int:id>/delete/', views.event_delete, name='event_delete'),
    path('categories/', views.category_list, name='category_list'),
    path('categories/create/', views.category_create, name='category_create'),
    path('categories/<int:id>/edit/', views.category_edit, name='category_edit'),
    path('categories/<int:id>/delete/', views.category_delete, name='category_delete'),
    path('participants/', views.participant_list, name='participant_list'),
    path('participants/create/', views.participant_create, name='participant_create'),
    path('participants/<int:id>/edit/', views.participant_edit, name='participant_edit'),
    path('participants/<int:id>/delete/', views.participant_delete, name='participant_delete'),
]
