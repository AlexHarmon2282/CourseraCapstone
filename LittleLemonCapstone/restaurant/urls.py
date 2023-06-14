from django.contrib import admin 
from django.urls import path 
from . import views
  
urlpatterns = [ 
    path('', views.index, name='index'),
<<<<<<< HEAD
    path('menu/', views.MenuItemView.as_view()),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
=======
    path('menu/', views.menuView.as_view()),
    path('booking/', views.bookingView.as_view)
>>>>>>> parent of 79bea59 (Setup serializers on the menu API, possibly unsuccessfully?)
]