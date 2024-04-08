from django.contrib import admin
from django.urls import path
from cafes.views import *
from django.conf import settings
from django.conf.urls.static import static

app_name='cafes'

urlpatterns = [
    path('', MenuLV.as_view(), name='index'),
    path('<int:pk>/', MenuDV.as_view(), name='detail'),
    path('<int:pk>/ review/create/', ReviewCreateView.as_view(), name='review_create'),
    path('<int:pk>/review/<int:review_id>/delete/', ReviewDelete, name='review_delete'),
    path('menu/create/', MenuCreateView.as_view(), name='create'),
    path('<int:pk>/menu/update/', MenuUpdateView.as_view(), name='update'),
    path('<int:pk>/menu/delete/', MenuDeleteView.as_view(), name='delete'),
    path('<int:pk>/order/create/',OrderCreate, name='order_create'),
    path('order/',OrderLV.as_view(), name='order_index'),
    path('order/<int:pk>/delete',OrderDelete, name='order_delete'),


]
