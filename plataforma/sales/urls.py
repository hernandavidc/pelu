from django.urls import path
from django.contrib.auth.decorators import login_required

from .views import SaleListAndCreate

sales_patterns = ([
    path('ventas/',  login_required(SaleListAndCreate.as_view()), name='ListAndCreate'),
    # path('ventas/editar/<int:pk>', login_required(ProductUpdate.as_view()), name='update'),
    # path('ventas/borrar/<int:pk>', login_required(ProductDelete.as_view()), name='delete'),
], 'sales')