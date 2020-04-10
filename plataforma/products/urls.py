from django.urls import path
from django.contrib.auth.decorators import login_required

from .views import ProfitProductListAndCreate, ProductListAndCreate, ProductUpdate, ProfitProductUpdate, ProductDelete, ProfitProductDelete

products_patterns = ([
    path('productos/',  login_required(ProductListAndCreate.as_view()), name='ListAndCreate'),
    path('productos/editar/<int:pk>', login_required(ProductUpdate.as_view()), name='update'),
    path('productos/borrar/<int:pk>', login_required(ProductDelete.as_view()), name='delete'),
    path('productos/beneficios/',  login_required(ProfitProductListAndCreate.as_view()), name='profitsListAndCreate'),
    path('productos/beneficios/editar/<int:pk>', login_required(ProfitProductUpdate.as_view()), name='profitsUpdate'),
    path('productos/beneficios/borrar/<int:pk>', login_required(ProfitProductDelete.as_view()), name='profitsDelete'),
], 'products')