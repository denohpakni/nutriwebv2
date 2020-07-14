from django.urls import path

from orderingapp import views


urlpatterns = [
    path('user-dash', views.userDashboard, name='user-dashboard'),
    path('order/<int:id>', views.placeOrder, name='order'),
    path('previousorders', views.showOrderHistory, name='order-history'),
]