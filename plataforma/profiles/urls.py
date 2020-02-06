from django.urls import path
from .views import ProfileListView, ProfileDetailView

profiles_patterns = ([
    path('perfiles', ProfileListView.as_view(), name='list'),
    path('perfil/<username>/', ProfileDetailView.as_view(), name='detail'),
], "profiles")
