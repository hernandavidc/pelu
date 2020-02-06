from django.urls import path
from django.contrib.auth.decorators import login_required

from .views import ProfitProductListAndCreate, ProductListAndCreate, ProductUpdate, ProfitProductUpdate

products_patterns = ([
    path('productos/',  login_required(ProductListAndCreate.as_view()), name='ListAndCreate'),
    path('productos/beneficios/',  login_required(ProfitProductListAndCreate.as_view()), name='profitsListAndCreate'),
    path('productos/editar/<int:pk>', ProductUpdate.as_view(), name='update'),
    path('productos/beneficios/editar/<int:pk>', ProfitProductUpdate.as_view(), name='profitsUpdate'),
], 'products')