from django.urls import path

from applications.product.views import ProductListView, ProductDetailView

urlpatterns = [
    path('products-list/', ProductListView.as_view()),
    path('products-list/<int:pk>/', ProductDetailView.as_view()),
]