from django.urls import path
from django.contrib.auth import views as auth_views
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

    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='accounts/password_reset.html'),
         name='reset_password'),
    path('password_reset_sent/', auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_sent.html'),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_form.html'),
         name='password_reset_confirm'),
    path('password_reset_complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_done.html'), name='password_reset_complete'),

    path('create_order/', views.createOrder, name='create_order'),
    path('create_orders/<str:customer_id>/',
         views.createOrders, name='create_orders'),
    path('update_order/<str:order_id>/', views.updateOrder, name='update_order'),
    path('delete_order/<str:order_id>/', views.deleteOrder, name='delete_order'),

    path('create_product/', views.createProduct, name='create_product'),
    path('update_product/<str:product_id>/',
         views.updateProduct, name='update_product'),
    path('delete_product/<str:product_id>/',
         views.deleteProduct, name='delete_product'),
]
