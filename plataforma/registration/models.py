from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

from companies.models import Company, Occupation

def custom_upload_to(instance, filename):
    old_instance = Profile.objects.get(pk=instance.pk)
    old_instance.avatar.delete()
    return 'profiles/' + filename

class Profile(models.Model):
    ACCESS_CHOICES = [
        ('admin', 'Administrador'),
        ('collaborator', 'Colaborador'),
        ('other', 'otro'),
    ]
    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    company = models.ForeignKey(Company, verbose_name="Empresa", related_name="getEmployees", on_delete=models.PROTECT)
    occupation = models.ForeignKey(Occupation, verbose_name="Ocupación", related_name="getProfiles", on_delete=models.PROTECT)
    avatar = models.ImageField(upload_to=custom_upload_to, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    cc = models.PositiveIntegerField(unique=True,verbose_name="Cédula",null=True, blank=True, error_messages={'unique':"Esta cedula ya tiene vinculada una cuenta."})
    link = models.URLField(max_length=200, null=True, blank=True)
    birthday = models.DateTimeField(verbose_name="Cumpleaños", default=datetime.now, null=True, blank=True)
    access = models.CharField(max_length=12,choices=ACCESS_CHOICES,default='collaborator',)
    
    class Meta:
        ordering = ['user__username']

    def __str__(self):
        return self.cc + ' ' + self.user.username

@receiver(post_save, sender=User)
def ensure_profile_exists(sender, instance, **kwargs):
    if kwargs.get('created', False):
        Profile.objects.get_or_create(user=instance)


