from django.contrib import admin
from django.urls import path, include
from django.conf import settings

from products.urls import products_patterns
from profiles.urls import profiles_patterns
from .views import HomePageView, DashboardPageView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('django.contrib.auth.urls')),
    path('', include('registration.urls')),
    path('', include(products_patterns)),
    path('', include(profiles_patterns)),
    path('', HomePageView.as_view(), name='index'),
    path('inicio', DashboardPageView.as_view(), name='dashboard'),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
