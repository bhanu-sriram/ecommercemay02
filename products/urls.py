from products import views
from django.urls import path
urlpatterns = [
    path('hello/',views.hello),
    path('allproducts/',views.get_products),
    path('productbyid/<int:id>',views.get_product_by_id),
    path('createproduct/',views.create_product),
]