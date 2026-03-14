from django.urls import path
from .views import *

urlpatterns = [
    path('dashboard/', dashboard_view, name='dashboard'),
    path('setting-dashboard/', setting_view, name='setting-dashboard'),
    path('product-main-category-list/', product_main_category_view, name='product_main_category_list'),
    path('add_new_product_main_category/', add_product_main_category, name='add_new_product_main_category'),

]
