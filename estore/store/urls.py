from django.urls import path

from . import views

urlpatterns = [
	
	path('', views.store, name="store"),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),
    path('search/', views.product_search, name='search'),
    path('views/<int:product_id>/', views.product_view, name='views'),

	path('update_item/', views.updateItem, name="update_item"),
	path('process_order/', views.processOrder, name="process_order"),

]