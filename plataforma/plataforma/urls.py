from django.contrib import admin
from django.urls import path, include

from profiles.urls import profiles_patterns

from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('django.contrib.auth.urls')),
    path('', include('registration.urls')),
    path('', include(profiles_patterns)),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
