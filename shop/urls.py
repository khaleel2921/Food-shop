from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='hm'),
    path('<slug:category_slug>/',views.home,name='prod_category'),
    path('<slug:category_slug>/<slug:product_slug>',views.prodDetails,name='details'),
    path('search',views.searching,name='search'),
]