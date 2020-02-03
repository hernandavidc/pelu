from django.views.generic import CreateView
from django.views.generic.edit import UpdateView
from django.views import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django import forms

from django.contrib.auth.models import User
from companies.models import Company, Occupation
from .forms import UserCreationFormWithEmail, ProfileForm, EmailForm
from .models import Profile

class SignupCompanyView(View):
    template_name = 'registration/signupCompany.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        print(str(request.POST))
        name = request.POST['companyName']
        direction = request.POST['companyDirection']
        contactNumber = request.POST['companyContactNumbre']
        try:
            company = Company.objects.create(name=name,direction=direction,contactNumber=contactNumber)
        
            first_name = request.POST['companyManagerName']
            last_name = request.POST['companyManagerLastName']
            cc = request.POST['cc']
            username = request.POST['username']
            email = request.POST['email']
            password1 = request.POST['password1']
            password2 = request.POST['password2']

            if (password1==password2):
                company.save()
                user = User.objects.create_user(username, email, password2)
                user.first_name = first_name
                user.last_name = last_name
                occupation, created = Occupation.objects.get_or_create(name='administrador',)
                profile = Profile.objects.create(user=user,company=company,occupation=occupation,cc=cc,access = 'admin')
                profile.save()
                user.profile = profile
                user.save()
            else:
                company.delete()
                raise forms.ValidationError("Las contraseñas deben ser iguales")
        except Exception as e:
            print(e)
            return render(request, self.template_name)
        return redirect(reverse_lazy('login') + '?register')

class SignupView(CreateView):
    form_class = UserCreationFormWithEmail
    template_name = 'registration/signup.html'

    def get_success_url(self):
        return reverse_lazy('login') + '?register'

    def get_form(self, form_class=None):
        form = super(SignupView, self).get_form()
        #Modificar campos en "tiempo rela" del formulario signup para no perder validaciones
        form.fields['username'].widget = forms.TextInput(attrs={'class':'form-control mb-2', 'placeholder':'Nombre de usuario'})
        form.fields['email'].widget = forms.EmailInput(attrs={'class':'form-control mb-2', 'placeholder':'Dirección email'})
        form.fields['password1'].widget = forms.PasswordInput(attrs={'class':'form-control mb-2', 'placeholder':'Contraseña'})
        form.fields['password2'].widget = forms.PasswordInput(attrs={'class':'form-control mb-2', 'placeholder':'Repite la Contraseña'})

        return form

@method_decorator(login_required, name='dispatch')
class ProfileUpdate(UpdateView):
    form_class = ProfileForm
    success_url = reverse_lazy('profile')
    template_name = 'registration/profile_form.html'

    def get_object(self):
        #recuperamos el objeto que se va editar
        profile, created = Profile.objects.get_or_create(user=self.request.user)
        return profile

@method_decorator(login_required, name='dispatch')
class EmailUpdate(UpdateView):
    form_class = EmailForm
    success_url = reverse_lazy('profile')
    template_name = 'registration/profile_email_form.html'

    def get_object(self):
        #recuperamos el objeto que se va editar
        return self.request.user

    def get_form(self, form_class=None):
        form = super(EmailUpdate, self).get_form()
        # Modificar en tiempo real
        form.fields['email'].widget = forms.EmailInput(
            attrs={'class':'form-control mb-2', 'placeholder':'Email'})
        return form