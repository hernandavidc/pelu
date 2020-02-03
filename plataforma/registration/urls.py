from django.urls import path
from .views import SignupView, ProfileUpdate, EmailUpdate, SignupCompanyView

urlpatterns = [
    path('crear/empresa', SignupCompanyView.as_view(), name="signupCompany"),
    #path('crear/perfil', SignupView.as_view(), name="signup"),
    path('perfil/', ProfileUpdate.as_view(), name="profile"),
    path('perfil/email/', EmailUpdate.as_view(), name="profile_email"),
]