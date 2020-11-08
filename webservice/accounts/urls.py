from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.products, name='products'),
    path('customer/<str:pk>/', views.customer, name='customer'),

    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('user/', views.userPage, name='user'),
    path('account/', views.accountSettings, name='account'),

    path('create_order/', views.createOrder, name='create_order'),
    path('create_orders/<str:customer_id>/',
         views.createOrders, name='create_orders'),
    path('update_order/<str:order_id>/', views.updateOrder, name='update_order'),
    path('delete_order/<str:order_id>/', views.deleteOrder, name='delete_order'),

]
